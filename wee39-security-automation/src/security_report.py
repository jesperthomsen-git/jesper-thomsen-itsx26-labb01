

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



import csv
#import pandas as pd
import re

search = "a"
risknorm = 1
risknight =  2
risklogin = 3
riskcountry = 5

with open("data/userlogs.csv", encoding="utf-8", newline="") as userlogs:
    user_read = csv.DictReader(userlogs)
    user_list = list(user_read)

    print("Skriver ut CSV dokument")

    for users in user_list:
        print(
            users["date"],
            users["last_name"],
            users["first_name"],
            users["email"],
            users["country"],
            users["ip_address"]
        )
        


import pathlib
import os

suspicious_ip = "data/suspicious_ips.txt"

def load_indicators(path): #berättar vart filen finns  
    path = [ 

        "data/auth.log"
        "data/access.log"
        "data/firewall.log"
    ]
    
def analyze_logs(path, indicators):

        for f in :
            if f in line:
                sus_ip = {line.strip() for line in f if line.strip()}
        print("fel")

def write_report(results, path):
    print("testar om denna funktionen funkar")
    report_lines = [
        "ITSX26 SECURITY REPORT"
        f""
        f""
        f""
        f""
        f"",
        f"LIMITATION",

    ]
    
    f.write("\n".join(report_lines))

def main():
    load_indicators(suspicious_ip)
    analyze_logs()
    write_report()

print("Kontrollerar om filer existerar\n")
main()

skipped = 0
failed_count = 0

with open("data/auth.log", encoding="utf-8") as log_file: #berättar vart filen finns
    for line in log_file:
        if "Failed login" in line:
            failed_count += 1
            print(line.strip())
        fields = line.split()
        source_fields = [f for f in fields if f.startswith("src=")] # f = variabel i arrayen som skapar splits efter "="

        if not source_fields:
            skipped += 1
            continue
        ip_address = source_fields[0].split("=", 1)[1]
    print(f"IP address: {ip_address}")

    print(f"Failed logins: {failed_count}")

with open("data/suspicious_ips.txt", encoding="utf-8") as ip_file: #berättar vart filen finns
    susp_ips = {line.strip() for line in ip_file if line.strip()}
    print ("suspicious ip: ", susp_ips)

   # for line in ip_file:
    #    linesplit = line.split()
    #    array = [f for f in linesplit if f.startswith("")]
    #    susip = array[0].split("=", 1)[1]
    #print(f"suspicious ip: {susip}")

with open("data/access.log", encoding="utf-8") as access_file: #berättar vart filen finns
    acclogs = {line.strip() for line in access_file if line.strip()}
    print ("Listing access logs: ", acclogs)

with open("data/firewall.log", encoding="utf-8") as fw_file: #berättar vart filen finns
    fw = {line.strip() for line in fw_file if line.strip()}
    print ("Listing firewall settings: ", fw)