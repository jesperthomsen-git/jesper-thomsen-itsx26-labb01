
# 01. ANALYS
--------------------------------------------
| DEL | FRÅGA ATT BESVARA |
|---|---|
| Rådata |	Vilka filer och loggrader användes? |
| Observation | Vad räknade eller matchade programmet konkret? |
| Slutsats | Vilken begränsad slutsats stöds av observationen? |
| Osäkerhet | Vad kan data och program inte fastställa? |
| Alternativ förklaring	| Vilka andra rimliga orsaker kan ge samma mönster? |
| Säkerhetsbetydelse | Varför är resultatet relevant för fortsatt analys eller prioritering? |


### 01.1 Rådata: Vilka filer och loggrader användes? 
--------------------------------------------

Rådatan som analyseras är "Dataset B: Advanced" som innehåller en access.log, aut.log och firewall.log. Genom dessa filer har jag lyckats att skapa en grund där programmet läser samtliga loggrader från filer som blir placerade i ./data.  Programmet har blivit framtidssäkrad genom en filtrering utav Regex kod som läser in och filtrerar inkommande data och sedan via denna process placerar rätt data i rätt kolumn. 

### 01.2 Observation: Vad räknade eller matchade programmet konkret?
--------------------------------------------

Programmet är skapat för att kunna analysera indatan på ett effektivt sätt genom databashantering. Datan blir därefter matchad mot IOC filen för att kunna hitta mönster gentemot användare, IP-addresser och utvalda events som misslyckade inloggnings försök.

Programmet räknar också frekvensen utav unika IP-addresser och sedan räknar ut hår många gånger den unika addressen uppstår. Efter uträkning skapar den en lättviktig analys på om man behöver undersöka genom hög risk eller resterande bli medel risk där man inte behöver skapa någon action för tillfället.

### 01.3 Slutsats: Vilken begränsad slutsats stöds av observationen?
--------------------------------------------

Observationen skapar en helhetsbild av loggarna som datan har samlats från, dessa blir då extraherade och blir rapporterade i [security_report.txt](../output/security_report.txt). 

Del av resultatet som skrivs ut för att se till att man inte skapar misstankar mot användare eller IP-addresser bara för att den dyker upp oftare än vanligt och oftast har en naturlig förklaring till varför personen har agerat som den har gjort under tiden själva fångsten ägde rum.

En snutt som jag också nämner i rapporten som är här nedan:

    "IOC-träffar visar att observerade IP-addresser förekommer i IOC Listan"
    "Detta betyder ej att personen är misstänkt."
    "Behöver bygga större case och evidens mot användare innan utredning startar."

    "Att användare eller IP förekommer i IOC-listan bevisar inte att en attack har ägt rum."
    "IP-addresser kan vara utdelade, förfalskade genom spoofing eller återanvända"

    "Analysen har byggs upp genom data extrahering, textmatching och regex för att säkerställa faktuell data."
    "Fält som inte följer med eller saknas helt följer inte förväntat format och kommer därför saknas i resultatet"

Då det är viktigt att poängtera att datan inte är fastslådd och att detta bara stöde indikator listan men att inget är färdigställt bara för att datan som sammanställ skrivs in i en rapport.

### 01.4 Osäkerhet: Vad kan data och program inte fastställa?
--------------------------------------------

Även om observationen skapar en helhetsbild av fångsten så är den inte avgörande data. Detta i sig kan skapa osäkerhet genom att programmet kan oundvikligt indikera att en person är misstänkt för en attack vilket jag såg till att detta blev skrivet i rapporten som påminnelse. 

Programmet i fråga kan inte återskapa, fånga en specifik incident eller en attack som till exempel Wireshark kan, detta program analyserar data från fångst genom tredje parts applikationer som skapar loggarna 

### 01.5 Alternativ förklaring: Vilka andra rimliga orsaker kan ge samma mönster? 
--------------------------------------------

