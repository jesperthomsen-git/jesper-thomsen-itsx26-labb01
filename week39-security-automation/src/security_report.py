

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
#☐ Programmet kan köras från dokumenterad projektrot.
#☐ Indata öppnas för läsning och originalfilerna ändras inte.
#☐ Minst två datakällor behandlas.
#☐ Minst ett mönster räknas eller sammanställs.
#☐ IOC-listan läses och används för medlemskontroll.
#☐ Felaktiga eller ofullständiga rader hanteras explicit.
#☐ Rapporten skapas i output/ och kan återskapas med samma indata.
#☐ Resultatet sorteras eller presenteras på ett stabilt och begripligt sätt.


#                         SÄKERHETSRAMAR
#Använd kursens syntetiska dataset eller annan uttryckligen godkänd testdata.
#Publicera inte verkliga loggar, personuppgifter, tokens eller lösenord.
#Programmet ska inte kontakta externa API:er eller hotdatatjänster.
#Programmet ska inte skanna nät, försöka logga in eller genomföra brute force.
#Programmet ska inte automatiskt blockera adresser, ändra brandvägg eller påverka konton.
#Sanera skärmbilder och evidens innan publicering.

#                         Definition of Done
#☐ Rätt dataset och analyserade filer anges.
#☐ Programmet körs enligt README.
#☐ Originaldata är oförändrad.
#☐ Minst två datakällor analyseras.
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
import numpy as np


folder = Path("week39-security-automation/data")
output_path = "week39-security-automation/output/security_report.csv"

print("Kontrollerar om pandas biblioteket är installerat, vänligen vänta.")

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]) #skapar en exekveringskod som installerar pandas om det behövs för att kunna köra skriptet
    
def pandas_installed(pkg): #skapar en kontroll om det går att importera pandas eller inte
    try:
        __import__(pkg)
        return True
    except ImportError: 
        return False
    
if pandas_installed("pandas"):# om pandas finns så importerar vi den
    print("pandas existerar redan, fortsätter..\n")
    import pandas as pd
else:                         # annars kallar vi på install() funktionen som behöver subprocess och sys imports för att fungera.
    print("Installerar pandas, vänligen vänta ytterligare..")
    import subprocess
    import sys
    install("pandas")
    import pandas as pd
    print("pandas är nu installerat, fortsätter..\n")
    

pandas_installed("pandas")

def load_indicators(folder): #berättar vart filen finns  

    print("Kontrollerar filer i /data finns för uppgiften")
    folder = Path(folder)
    dataframes = []    
    
    log_files = [
        file for file in folder.rglob("*")
        if file.is_file()
        ]
    
    for file in log_files:
        try:
            with file.open("r", encoding="utf-8") as f:
                file_lines = 0
                
                for line in f:
                    line = line.strip()
                    
                    if line:
                        dataframes.append({
                            "log_entry": line,
                            "source_file": str(file)            
                            })
                        file_lines += 1
                print(f"Laddade filerna {file}: Hittade {file_lines} linjer av data")
                        
        except Exception as error:
            print(f"Kunde inte läsa {file}: {error}") 
        
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
        r"(?:event=|status=|method=)?"
        r"(?P<event>DENY|DROP|ALLOW|Failed|status|method)"
    )
    
    log_file = log_files.reset_index(drop=True).copy()
    
    #filtrerar hela min dataframe genom filter och inte bara log_entry som jag kommenterade ovan
    #filtered_logs = log_files.loc[combined_filter].copy() Denna kod behövs inte längre med är grunden för mitt kombinerade kommando för advancerad filtrering.
    
    print(
        f"Skriver ut antalet matchande rader som kompileras."
        f"Antalet matchningar: {combined_filter.sum()}"
    )
    
    if filtered_logs.empty:
        print("Inga rader matchade Regex.")
        return pd.DataFrame()
    
    
    csv_formatting = pd.concat( #sammanställer regex från strings som matchades innan tillsammans med andra strings som blir extraherade genom pd.concat
        [
            filtered_logs["log_entry"].str.extract(
                date_time,
                expand=True
            ),
            
            filtered_logs["log_entry"].str.extract(
                ip_pattern,
                expand=True
            ),
            
            filtered_logs["log_entry"].str.extract(
                users,
                expand=True
            ),
            
            filtered_logs["log_entry"].str.extract(
                events,
                expand=True
            )
        ],
        axis=1
    )
    
    csv_formatting["source_file"] = (
        filtered_logs["source_file"].to_numpy()
    )
    print(f"TEST SKER HÄR FÖR ATT TESTA REGEX"
            f"Datum check: ", date_match.sum(),
            "\n",
            f"IP CHECK: ", ip_match.sum(),
            "\n",
            f"USER MATCH: ", users_match.sum(),
            "\n",
            f"EVENT MATCH: ", events_match.sum(),
            "\n",
            f"ALLA MATCHNINGAR: ", combined_filter.sum()
        )
    return csv_formatting
    
def write_report(analyse, output_path):

    print("Kontrollerar om det finns data att skriva ner")
    
    if analyse.empty:
            print("Det finns inga resultat att skriva ner för tillfället..")
            return


    
    analyse.to_csv(output_path, index=False)
    print(f"Resultatet av fångsten har skrivits ner till {output_path}")


#def main_report(output_path):
    
    failed_count = 0
    error_list = []

    risknorm = 1
    risknight =  2
    risklogin = 3
    riskcountry = 5
    
    
    #print(f"Beräknar matchingar utifrån CSV dokument, vänligen vänta..")
    
    #with open(output_path, "w", encoding="utf-8", newline="") as user_logs:
        #user_read = csv.DictReader(user_logs)
       # data_list = list(user_read)

    #for line in data_list:
        #if "Failed login" in line:
            #failed_count += 1
    #print(f"Failed logins: {failed_count}")
    
    #df1 = pd.DataFrame([
        #columns=["source_file", "ip_address", "users", "login_status", "firewall_status"
        # ]])
    #pd.concat([df1])
    
    
    
    
    
            #print(line.strip())
        #fields = line.split()
        #source_fields = [f for f in fields if f.startswith("src=")] # f = variabel i arrayen som skapar splits efter "="

        #if not source_fields:
            #skipped += 1
            #continue
        #ip_address = source_fields[0].split("=", 1)[1]
        
    #print(f"IP address: {ip_address}")

   

    #susp_ips = {ip for ip in fields if line.strip()}

    #print ("suspicious ip: ", susp_ips)


    #acclogs = {line.strip() for line in access_file if line.strip()}
    #print ("Listing access logs: ", acclogs)


   # fw = {line.strip() for line in fw_file if line.strip()}
    #print ("Listing firewall settings: ", fw)
    
    #for data in data_list:
        #print(
            #data["suspicious_ips.txt"],
            #)


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
#main_report(output_path)
    

    
report = Path("week39-security-automation/output/security_report.txt")
report_lines = [
    ("***************************************"),
    ("*       ITSX26 SECURITY REPORT        *"),
    ("***************************************\n"),
    (""),
    (f"Data har tagits från {folder}\n"),
    (""),
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


