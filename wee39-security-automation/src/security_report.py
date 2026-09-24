

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

print("Kontrollerar om pandas biblioteket är installerat, vänligen vänta.")

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    
def pandas_installed(pkg):
    try:
        __import__(pkg)
        return True
    except ImportError: 
        return False
    
if pandas_installed("pandas"):
    print("pandas existerar redan, fortsätter..\n")
else:
    print("Installerar pandas, vänligen vänta ytterligare..")
    import subprocess
    import sys
    install("pandas")
    import pandas as pd
    print("pandas är nu installerat, fortsätter..\n")
    

pandas_installed("pandas")