Om man tänker innanför rimliga ramar har jag nämnt att det nödvändigtvis inte behöver vara samma person men att IP-addressen kanske har återanvänds. Personen har helt enkelt glömt sitt lösenord och testar olika lösenord som användaren kan tänkas ha använt vid registrering. När det kommer till att bli nekad genom en firewall kan det absolut skapa en viss misstanke då till exempel 401 som programmet samlar vid kompilering kan skapa indikationer på att någon som inte har rättigheter försöker att gära vissa moment som behöver elevering. Detta i sig behöver inte vara en indikation på angrepp men kan helt enkelt vara att användaren försöker gå in på en hemsida som brandväggen har manuellt blivit tillsagd att man inte ska få åtkomst till. 

### 01.6 Säkerhetsbetydelse: Varför är resultatet relevant för fortsatt analys eller prioritering?
--------------------------------------------

Datan som analyseras visar och sammanställer rå data. Datan i sig kan vara relevant vid specifik analys om fångsten var bred eller om man behöver hitta mönster som mänskliga ögat möjligtvis kan missa. Genom att skapa en nyare version av programmet med möjligtvis en GUI så kan man lättare anpassa vad man söker efter vilket skapar användarvänlighet och flexibilitet.



## 02. Testning och verifiering


### 02.1 Tre dokumenterade testfall:
--------------------------------------------

Första testfallet var ganska rak på sak när det kommer till malformed line som fångades upp i uppgiften. När kag körde programmet så såg jag direkt att denna lästes in i databasen. Jag gav inte det så mycket eftertanke tils jag började struktuera rapporten och märkte att det kan vara ganska enkelt att få ut den datan oavsikligt. Genom att lägga till extra åtgärder i koden som ser till att om den hittar specifika delar av strängen, i detta fall Mal/mal & Line/line så kommer jag få ett felmeddelande längre ner där den hittade denna strängen och avsluta återkallningen till rapporten.

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

Personligen efter att ha jobbat mycket med if funktioner så har jag börjat att tycka om att använda try: hellre för specifika fel och statuskoder som kan vara svåra att fånga upp med en enkel if även om man kan göra samma sak.

### 02.2 Identifiera ip mot IOC
--------------------------------------------

Då jag jobbar med kolumner kan jag skapa bättre struktur genom större projekt och filer och skapar en säkrare grund än att direkt räkna från ett text dokument.
Momentet att försöka matcha IP addresserna mot IOC var nog en av momenten jag hade svårast att tackla då jag behövde använda mig av olika metoder som i slutändan inte fungerade som tänkt.


#### 02.2.a) Normalfall
--------------------------------------------

Genom att kunna kalla på "ip_address" kolumnen i databanken genom att skapa en tom kolumn utan data så kan man använda report_data som en tunnel mellan databasen och rapporten.

    #sample kod tagen från rad 387
    report_data["IOC_match"] = (
        report_data["ip_address"]
        .isin(suspicious_ips)
    )

    #sample kod tagen från rad 429 - 436.
    matched_data = report_data[
        report_data["IOC_match"] == True
    ].copy()
    
    matched_data = matched_data.sort_values(
        by=["ip_address", "source_file"],
        ascending=True
    )

Denna inspiration hittades på Pandas hemsida under pandas.dataframe.isin() [^1] 


#### 02.2.b) Felfall
--------------------------------------------

