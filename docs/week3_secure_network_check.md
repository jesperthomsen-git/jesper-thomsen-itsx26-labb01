## Repo struktur

Reflektioner, CIA-analys & manuella observationer ligger i week3_secure_network_check.md <p>
│<p>
├── docs<p>
│ └── week3_secure_network_check.md<p>
├── evidence<p>
│ └── README.md<p>
│<p>
├── scripts<p>
│ └── secure_network_check.sh<p>
│<p>
├── README.md<p>
└── ...<p>
strukturen tagen är från Canvas: Oracle Cloud VM, Linux, hardening, recovery och cleanup 

-------------------------------------------------------------

## Miljöbeskrivning

Miljö: Oracle Cloud
Ubuntu 26.04
Ens3

### Adresser: 
* Lokal adress är localhost 127.0.0.1 och är på ens sercer i Oracle cloud eller lokalt på ens dator
* Privat adress är ett nätverk som man kan koppla sig till som inte går ut på internet som heter LAN
* Publik adress är din IP adress som blir konverterad till publik så webbplatser vet vem det är. 

### Begränsningar:
* Begränsningar som kan följa med Oracle cloud är att man kan låsa sig själv ute om man gör något fel medans man har sudo rättigheter
* Kan möjligtvis kosta pengar om man ändrar i inställningar
* Kan ha en viss fördröjning
* Har öppna portar 80 & 443 som vem som helst kan komma in genom
* Annorlunda gränsnitt och funktioner från andra distron

-------------------------------------------------------------

## Reflektioner för projektet

### Manuella observationer

| Kontrollerade | Kontroll | Förklarande |
|---|---|---|
| Interface och IP | hostname -i | Hostname ger en localhost adressen för OCI |
| DNS | getent hosts | Visar entries på namnet hosts och visar localhost, loopback och subnätet 127.0.1.1|
| Portar | ss -tuln | Visar vilka portar som är öppna och stängda för tillfället, kan hjälpa med att minska området för attacker |
| Processer | systemctl | Används för att få insikt från systemd men tillåter dig att kontrollera vissa delar så som att slå på ssh som exempel |
| Routing | ip route | Visar prompter och steg för att komma ut på internet |

-------------------------------------------------------------

### CIA-analys

#### Konfidentialitet:
Vilka uppgifter i nätverksutdata kan vara känsliga, och hur sanerar du dem?

När det kom till utdatan så var jag mån om att ha hemsidan utanför skriptet, detta var för att både skapa en enklare struktur men också som ett säkerhetstänk för att inte hårdkoda in en hemsida i programmet.

En annan del var när jag använde grep för att få information om min port 8080 var öppen eller ej samt vilka portar som var under listen. Såg till att datan sparades som word count så att känslig information om tjänster eller processer som är aktiva inte blir exponerade.

En extra del i konfidentialitet var att skapa en hardening grund redan från början genom chmod 700 direkt efter skapandet av filen. Då all information sparas i en logg lade jag också till en funktion som räknar hur många loggar som sparas i filen README.md och frågar om man vill radera filen. Om man svarar ja så skapar den en ny loggfil, skapar rättigheterna och börjar logga i den direkt efter.


#### Intigritet:
Hur hjälper loggar, versionshistorik, tydliga statusar och kontroller till att skapa tillit till resultatet?

Att man skapar en logg för att se vart som skriptet det går fel eller vart det går rätt till kan ha stor betydelse på hur integriteten förblir fortsatt i skriptet. Versions historik samt tydliga statusar tillsammans med kontroller så som [OK], [INFO] [WARN] eller [FAIL] kan ha stor betydelse i översikten och ger en tydlig bild vart det kan gå fel om man vill troubleshoota.


#### Tillgänglighet
Tillgänglighet: Hur visar DNS, route, tjänst och port om en funktion är tillgänglig?

När man försöker gå in på en hemsida som inte är tillgänglig så letar ens dator efter en specik IP adress som konverteras över till ett domän namn men kommer aldrig fram. Detta gör att paketet kommer tillbaka olevererat. Genom route kan man felsöka om det är på ens egna sida eller om hemsidan är nere genom att kolla på om till exempel ens portar eller tjänster är nere som till exempel "ss- tuln", "ip addr" och "hostname -i".
 
    ss -tuln
    ip addr  
    hostname -i

När det är en tjänst är inaktiv så brukar den oftast stå som att den lyssnar, det betyder att den håller utkik på inkommande kommandon från en port, som till exempel port 8080. När porten är stängd så kommer tjänsten inte att visas i listan under "ss -tuln". När man då kallar på en funktion som att starta sin egna lokala HTTP server så kan man enkelt se att detta port öppnas och att en tjänst blir tilldelar för den porten, som en person som håller dörren öppen för den som har tillåtelse till det. 

Med detta kan man se till att olike processer och tjänster inte har sina dörrar öppna för tillgång hela tiden men att man stänger dessa för att kunna minska ytan för attacker. Genom tillgänglighet och en säker approach så kan man se till att personer som ska ha tillgång till tjänster eller portar har det medans andra som till exempel saknar nycklar eller tillgång till den server på det lokala nätverket inte får tillgång.

-------------------------------------------------------------

### Avvägning
Ge ett exempel där en säkerhetsåtgärd kan försämra tillgänglighet om den konfigureras fel.

Ett klart exempel var när jag bytte ut koden för min harden funktion som ändrade både fil men också mappen från ursprungligen 700 till chmod 600 vilket gjorde att jag förlorade access och persmissions ganska fort och låste mig ute från att kunna köra skriptet ordentligt. 

Ett annat exampel var att jag skapade och körde skriptet som root i början men ändrade detta så att vilken användare kan köra detta skriptet men endast den som kör skriptet kan få åtkomst till mappen och läsa filen.

Detta är något som jag kommer ta med mig i framtiden.

-------------------------------------------------------------

## Reflektion & förbättring
Att skapa ett robust skript i bash kan vara svårt och ganska oflexibelt men är ett otroligt bra verktyg för att kunna skapa små och konsisa automationer som hjälper daglig drift. Att skapa större skript i bash kan leda till olika säkerhets risker som till exempel mitt chmod problem eller att man råkar köra den i admin så den skapar, flyttar eller raderar mappar den inte borde ha gjort. 

Man kan alltid förbättras och om jag skulle fortsätta med skriptet och försöka att optimera det så skulle jag nog skapa fler funktioner och kalla på dem genom bättre argument för att i slutändan få en mer lättläslig kod men också mer användarvändligt. Ner det kommer till harderning och säkerhets tänket så har jag lagt till en funktion som tar bort hela README.md filen och skapar en ny med chmod redan fixat, detta kan självklart skapa problem när det kommer till felsök under en längre period och finns då en chans att förlora datan för alltid. 

Det jag skulle kunna förbättra är att skapa en temporär logg vid varje skript exekvering och fråga om man skicka denna loggen över till en mer permanent logg som inte tas bort av programmet. Tanken var att behålla intigriteten på filen så den inte kan manipuleras externt med konfidentialitet i åtanke men när jag avväger hur jag har kodat så kommer det självklart att påverka tillgängligheten till loggen om det tas bort efter att loggen har mött en viss mängd.

• Vilken kontroll gav mest värde och varför?
• Vilken miljöskillnad påverkade ditt arbete?
• Vilket fel var svårast att tolka?
• Vad skulle du förbättra i en version 2?
• Hur kan verktyget användas i en verklig drift- eller säkerhetsprocess utan att bli riskabelt?

