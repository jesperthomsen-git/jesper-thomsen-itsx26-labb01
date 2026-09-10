## Miljöbeskrivning

### Miljö: Oracle Cloud
### Ubuntu 26.04
### Ens3
### Adresser: 
* Lokal adress är localhost 127.0.0.1 och är på ens dator
* Privat adress är ett nätverk som man kan koppla sig till som inte går ut på internet som heter LAN
* Publik adress är din IP adress som blir konverterad till publik så webbplatser vet vem det är. 

### Begränsningar:
* Begränsningar som kan följa med Oracle cloud är att man kan låsa sig själv ute om man gör något fel medans man har sudo rättigheter
* Kan möjligtvis kosta pengar om man ändrar i inställningar
* Kan ha en viss fördröjning
* Har öppna portar 80 & 443 som vem som helst kan komma in genom
* Annorlunda gränsnitt och funktioner från andra distron

## Manuella observationer

| Kontrollerade | Kontroll | Förklarande |
|---|---|---|
| Interface och IP | hostname -i | Hostname ger en localhost adressen för OCI |
| DNS | getent hosts | Visar entries på namnet hosts och visar localhost, loopback och subnätet 127.0.1.1|
| Portar | ss -tuln | Visar vilka portar som är öppna och stängda för tillfället, kan hjälpa med att minska området för attacker |
| Processer | systemctl | Används för att få insikt från systemd men tillåter dig att kontrollera vissa delar så som att slå på ssh som exempel |
| Routing | ip route | Visar prompter och steg för att komma ut på internet |

## CIA-analys

### Konfidentialitet:
Vilka uppgifter i nätverksutdata kan vara känsliga, och hur sanerar du dem?

När det kom till utdatan så var jag mån om att ha hemsidan utanför skriptet, detta var för att både skapa en enklare struktur men också som ett säkerhetstänk för att inte hårdkoda in en hemsida i programmet.

En annan del var när jag använde grep för att få information om min port 8080 var öppen eller ej samt vilka portar som var under listen. Såg till att datan sparades som word count så att känslig information om tjänster eller processer som är aktiva inte blir exponerade.

En extra del i konfidentialitet var att skapa en hardening grund redan från början genom chmod 700 direkt efter skapandet av filen. Då all information sparas i en logg lade jag också till en funktion som räknar hur många loggar som sparas i filen README.md och frågar om man vill radera filen. Om man svarar ja så skapar den en ny loggfil, skapar rättigheterna och börjar logga i den direkt efter.

### Intigritet:
Hur hjälper loggar, versionshistorik, tydliga statusar och kontroller till att skapa tillit till resultatet?

Att man skapar en logg för att se vart som skriptet det går fel eller vart det går rätt till kan ha stor betydelse på hur integriteten förblir fortsatt i skriptet. Versions historik samt tydliga statusar tillsammans med kontroller så som [OK], [INFO] [WARN] eller [FAIL] kan ha stor betydelse i översikten och ger en tydlig bild vart det kan gå fel om man vill troubleshoota.

### Tillgänglighet
Tillgänglighet: Hur visar DNS, route, tjänst och port om en funktion är tillgänglig?


### Avvägning


## Reflektion & förbättring