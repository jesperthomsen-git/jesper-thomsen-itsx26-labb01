import csv
import re
from pathlib import Path
import os
import subprocess
import sys

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
    
def load_indicators(folder): #berättar vart filen finns  

    print("Kontrollerar filer i /data finns för uppgiften")
    folder = Path(folder)
    files = list(folder.rglob("*.log"))

    if not files:
        print("Hittar inte filer i {folder}")
        return pd.DataFrame()
        
    else:
        print("Hittade filerna: ")
        for file in files:
            print(file)
        
    dataframe = []
    
    for file in files:
        try:
            df = pd.read_csv(
                file,
                sep='\s+',
                engine='python',
                header=None, 
                )

            df["source_file"] = file.name
            dataframes.append(df)
        
        except Exception as error:
            print(f"Kunde inte läsa {file}: {error}")
            
        
def analyse_logs(df):
    print("Kontrollerar filer för analys..")
    
    if df.empty:
            print("Det finns inget att analysera")
            return df
    
    
    print("Kompilerar loggar till en security_report.CSV fil")
    return df
        

def write_report(results, output_path):

    print("Kontrollerar om det finns data att skriva ner")
    if results.empty:
            print("Det finns inga resultat att skriva ner för tillfället..")
            return
    results.to_csv(output_path, index=False)
    print(f"Resultatet av fångsten har skrivits ner till {output_path}")

def main_frame():
    folder = Path('wee39-security-automation/data')
    output_path = "wee39-security-automation/reports/security_report.csv"
    logs = load_indicators(folder)
    analyse = analyse_logs(df)
    write = write_report(results, output_path)
        
        
pandas_installed("pandas")

main_frame()

