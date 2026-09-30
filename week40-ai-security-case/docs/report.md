3. Gemensamma säkerhets- och källkrav
Använd inte verkliga personuppgifter, autentiseringsuppgifter eller känsliga loggar.
Sanera skärmbilder och teknisk evidens.
Presentera inte antaganden som bekräftade fakta.
Använd officiell CIS-källa för kontrollnamn och version.
Externa påståenden ska ha relevanta och kontrollerbara källor.
AI-genererade påståenden ska verifieras innan de används.
Beskriv inte AI-hotet som mer avancerat än underlaget stödjer.

Definition of Done
CASE B
Valt case och tydlig avgränsning.
Fakta, hypoteser, antaganden och kunskapsluckor separerade.
Flera beroenden och 5-7 steg.
CIA, upptäckbarhet och residualrisk.
3-5 valda och minst två bortvalda CIS Controls.
Högst fem prioriterade åtgärder med beroenden.
Två målgruppsanpassade perspektiv samt engelsk sammanfattning.
Kritisk AI-granskning, källor och fördjupad muntlig förberedelse.


| OMRÅDE | KRITERIUM FÖR VG |
|---|---|
| Systematiskt säkerhetsmindset | Ofullständig och tvetydig information hanteras stringent; ny evidens kopplas till hur bedömningen kan ändras. |
| Beroenden | Teknik, information, identitet, människor och processer vägs samman. |
| CIA och risk | Sannolikhet, konsekvens, upptäckbarhet, befintliga kontroller och residualrisk analyseras med hög kvalitet. |
| CIS-val och bortval | Kontroller prioriteras och minst två alternativa kontroller väljs bort med tydlig motivering. |
| Alternativa förklaringar | Minst två rimliga förklaringar diskuteras och evidens för att skilja dem åt identifieras. |
| Verifiering | Verifieringen kan faktiskt visa om åtgärden fungerar och anger evidens, ansvar och uppföljning. |
| Åtgärdsprioritering | Åtgärder balanserar människa, process och teknik samt visar beroenden och genomförbarhet. |
| Dokumentation och spårbarhet | Underlaget håller särskilt hög kvalitet i riskdokumentation, källor, struktur och spårbarhet. |
| Målgruppsanpassning | Teknisk respektive verksamhetsnära kommunikation anpassas konsekvent till olika beslutsbehov. |
| AI och självständighet | Studenten identifierar brister i AI-stöd, verifierar centrala påståenden och motiverar egna korrigeringar. |
 --- VG-nivå --- | För VG ska samtliga G-krav vara uppfyllda. Därutöver ska arbetet visa särskilt hög kvalitet enligt kriterierna nedan. |

 | OMRÅDE | KRITERIUM FÖR G |
|---|---|
| Fakta och avgränsning | Givna fakta, antaganden och osäkerheter skiljs åt. |
| Tillgångar och händelsekedja | Relevanta tillgångar identifieras och händelsekedjan är begriplig. |
| CIA- och riskanalys | Konsekvenser är casespecifika och risk bedöms med en rimlig motivering. |
| CIS Controls | CIS 6, 8 och 14 kopplas till konkreta och relevanta åtgärder.|
| Verifiering | Studenten beskriver hur de viktigaste åtgärderna kan kontrolleras.|
| Teknisk förståelse | Minst en relevant teknisk koppling till tidigare kursmoment görs. |
| Dokumentation | Rapporten är strukturerad, källbelagd och skiljer evidens från slutsats. |
| Kommunikation | Svensk och engelsk sammanfattning är begriplig och målgruppsanpassad. |
| AI och självständighet | AI-användning redovisas och studenten kan förklara samt verifiera resultatet. |
| --- Bedömningsgräns --- | Case A är avgränsat för bedömning upp till G. Ett mer omfattande svar inom Case A ger inte automatiskt VG, eftersom Case A inte kräver den komplexitet och självständiga kontrollprioritering som behövs för VG-underlag. |


## Case B: Prompt injection i vårdrelaterat AI-system, sikte VG

