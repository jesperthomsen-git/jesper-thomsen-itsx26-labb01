
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
    • ☐ Ange vilket AI-verktyg som användes.
    • ☐ Beskriv vad AI hjälpte till med.
    • ☐ Beskriv hur du testade och verifierade förslagen.
    • ☐ Markera eller förklara större AI-genererade koddelar.
    • ☐ Var beredd att muntligt förklara programmets dataflöde och analyslogik.

## Sammantagen betygsnivå
| BETYG | SAMMANTAGEN NIVÅ |
| G	|Samtliga obligatoriska leveranser och säkerhetsramar är uppfyllda. Analysen fungerar, är begriplig och gör proportionerliga påståenden utifrån evidensen. |
| VG | G är uppfyllt och arbetet visar genomgående fördjupad korrelation, robust databehandling, reproducerbar verifiering och analytisk mognad. Enstaka avancerade koddetaljer räcker inte i sig. |
| Ej godkänt |Centrala leveranser saknas, programmet kan inte verifieras, säkerhetsramar bryts eller analysen gör ogrundade påståenden som inte kan kopplas till evidens. |




## 01. Metod
--------------------------------------------

## 02. observation
--------------------------------------------

## 03. Oäkerhet
--------------------------------------------

## 04. Säkerhetsbetydelse
--------------------------------------------

## 05. Alternativ förklaring
--------------------------------------------

## 03. Slutsats
--------------------------------------------
