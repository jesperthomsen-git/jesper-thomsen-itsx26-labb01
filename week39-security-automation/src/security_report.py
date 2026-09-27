

#                         DITT UPPDRAG
# Läs minst två av kursens datakällor.
# Identifiera och räkna minst ett säkerhetsrelevant mönster.
# Extrahera och sammanställ käll-IP-adresser.
# Jämför observerade adresser mot suspicious_ips.txt.
# Hantera minst ett formatfel eller saknat fält begripligt.
# Skriv en reproducerbar rapport till output/security_report.txt.
# Analysera minst en observation med slutsats, osäkerhet och säkerhetsbetydelse.
# Dokumentera hur programmet körs, testas och avgränsas.


#                         FUNKTIONSKRAV
#[X] Programmet kan köras från dokumenterad projektrot.
#[X] Indata öppnas för läsning och originalfilerna ändras inte.
#[X] Minst två datakällor behandlas.
#☐ Minst ett mönster räknas eller sammanställs.
#☐ IOC-listan läses och används för medlemskontroll.
#☐ Felaktiga eller ofullständiga rader hanteras explicit.
#☐ Rapporten skapas i output/ och kan återskapas med samma indata.
#☐ Resultatet sorteras eller presenteras på ett stabilt och begripligt sätt.

#                         Definition of Done
#[X] Rätt dataset och analyserade filer anges.
#☐ Programmet körs enligt README.
#[X] Originaldata är oförändrad.
#[X] Minst två datakällor analyseras.
#☐ IOC-jämförelse och minst ett räknat mönster finns.
#☐ Felaktig data hanteras och redovisas.
#☐ Rapportfilen genereras i output/.
#☐ analysis.md innehåller observation, slutsats, osäkerhet, alternativ förklaring och säkerhetsbetydelse.
#☐ Minst tre testfall är dokumenterade.
#☐ AI-användning är redovisad och verifierad.
#☐ Repositoryt innehåller meningsfull commit-historik.
#☐ Canvas-inlämningen länkar direkt till rätt leverans.


import csv #importerar moduler för att skapa csv filer
import re #importerar requests, har denna fall i fall jag kommer använda den i framtiden
from pathlib import Path #använder mig av pathlib biblioteket för att hitta filer och mappar
import os #samma som ovan
import subprocess #För att installera pandas om det inte finns på systemet #beta
import sys #För att installera pandas om det inte finns på systemet #beta
import numpy as np #för att kunna hantera summeringar längre ner när det kommer till matchningar inom arrays


folder = Path("week39-security-automation/data")
output_path = "week39-security-automation/output/security_report.csv"



print("Kontrollerar om pandas biblioteket är installerat, vänligen vänta.")

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
    print(pd.__version__)
except ImportError as e:
    print(f"Pandas import gick inte egenom igen, error: {e}")
    print("Avslutar scriptet.")
    sys.exit()
    



def load_indicators(folder): #berättar vart filen finns  

    print("Kontrollerar filer i /data finns för uppgiften")
    folder = Path(folder)
    dataframes = []    
    total_lines = 0
    
    log_files = [
        file for file in folder.rglob("*")
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

        except Exception as error:
            print(f"Kunde inte läsa {file}: {error}") 
    
    print(
        f"Totalt {total_lines} blev inlästa"
    )
        
    return pd.DataFrame(dataframes)

def analyse_logs(log_files):
    print("Kontrollerar filer för analys..")
    
    if log_files.empty:
            print("Det finns inget att analysera")
            return pd.DataFrame()
    
    print("Kompilerar loggar till en security_report.CSV fil")
    
    #Skapat regex för att kunne filtrera för att skapa en grund för bättre matching av kolumner
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
    
    #filtrerar hela min dataframe genom filter och inte bara log_entry som jag kommenterade ovan
    #filtered_logs = log_files.loc[combined_filter].copy() Denna kod behövs inte längre med är grunden för mitt kombinerade kommando för advancerad filtrering.
    
    
    csv_formatting = pd.concat( #sammanställer regex från strings som matchades innan tillsammans med andra strings som blir extraherade genom pd.concat
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
    
    
    ip_count =  csv_formatting["ip_address"].value_counts(dropna=True)
    
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
    
    
    admin_count = csv_formatting["user"].eq("admin").sum()
    root_count = csv_formatting["user"].eq("root").sum()
    status_401_count = csv_formatting["status_code"].eq("401").sum()
    deny_count = csv_formatting["event"].eq("DENY").sum()
    failed_login_count = csv_formatting["event"].eq("Failed login").sum()
    #ip_counter = 

    
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
    
    csv_formatting.sort_values(
        "TOT_IOC",
        ascending=False,
        inplace=True
    ) 
    
    
    csv_formatting.reset_index( #skapar en reset från föregående kolumner så allt nollställs fall i fall.
        drop=True,
        inplace=True
    )   
    
    print("TESTAR IP", ip_count)
    
    print("SKAPAR FULLSTÄNDIG RAPPORT I CSV FILEN MED SUMMERING, VÄNLIGEN VÄNTA")
    
    summary_values = (
        csv_formatting["TOT_IOC"]
        .apply(lambda score: "Hög risk" if score >= 10 else "Medel risk")
    )
    
    
    csv_formatting.insert(
        loc=len(csv_formatting.columns),
        column="-----_SCORE_-----",
        value=summary_values
    )



    
    report = Path("week39-security-automation/output/security_report.txt")
    report_lines = [
    ("***************************************"),
    ("*       ITSX26 SECURITY REPORT        *"),
    ("***************************************\n"),
    (""),
    (f"Antal filer som har extraherats: {len(log_files)} och sedan extraherats till security_report.csv.\n"),
    (f"Totalt  linjer av data har extraherats"),
    ("INFO: Formatfel eller tomma linjer hoppas över på grund av Regex filtrering."),
    (""),
    (""),
    (""),
    ("-----IP Addresser och IOC-Matching-----"),
    (""),
    (""),
    (f"{ip_count}"),
    (""),
    (""),
    (""),
    (""),
    ("---------------MÖNSTER-----------------"),
    (""),
    (""),
    (""),
    ("**********  BEGRÄNSNINGAR  ************\n"),
    (""),
    (""),
    (""),

    ]
    with open(report, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    
    
    return csv_formatting
    
def write_report(analyse, output_path):

    print("Kontrollerar om det finns data att skriva ner")
    
    if analyse.empty:
            print("Det finns inga resultat att skriva ner för tillfället..")
            return
    
    
    
    analyse.to_csv(output_path, index=False)
    print(f"Resultatet av fångsten har skrivits ner till {output_path}")


def main_frame():
    
    output_folder = Path("week39-security-automation/output")
    output_folder.mkdir( #skapar en output mapp om den inte finns
        parents=True, 
        exist_ok=True
        ) 
    


    log_files = load_indicators(folder)
    analyse = analyse_logs(log_files)
    write_report(analyse, output_path)

    
main_frame()

    



