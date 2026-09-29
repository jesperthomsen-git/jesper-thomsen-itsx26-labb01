#                         DITT UPPDRAG
# Läs minst två av kursens datakällor.
# Identifiera och räkna minst ett säkerhetsrelevant mönster.
# Extrahera och sammanställ käll-IP-adresser.
# Jämför observerade adresser mot suspicious_ips.txt.
# Hantera minst ett formatfel eller saknat fält begripligt.
# Skriv en reproducerbar rapport till output/security_report.txt.
# Analysera minst en observation med slutsats, osäkerhet och säkerhetsbetydelse.
# Dokumentera hur programmet körs, testas och avgränsas.
#
#
#                         FUNKTIONSKRAV
#[X] Programmet kan köras från dokumenterad projektrot.
#[X] Indata öppnas för läsning och originalfilerna ändras inte.
#[X] Minst två datakällor behandlas.
#[X] Minst ett mönster räknas eller sammanställs.
#[X] IOC-listan läses och används för medlemskontroll.
#[X] Felaktiga eller ofullständiga rader hanteras explicit.
#[X] Rapporten skapas i output/ och kan återskapas med samma indata.
#[X] Resultatet sorteras eller presenteras på ett stabilt och begripligt sätt.
#
#                         Definition of Done
#[X] Rätt dataset och analyserade filer anges.
#☐ Programmet körs enligt README.
#[X] Originaldata är oförändrad.
#[X] Minst två datakällor analyseras.
#[X] IOC-jämförelse och minst ett räknat mönster finns.
#[X] Felaktig data hanteras och redovisas.
#[X] Rapportfilen genereras i output/.
#[X] analysis.md innehåller observation, slutsats, osäkerhet, alternativ förklaring och säkerhetsbetydelse.
#[X] Minst tre testfall är dokumenterade.
#☐ AI-användning är redovisad och verifierad.
#[X] Repositoryt innehåller meningsfull commit-historik.
#[X] Canvas-inlämningen länkar direkt till rätt leverans.


import csv #importerar moduler för att skapa csv filer
import re #importerar requests, har denna fall i fall jag kommer använda den i framtiden
from pathlib import Path #använder mig av pathlib biblioteket för att hitta filer och mappar
import os #samma som ovan
import subprocess #För att installera pandas om det inte finns på systemet #beta
import sys #För att installera pandas om det inte finns på systemet #beta
import numpy as np #för att kunna hantera summeringar längre ner när det kommer till matchningar inom arrays
import difflib as dl #behövs inte i mitt program längre och är en legacy import som användes för att matcha arrays mot IOC

folder = Path("week39-security-automation/data")
output_path = "week39-security-automation/output/security_report.csv"



print("Kontrollerar om pandas biblioteket är installerat, vänligen vänta.")

#Skapar ett stabilt test som kontrollerar om du har pandas installerat som bibliotek, om den inte hittar pandas så importeras subprocess och sys för att kunne skapa ett kommando
#som force installerar pandas genom koden [sys.executable, "-m", "pip", "install", "--upgrade", "--force-install", "pandas"]. Denna variant av kod hittades på ett forum som heter stack overflow och har sedan återanvänts för detta syfte.
try:        
    print("Försöker att importera Pandas")
    import pandas as pd
    print("Importering utav Pandas lyckades\n")
except ImportError as e:
    print(f"Pandas import gick inte igenom, error: {e}")
    print("Försöker att installera/ominstallera Pandas för att se om detta hjälper..")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "--force-install", "pandas"],
        check=True
    ) 
try:
    print("kontrollerar version för att se om pandas är installerat rätt")
    import pandas as pd
    print("v Pandas version: v")
    print(pd.__version__)
except ImportError as e:
    print(f"Pandas import gick inte egenom igen, error: {e}")
    print("Avslutar scriptet.")
    sys.exit()
    



def load_indicators(folder): #berättar vart filen finns  

    print("Kontrollerar filer i /data finns för uppgiften")
    folder = Path(folder)
    #"dataframes" är termen som pandas använder sig utav i många av deras variabler och något som har hjälpt mig att kunna koppla deras material och exempler till detta program 
    dataframes = [] 
    total_lines = 0
    
    log_files = [
        file for file in folder.rglob("*.log")
        if file.is_file()
        ]
    
    for file in log_files:
        try:
            file_lines = 0
            
            with file.open("r", encoding="utf-8") as f:
                
                for line in f:
                    line = line.strip()
                    
                    if line:
                        dataframes.append({
                            "log_entry": line,
                            "source_file": str(file)            
                        })
                        
                        file_lines += 1
                print(f"{file} har {file_lines} linjer som har lästs in.")
            total_lines += file_lines

#Att göra tries istället för ifs känns som en stadigare resurs då du har möjlighet att få ordentliga statuskoder som berättar vad som är fel
#Detta är något jag kommer använda mig utav i majoriteten av mitt program.

        except Exception as error: 
            print(f"Kunde inte läsa {file}: {error}") 
    
    print(
        f"Totalt {total_lines} blev inlästa"
    )
        
    return pd.DataFrame(dataframes), total_lines

def analyse_logs(log_files):
    print("Kontrollerar filer för analys..")
    
    if log_files.empty:
            print("Det finns inget att analysera")
            return pd.DataFrame()
    
    print("Kompilerar loggar till en security_report.CSV fil")
    
    #Skapat regex för att kunne filtrera för att skapa en grund för bättre matching av kolumner
    #
    #I denna del har jag haft väldigt mycket problem och den del jag förmodligen har använt mest tid i.
    #När in-datan extraheras så kom alla rader in på en rad.
    #Dessa variabler filtrerar indata genom regex kod för att kontrollera indata är relevant och sedan fyller in data i förbestämda kolumner nedan.
    
    date_time = (
        r"(?P<date>20\d{2}-\d{2}-\d{2})"
        r"(?P<time>T\d{2}:\d{2}:\d{2})"
    )

    ip_pattern = (
        r"(?P<ip_address>"
        r"(?<![\d.])"
        r"(?:\d{1,3}\.){1,3}\d{1,3}"
        r"(?![\d.])"
        r")"
    )
    
    users = r"user=(?P<user>\S+)"
    
    events = (
        r"(?:event=)?"
        r"(?P<event>DENY|DROP|ALLOW|Failed login)"
    )
    
    methods = r"method=(?P<method>[A-Za-z]+)"

    status_codes = r"status=(?P<status_code>\d{3})"
    
    log_file = log_files.reset_index(drop=True).copy()
    
    #filtrerar hela min dataframe genom regex filter och inte bara log_files som jag kommenterade ovan
    #filtered_logs = log_files.loc[combined_filter].copy() Denna kod behövs inte längre med är grunden för mitt kombinerade kommando för advancerad filtrering.
    #koden ovan gav mig en grun att arbeta på och kommer reflektera på detta i min analys för felfall.
    
    
    #sammanställer regex från strings som matchades innan tillsammans med andra strings som blir extraherade genom pd.concat
    csv_formatting = pd.concat( 
        [
            log_file["log_entry"].str.extract(
                date_time,
                expand=True
            ),
            
            log_file["log_entry"].str.extract(
                ip_pattern,
                expand=True
            ),
            
            log_file["log_entry"].str.extract(
                users,
                expand=True
            ),

            log_file["log_entry"].str.extract(
                events,
                expand=True
            ),
            log_file["log_entry"].str.extract(
                status_codes,
                expand=True
            ),  
            log_file["log_entry"].str.extract(
                methods,
                expand=True
            )
        ],
        axis=1
    )
    
    csv_formatting["log_entry"] = log_file["log_entry"]
    csv_formatting["source_file"] = log_file["source_file"]
    
    
    #Skapandet utav layout för CSV dokumentet och kommer användas framöver för att kalla på specifika kolumner för data extrahering.
    csv_formatting = csv_formatting [
        [
            "source_file",
            "date",
            "time",
            "ip_address",
            "user",
            "event",
            "status_code",
            "method",
            "log_entry",
            
        ]
        
    ]
    
    #ip_count är en variabel som kallar på kolumnen "ip_address" som en referens.
    #.value_counts() har varit första gången jag har använt mig utav räknesätt i python, numpys .sum() är en annan funktion jag kommer använda mycket i framtida kod.  
    ip_count =  csv_formatting["ip_address"].value_counts(dropna=True)
    
    
    #En try funktion som kontrollerar om "ip_frequency" och "TOT_IOC" redan finns fördefinerat eller inte, då ignoreras denna try och ignorerar fel
    #Första tröskeln var att försöka lägga till nya kolumner i mitt program och är evidens att programmet i sig är både robust men skör vid vissa aspekter.
    #Som att försöka lägga till fler kolumner efter Regex och fördefinerade kolumner var satta.
    #Försök var gjorde att implementera dessa men genom att använda Jupyter som en säker miljö så lyckades jag få fram denna kod som inspirerats från både Pandas.pydata.org och youtube videos.
    try:
        csv_formatting = csv_formatting.drop( #ignorerar fel eller om dessa redan existerar
        columns=["ip_frequency", "TOT_IOC"],
        errors="ignore"
        )
        
        csv_formatting.insert(
        loc=4,
        column="ip_frequency",
        value=(
            csv_formatting["ip_address"]
            .map(ip_count)
            .fillna(0)
            .astype(int)
            )
        )
        csv_formatting.insert(
                loc=len(csv_formatting.columns),
                column="TOT_IOC",
                value=0
        )
    except ValueError as e:
        print(f"Fel uppstod med att skapa kolumnerna: {e}")
    
    csv_formatting["status_code"] = csv_formatting["status_code"].astype(str)
    
    csv_formatting["TOT_IOC"] += (csv_formatting["ip_frequency"] - 1).clip(lower=0)
    
    
    #Testar att indentera långa strängar
    csv_formatting.loc[csv_formatting["user"].eq("admin"),
        "TOT_IOC"
    ] += 1
    
    csv_formatting.loc[csv_formatting["user"].eq("root"),
        "TOT_IOC"
    ] += 2
    
    csv_formatting.loc[csv_formatting["status_code"].eq("401"),
        "TOT_IOC"
    ] += 2
    
    csv_formatting.loc[csv_formatting["event"].eq("DENY"), 
    "TOT_IOC"
    ] += 1
    
    csv_formatting.loc[csv_formatting["event"].eq("Failed login"),
    "TOT_IOC"
    ] += 3
    #ser ganska märkligt ut..
    #När man kollar på hur vissa människor indenterar så ser deras kod väldigt märkligt ut men ser detta som en övning i sig
    #att kunna skapa bra struktur både för mig själv men också för andra som försöker förstå min kod.
    
    csv_formatting.sort_values(
        "TOT_IOC",
        ascending=False,
        inplace=True
    ) 
    
    #skapar en reset från föregående kolumner så allt nollställs fall i fall.
    csv_formatting.reset_index( 
        drop=True,
        inplace=True
    )   
    
    print("IP Addresser som extraherades samt antal: ", ip_count)
    
    print("SKAPAR FULLSTÄNDIG RAPPORT I CSV FILEN MED SUMMERING, VÄNLIGEN VÄNTA\n")
    
    summary_values = (
        csv_formatting["TOT_IOC"]
        .apply(lambda score: "Hög risk" if score >= 10 else "Medel risk")
    )
    
    
    csv_formatting.insert(
        loc=len(csv_formatting.columns),
        column="-----_SCORE_-----",
        value=summary_values
    )
    
    return csv_formatting, ip_count
    