### Scenario
En vårdorganisation använder en intern AI-assistent för att sammanfatta rutindokument och stödja personalens informationssökning. Assistenten får behandla dokument från flera interna källor. Efter att ett externt dokument laddats upp börjar assistenten lämna svar som innehåller information som inte tycks höra till det uppladdade dokumentet. Dokumentet innehåller dessutom dold eller svårupptäckt text som instruerar assistenten att ignorera tidigare instruktioner. Det är ännu inte fastställt om känsliga uppgifter faktiskt har exponerats. Organisationen saknar en fullständig bild av assistentens åtkomsträttigheter, loggning och dokumentflöden.


### Givna fakta
    • AI-assistenten sammanfattar dokument.
    • Dokument kommer från flera källor.
    • Ett externt dokument har laddats upp.
    • Dokumentet innehåller avvikande instruktioner.
    • Assistentens output har förändrats.
    • Behörigheter och loggning är inte fullständigt kartlagda.
    • Det finns ingen bekräftad dataexponering.
    • Orsakssambandet är ännu inte verifierat.

### Uppgift för Case B
    17. Separera fakta, hypoteser, antaganden och saknad information.
    18. Identifiera informations-, system-, identitets- och processberoenden.
    19. Beskriv en händelsekedja i fem till sju steg.
    20. Analysera CIA-konsekvenser och motivera den mest kritiska dimensionen.
    21. Bedöm sannolikhet, konsekvens, upptäckbarhet och residualrisk.
    22. Välj tre till fem kontroller från listan nedan. Motivera både val och minst två bortval.
    23. Föreslå högst fem prioriterade åtgärder och beskriv beroenden mellan dem.
    24. Ange verifieringsmetod, ansvarstyp och relevant evidens för huvudåtgärderna.
    25. Diskutera minst två alternativa förklaringar och vilken evidens som kan skilja dem åt.
    26. Kommunicera separat till teknisk respektive verksamhetsnära målgrupp.
    27. Redovisa och kritiskt granska AI-stöd och externa källor.

### Kontroller att välja mellan i Case B

| CONTROL | MÖJLIG RELEVANS |
|---|---|
| CIS 2: Inventory and Control of Software Assets | Överblick över AI-tjänst, integrationer och tillåtna programvaror. |
| CIS 3: Data Protection	| Klassning, åtkomst och skydd för information som behandlas av assistenten. |
| CIS 4: Secure Configuration of Enterprise Assets and Software | Säkra grundinställningar för tjänst och integrationer. |
| CIS 6: Access Control Management | Minsta privilegium och begränsning av vilken information assistenten kan nå. |
| CIS 8: Audit Log Management | Spårbarhet för dokument, åtkomst, output och händelser. |
| CIS 16: Application Software | Security	Säker design, test samt hantering av betrodd och obetrodd input. |
| CIS 17: Incident Response Management | Utredning, eskalering, evidens och hantering av möjlig dataexponering. |



## 1. Executive summary	- 150-250 ord på svenska: risk, högsta prioritet och central osäkerhet.



## 2. Fakta, hypoteser och scope -	Givet underlag, antaganden, kunskapsluckor och avgränsning.



## 3. Tillgångar och beroenden - Information, system, identiteter, processer och förtroende.



## 4. Händelsekedja och alternativa förklaringar - Fem till sju steg samt minst två alternativa förklaringar.



## 5. CIA- och fördjupad riskanalys	- Sannolikhet, konsekvens, upptäckbarhet, befintliga kontroller, osäkerhet och residualrisk.



## 6. CIS-mappning och bortval	- Tre till fem valda kontroller och minst två motiverade bortval.



## 7. Prioriterad förbättringsplan -Högst fem åtgärder, beroenden, ansvarstyp och verifiering.



## 8. Teknisk verifieringsplan	- Vilken evidens som behöver samlas och hur den tolkas.



## 9. Två målgrupper - Teknisk analys samt verksamhets-/ledningsanpassad rekommendation.


# 10 FYLL I ENGLISH SECURITY SUMMARY


## 11. AI- och källredovisning - Kritisk granskning, fel, korrigeringar och källor.



## 12. Slutsats	Proportionerlig - bedömning och residualrisk.





