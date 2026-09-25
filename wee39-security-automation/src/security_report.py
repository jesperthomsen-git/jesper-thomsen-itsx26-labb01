

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



output_path = "wee39-security-automation/output/security_report.csv"

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
    log_files = list(folder.rglob("*.log"))
    
    if not log_files:
        print(f"Hittar inte filer i {folder}")
        return pd.DataFrame()
        
    else:
        print("Hittade filerna: ")
        for file in log_files:
            print(file)
        
    dataframes = []
    
    for file in log_files:
        try:
            df = pd.read_csv(
                file,
                engine='python',
                header=None,
                names=["log_entry"],
                dtype=str 
                )

            df["source_file"] = file.name
            dataframes.append(df)
        
        except Exception as error:
            print(f"Kunde inte läsa {file}: {error}")
    
    if not dataframes:
        return pd.DataFrame()
    
    return pd.concat(dataframes, ignore_index=True)

def analyse_logs(log_files):
    print("Kontrollerar filer för analys..")
    
    if log_files.empty:
            print("Det finns inget att analysera")
            return log_files
    
    
    print("Kompilerar loggar till en security_report.CSV fil")
    return log_files


def write_report(analyse, output_path):

    print("Kontrollerar om det finns data att skriva ner")
    
    if analyse.empty:
            print("Det finns inga resultat att skriva ner för tillfället..")
            return

    analyse.to_csv(output_path, index=False)

    print(f"Resultatet av fångsten har skrivits ner till {output_path}")


def main_frame():
    
    folder = Path("wee39-security-automation/data")
    output_folder = Path("wee39-security-automation/output")
    output_folder.mkdir( #skapar en output mapp om den inte finns
        parents=True, 
        exist_ok=True
        ) 
    


    log_files = load_indicators(folder)
    analyse = analyse_logs(log_files)
    write_report(analyse, output_path)
    
    

def main_report(output_path):
    
    print(f"Beräknar matchingar utifrån CSV dokument, vänligen vänta..")
    
    with open(output_path, encoding="utf-8", newline="") as user_logs:
        user_read = csv.DictReader(user_logs)
        user_list = list(user_read)

    for user in user_list:
        print(
            user["log_entry"]
        )
            
            
        
    
    

main_frame()
main_report(output_path)
    
    