En sample kod som inte fungerade på grund av att summeringen genom Diff import fungerade inte som jag hade tänkt. Detta var kommenterat som en legacy import i koden. Då arrays är en väg att kunna skapa counters för var IP träff så gör den det för alla träffar av IP vilket inte är vad jag är ute efter. Om legacy koden kördes så fick man över 20 träffar i while loopen istället för att ge en summa som .sum() eller value_counter() kan enklare klara av:

    with open(log_file, "r", encoding="utf-8") as f1:
        
            file1_lines = [
                    line for line in f1
                    if line
                    ]


    with open(Security_ioc, "r", encoding="utf-8") as f2:
    
        file2_lines = [
                line for line in f2
                if line
                ]
        
    print(f"Skapar en fullständig rapport genom att matcha {f2} mot {f1}")
    
    susp_ips = {line.strip() for line in file1_lines if line.strip()}
    diff = list(differ.compare(file1_lines, file2_lines))
    
    print(f"Matchningar som kommer att jämföras mot: {susp_ips} som finns noterat i {f1}")
    
    
    with open(report, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

Tanken var att matcha logfilerna mot ioc dokumentet först för att kunna skapa snabba matchningar men då jag använder en databas behövdes andra åtgärder där jag behövde kalla ut datan genom kolumner.

(Notering: while loopen var inte medtagen av misstag och kan inte hitta koden som ändrades. Sample koden ovan var huvud koden för att kunna skapa matching mellan fil 1 och fil 2 genom diff variabeln.)


Hitta mönster genom matching av IOC och IP addresser




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

Försökte att skapa regler för när panda hittade strängarna som börjar på t.ex "admin" detta var något som inte helt fungerade och som jag förstår skriver över alla andra poäng som jag ville lägga tillsammans och bara tar den senaste och skriver ut
df["suspicious_activity"] = np.where(df["user"]=="admin", 0, 2)
df["suspicious_activity"] = np.where(df["user"]=="root", 0, 3)
df["suspicious_activity"] = np.where(df["status_code"]=="401", 0, 1)
df["suspicious_activity"] = np.where(df["event"]=="DENY", 0, 1) 
df["suspicious_activity"] = np.where(df["event"]=="Failed Login", 0, 1)

genom att använda mig av pd.loc så kan jag lättare lokalisera vad jag vill ha som "admin" genom 
    df.loc[df["user"].eq("admin"), "suspcious_activity"] += 1
    df är min dataframe
    .loc är locate
    ["user"] är min kolumn
    .eq är equals, samma som om jag skulle skriva =
    Om .loc hittar "admin" i strängen så lägger den till en counter till suspicious activity kolumnen

Detta fungerar på samma logic som övningen vi gjorde i måndagen den 21:a
    failed_count = 0
    if "Failed login" in line:
            failed_count += 1

Då jag jobbar med kolumner kan jag skapa bättre struktur genom större projekt och filer och skapar en säkrare grund än att direkt räkna från ett text dokument.
Fungerade inte på grund av att summeringen genom Diff import fungerade inte som jag hade tänkt, då arrays är en väg att kunna skapa counters för var IP träff så gör den det för alla träffar av IP vilket inte är vad jag är ute efter.
    with open(log_file, "r", encoding="utf-8") as f1:
        
            file1_lines = [
                    line for line in f1
                    if line
                    ]


    with open(output_path, "r", encoding="utf-8") as f2:
    
        file2_lines = [
                line for line in f2
                if line
                ]
        
    print(f"Skapar en fullständig rapport genom att matcha {f2} mot {f1}")
    
    susp_ips = {line.strip() for line in file1_lines if line.strip()}
    diff = list(differ.compare(file1_lines, file2_lines))
    
    print(f"Matchningar som kommer att jämföras mot: {susp_ips} som finns noterat i {f1}")
    
    
    with open(report, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))





osäkerhet och säkerhetsbetydelse.


## 03. Oäkerhet
--------------------------------------------

## 04. Säkerhetsbetydelse
--------------------------------------------

## 05. Alternativ förklaring
--------------------------------------------

## 03. Slutsats
--------------------------------------------
 genom pandas men kan också tvingas in i databaser genom pd.NA för att inte skapa data som kan vara felaktig.Denna har då filtrerats bort

 Även om malformed line visas tydligt i Jupyter Notebook så är detta inget som visas eller kan extraheras till text rapporten.
 #slutsats, osäkerhet och säkerhetsbetydelse.

--------------------------------------------
 ## EXTERNA LÄNKAR

[^1] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin