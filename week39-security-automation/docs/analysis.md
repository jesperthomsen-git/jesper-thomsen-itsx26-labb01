
## Ditt uppgdrag
* Läs minst två av kursens datakällor.
* Identifiera och räkna minst ett säkerhetsrelevant mönster.
* Extrahera och sammanställ käll-IP-adresser.
* Jämför observerade adresser mot suspicious_ips.txt.
* Hantera minst ett formatfel eller saknat fält begripligt.
* Skriv en reproducerbar rapport till output/security_report.txt.
* Analysera minst en observation med slutsats, osäkerhet och säkerhetsbetydelse.
* Dokumentera hur programmet körs, testas och avgränsas.

| Rådata |	Vilka filer och loggrader användes? |
|---|---|
| Observation | Vad räknade eller matchade programmet konkret? |
| Slutsats | Vilken begränsad slutsats stöds av observationen? |
| Osäkerhet | Vad kan data och program inte fastställa? |
| Alternativ förklaring	| Vilka andra rimliga orsaker kan ge samma mönster? |
| Säkerhetsbetydelse | Varför är resultatet relevant för fortsatt analys eller prioritering? |

## Testning och verifiering
    • ☐ Visa minst tre dokumenterade testfall.
    • ☐ Minst ett test ska ha ett känt positivt utfall.
    • ☐ Minst ett test ska ge noll träffar.
    • ☐ Minst ett test ska innehålla ett formatfel eller saknat fält.
    • ☐ Jämför programmets resultat med ett manuellt räknat kontrollvärde.
    • ☐ Dokumentera eventuella hoppade rader i rapport eller analys.


## Bedömningspremiss
Bedömningen gäller säkerhetsautomation: problemförståelse, dataflöde, säker hantering, reproducerbarhet, evidens och analys. Pythonkodens elegans är stödjande, men ersätter inte korrekt säkerhetsresonemang.

| OMRÅDE | G | VG |
|---|---|---|
Automatiserat analysflöde | Programmet läser minst två filer, genomför relevant filtrering/räkning och skapar rapport. | Flödet är tydligt uppdelat, robust mot variationer och kombinerar flera datakällor utan att blanda ansvar. |
|Evidens och spårbarhet | Resultat kan kopplas till konkret indata och dokumenterad körning.	| Resultat är reproducerbara, sorterade och stöds av systematiska testfall och tydliga mellanresultat. |
|Säkerhetsanalys	| Minst en rimlig observation, slutsats och begränsning redovisas. | Flera observationer korreleras och vägs mot alternativa förklaringar, falska positiva och datakvalitet. |
|Defensiv databehandling | Saknad fil eller formatfel hanteras begripligt; originaldata ändras inte. | Felhantering och validering är systematisk, redovisar bortfall och förhindrar tysta felanalyser. |
|Rapportering | Rapporten är begriplig och innehåller centrala resultat och begränsning. | Rapporten prioriterar fynd, skiljer fakta från tolkning och förklarar säkerhetsbetydelse proportionerligt. |
|Dokumentation och förklaring | README och analysis.md visar hur lösningen körs och vad den gör. | Dokumentationen gör metod, designval, testning, begränsningar och förbättringsmöjligheter fullt spårbara. |
|AI och självständighet | AI-användning redovisas och studenten kan förklara lösningen.	| Studenten visar kritisk granskning av AI-förslag och kan motivera egna korrigeringar och designval. |

## AI-användning
AI-stöd är tillåtet för förklaringar, felsökning, kodgranskning och förslag. Du ansvarar för att förstå, testa och verifiera allt som lämnas in.
    • ☐ Ange vilket AI-verktyg som användes.<p>
    • ☐ Beskriv vad AI hjälpte till med.<p>
    • ☐ Beskriv hur du testade och verifierade förslagen.<p>
    • ☐ Markera eller förklara större AI-genererade koddelar.<p>
    • ☐ Var beredd att muntligt förklara programmets dataflöde och analyslogik.<p>

## Sammantagen betygsnivå
| BETYG | SAMMANTAGEN NIVÅ |
|---|---|
| G	|Samtliga obligatoriska leveranser och säkerhetsramar är uppfyllda. Analysen fungerar, är begriplig och gör proportionerliga påståenden utifrån evidensen. |
| VG | G är uppfyllt och arbetet visar genomgående fördjupad korrelation, robust databehandling, reproducerbar verifiering och analytisk mognad. Enstaka avancerade koddetaljer räcker inte i sig. |
| Ej godkänt |Centrala leveranser saknas, programmet kan inte verifieras, säkerhetsramar bryts eller analysen gör ogrundade påståenden som inte kan kopplas till evidens. |




## 01. Metod
--------------------------------------------

## 02. observation
--------------------------------------------
Under min research hittade jag att pd.concat kan samla all information genom att kombinera information från loggfilerna till array som jag har döpt till dataframes, denna samlar då all information tills jag kallar på den igenom pd.concat i min "write_report()" funktion via "pd.concat(dataframes, ignore_index=True)"
    pd.concat(dataframes, ignore_index=True)


problem med filters

format = (
        r"(?P<date>\d{4}-\d{2}-\d{2})\s+" #YYYY-MM-DD
        r"T"
        r"(?P<time>\d{2}:\d{2}:\d{2}Z)\s+"
        r"src=(?P<ip_adress>\S+)\s+"
        r"user=(?P<user>\S+)\s+"
        r"(?P<event>DENY|DROP|ALLOW|FAILED|status|method)"
    )
    
    csv_formatting = log_files["log_entry"].str.extract( #Testar pandas.Series.str.extract kommando som jag hittade på pandas hemsida
        format,
        expand=True
        ) 
    
    csv_formatting["source_file"] = log_files["source_file"].values
    return csv_formatting 


Try ger bättre exception stoppar och errors än min föregående kod. uppdaterad kod är:
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


Genom att skapa en filtrerings funktion var något som inte direkt fungerade i min filtrering. jag förstod därefter att jag tar bort all annan information som inte passar innanför dessa ramar och något jag kommer ta bort från min kod men är lärorikt att ta med sig i framtiden.

    log_entry = log_files["log_entry"] # här skapar jag en series som finns med i pandas som samlar all data från förr till ett 1 dimensionellt array som samlar all data tills jag kallar på dem längre ner.

    #skapar nu en mini funktion som läser av om någon linje får träff på mitt regex filter ovan
    date_match = log_entry.str.contains(
        date_time,
        regex=True,
        na=False  
    )
    ip_match = log_entry.str.contains(
        ip_pattern,
        regex=True,
        na=False  
    )
    users_match = log_entry.str.contains(
        users,
        regex=True,
        na=False  
    )
    events_match = log_entry.str.contains(
        events,
        regex=True,
        na=False  
    )
    
    combined_filter = ( #kombinerar dessa för att sedan kunna använda mig av pd.concat igen för att samla allt i min dataframe []
        date_match 
        & ip_match 
        & users_match 
        & events_match
    )

## 03. Oäkerhet
--------------------------------------------

## 04. Säkerhetsbetydelse
--------------------------------------------

## 05. Alternativ förklaring
--------------------------------------------

## 03. Slutsats
--------------------------------------------