def write_report(analyse, output_path):
#En simpel kontroll som ser till att variabeln analys är fullständig, annars stoppar programmet och du får då ett felmeddelande. 
#i framtida version skulle jag hellre vilja använda mig utav try: iställer för en if även om logiken egentligen är den samma i grunden.
    print("Kontrollerar om det finns data att skriva ner")
    
    if analyse.empty:
            print("Det finns inga resultat att skriva ner för tillfället..")
            return
    
    analyse.to_csv(output_path, index=False)
    print(f"Resultatet av fångsten har skrivits ner till {output_path}")

def valid_lines(line):
    #Kontrollerar om vissa linjer finns som till exempel malformed och lines dycker upp. Detta var en av testfallen jag skapade för att se till att tomma linjer eller just en malformed line inte dyker upp i csv databasen 
    line = line.strip()
    if not line:
        return False
    
    if line == "Mal":
        return False
    if line == "mal":
        return False
    if line == "Line":
        return False
    if line == "line":
        return False
    
    return True


def compare_files(output_path, total_lines, ip_count, data_folder):
    
    #dessa linjer som används genom pathlib är inte något jag har jobbat med innan och fick många fel tillbaka om saker inte var definerade rätt.
    suspicious_path = Path("week39-security-automation/data")
    security_compiled_path = Path(output_path)
    data_folder = Path(suspicious_path)
    
    Security_ioc = data_folder / "suspicious_ips.txt"
    Security_compiled = security_compiled_path
    
    #Force skapar en security report
    report_path = security_compiled_path.with_name(
        "security_report.txt"
    )
    
    #Litet test så att filerna kan hittas genom ny kod jag hittade från Pathlib, om inte den hittar filen får jag ett ordentligt status meddelande
    try: 
        report_data = pd.read_csv(
            Security_compiled,
            dtype=str,
            keep_default_na=False   
        )

    except FileNotFoundError as e:
        print(f"Hittar inte CSV filen {Security_compiled} som behövs för att kunna sammanställa en rapport")
        return

