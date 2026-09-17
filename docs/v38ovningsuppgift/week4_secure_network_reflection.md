## WEEK 38 WIRESHARK

### FÖLJ -> FÅNGA -> FILTRERA -> ANALYSERA -> FÖRKLARA
### Du ska kunna:
* Följa ett paket
* Visa vad som syns i trafiken
* Förklara säkerhetsbetydelsen utan att överdriva
* Bevisa, vara konkret utan gissningar
* Anteckna osäkerheter

----------------------------------

## Rapport och evidens av Wireshark

|Relevat protokoll | vad syns (var konkret) | vad stöder observationen | vad kan inte avgöras |
|---|---|---|---|---|---|
|tex. HTTPS | vad syns (var konkret) | vad stöder observationen | vad kan inte avgöras |

----------------------------------
## Fördjupning av protokoll

Identifiera flödet och ändpunkterna
Ordna relevanta paket i tidsföljd
Jämför protokoll, synlighet och resultat
Avgränsa vad fångsten kan visa
Vad skyddas av krypteringen?
Hur syns brandvägg och hardening indirekt?
Hur kopplas saniterad evidens till CIA?

* Konfidentialitet: Vad exponeras eller skyddas?
* Integritet: Vad kan ändras eller verifieras?
* Tillgänglighet: Når trafiken avsedd tjänst?

----------------------------------

## Evidenskvalitet

Var samlades trafiken in?
Vilka filter eller avgränsningar användes?
Vad saknas/saknades vid fångsten?
Vilken osäkerhet ska anges? (förklara, var konkret)

----------------------------------


## Fördjupa flöden

Kan verifiera och jämföra vissa protokoller mot varandra för att se skillnad:

DNS <-> ICMP
HTTP <-> TLS/HTTPS
Lyckad anslutning <-> Uteblivet svar
egen pcap med reservspår genom trafigeneratorn

----------------------------------

## Brandvägg info

* SS bevisar lokalt lyssande tjänster men inte ensam extern nåbarhet
* Brandväggsregler beskriver avsedd tillåtelse eller blockering
* PCAP visar observerad nätverkstrafik vid fångspunkt

----------------------------------

## SÄKERHETSRAMAR

### DU FÅR INTE

* Fånga andras trafik
* Portskanna eller använda brute force
* Publicera pcap
* Testa mål utanför godkänd miljö

### GÖR ISTÄLLET

* Använd egen miljö eller reservspår som trafikgenerator eller pcap filer som blev uppladdade "week38_packet_journey_basic.pcap" och "week38_packet_journey_advanced.pcap"
* Begränsa tid, interface och mål
* Sanera adresser och andra identifiers
* fråga läraren vid osäkerhet via Slack

----------------------------------