#Här börjar sammanställningen utan den skriftliga rapporten genom try som innan för att kunna lokalisera rätt filer, annars får jag en error
    try:
        with Security_ioc.open("r", encoding="utf-8") as file:
            suspicious_ips = {
                line.strip()
                for line in file
                if valid_lines(line)
            }  

    except FileNotFoundError as e:
        print(f"Hittar inte IOC filen {report_path} som behövs för att kunna sammanställa en rapport")
        suspicious_ips = set()
    
    #skapar report_data som en tom kolumn som matchar datan från kolumnen ip_address genom .isin funktionen
    report_data["IOC_match"] = (
        report_data["ip_address"]
        .isin(suspicious_ips)
    )
    
    #ip_count blir tillkallad som jag skapade innan med .value_count() på rad 226.
    #då ip_count var skapad innanför en funktion behövde jag tillkalla den genom att nämna den i return kommandot.
    #
    #om man skriver print("ip_count") som testades på rad 298 så kan man se i terminal loggen att dtype:int64
    #IP-Addresserna tvingade jag att bli konverterade till int tidigare i programmet för att kunna räkna dem på rätt sätt
    #
    #för att kunna återkalla "ip_address" kolumnen behöver jag se till att dessa blir återkallade som strängar.
    ip_count = (
        report_data["ip_address"]
        .astype(str)
        .str.strip()
    )
    #Ser till att tomma strings, pd.na samt tomma kolumn fält inte tas med
    #pd.na är automatiskt lagt till när det inte finns något att fylla ut, detta tas upp i analys
    #sammanställer och extraherar data genom variabler som report_data fångar på rad 387
    ip_count = (
        ip_count[
            ip_count.notna()
            & ip_count.ne("")
        ]
        .value_counts()
        .sort_index()
    )
    
    unique_ips = (
            report_data["ip_address"]
            .replace("", pd.NA)
            .nunique()
        )
    
    missing_ips = (
            report_data["ip_address"]
            .replace("", pd.NA)
            .isna()
            .sum()
            )
    
    matched_data = report_data[
        report_data["IOC_match"] == True
    ].copy()
    
    matched_data = matched_data.sort_values(
        by=["ip_address", "source_file"],
        ascending=True
    )
    
    number_of_lines = report_data["source_file"].nunique()
    
    report_lines = [
        "***************************************",
        "*       ITSX26 SECURITY REPORT        *",
        "***************************************\n",
        "",
        "* DATAKÄLLOR",
        "---------------------------------------",
        "",
        f"* CSV Fil: {Security_compiled}",
        f"* IOC Fil: {Security_ioc}",
        "",
        f"Antal filer som har extraherats: {number_of_lines}, antal har sedan extraherats till security_report.csv.\n",
        "INFO: Formatfel eller tomma linjer hoppas över på grund av Regex filtrering.",
        "",
        "* SAMMANSTÄLLNING",
        "---------------------------------------",
        "",
        f"Totalt extraherade rader från CSV: {len(report_data)}",
        f"Totalt antal rader har extraherats: {total_lines}",
        "",
        "",
        "IP Addresser och IOC-Matching: ",
        f"Antal unika observerade IP-Addresser: {unique_ips}",
        f"Antal unika misstänkta IP-Addresser från IOC Lista: {len(suspicious_ips)}",
        "",
        f"Antal IOC träffar som matchar {len(matched_data)}",
        f"Antal rader utan IP-Addresser: {missing_ips}",
        "",
        "* IP ADDRESSER, FREKVENS",
        "---------------------------------------",
        "",
        ip_count.to_string(header=False),
        "",
        "* IOC-TRÄFFAR",
        "---------------------------------------",
        "",
    
        ]
    
    #Skapar ytterligare matchad data mot specifika kolumner innan jag fortsäller rapporten
    if matched_data.empty:
        report_lines.append(f"Inga IP-Addresser matchade {Security_ioc}")
    else:
        for _, row in matched_data.iterrows():
            report_lines.append(
                f"IP: {row.get("ip_address", "")} | "
                f"Frekvens: {row.get("ip_frequency", "")} | "
                f"Händelse: {row.get("event", "")} | "
                f"Användare: {row.get("user", "")} | "
                f"Status: {row.get("status_code", "")} | "
                f"Källa: {row.get("source_file", "")}"
            )
    #.exten ser till att lägga till ytterligare information i en variabel genom att kalla på den igen.
    report_lines.extend([
        "",
        "* RÄKNADE MÖNSTER",
        "---------------------------------------",
    ])
    
    events = (
        report_data["event"]
        .astype(str)
        .str.strip()
        .str.casefold()
    )
    #skapar ints från hur många gånger den kan hitta specifika strängar i CSV dokumentet
    failed_login = events.eq("failed login").sum()
    denied_events = events.eq("deny").sum()
    
    #Sammanställning utav rapporten som påbörjades på rad 440
    report_lines.extend([
            "",
            f"Antal misslyckade inloggningar: {failed_login}",
            f"Antal DENY-händelser: {denied_events}",
            "",
            "* SLUTSATS & BEGRÄNSNINGAR",
            "---------------------------------------",
            (
                "IOC-träffar visar att observerade IP-addresser förekommer i IOC Listan\n"
                "Detta betyder ej att personen är misstänkt.\n"
                "Behöver bygga större case och evidens mot användare innan utredning startar."
            ),
            "",
            (
                "Att användare eller IP förekommer i IOC-listan bevisar inte att en attack har ägt rum.\n"
                "IP-addresser kan vara utdelade, förfalskade genom spoofing eller återanvända"
            ),
            "",
            (
                "Analysen har byggs upp genom data extrahering, textmatching och regex för att säkerställa faktuell data.\n"
                "Fält som inte följer med eller saknas helt följer inte förväntat format och kommer därför saknas i resultatet"
            ),
            "",
            (
                "Programmets storlek och mängden kod som jag har behövt att lära mig i denna uppgiften har varit tufft.\n"
                "Genom att fortsätta med planen med att skapa ett program som kunde sammanställa information för att sedan hantera detta genom\n"
                "att kalla på informationen som kolumnerna har sparat gör att det känns värt tiden och att det finns stor utvecklingspotential för skriptet.\n"
                ""
                "Det som jag har har begränsningar med är att jag inte har kunnat använda mig av olika compare, difference eller matchning av strängar genom .startswith("")\n"
                "Vilket har gjort att jag har behövt att använda mer tid på att hitta lösningar på pandas hemsida och stackoverflow samt flertal videos med hur man kan manipulera csv.\n"
                ""
                "Begränsningarna som jag kan se i detta skriptet även om det har en gedigen ryggrad är att den inte är särskilt flexibel innanför skriptet.\n"
                "Det är därför jag tog hjälp av Jupyter Notebook för at lära mig hur man kan manipulera csv filen utan att direkt ändra i filen.\n"
                "Via Jupyter kan man enkelt bläddra och sortera effektivt efter det man söker efter och finns extra information i CSV filen som jag inte har tagit med i min rapport.\n"
                "Vänligen ta en stund att titta på den om du får tid över"
            ),
    
#slutsats, osäkerhet och säkerhetsbetydelse kommer tas i analysen

    ])

    with report_path.open("w", encoding="utf-8") as file:        
        file.write("\n".join(report_lines))
    print(f"Rapporten har blivit skapat: {report_path}")

def main_frame():
    
    output_folder = Path("week39-security-automation/output")
    #skapar en output mapp om den inte finns
    output_folder.mkdir( 
        parents=True, 
        exist_ok=True
        ) 
    
    log_files, total_lines = load_indicators(folder)
    analyse, ip_count = analyse_logs(log_files)
    
    write_report(analyse, output_path)
    compare_files(
        output_path=output_path, 
        total_lines=total_lines, 
        ip_count=ip_count, 
        data_folder=folder
    )

main_frame()