# Week 36 OCI Cloud Security Lab
## 1 & 2 Min OCI-miljö/Min lokala Linux-miljö/Min lokala WSL-miljö
- Tenancy (N/A): jesperthomsen
- Compartment (Endast OCI): jesperthomsen (root)
- Region (Endast OCI): eu-stockholm-1
- Availability Domain (Endast OCI): AD-1
- VM-namn/hostnamn/WSL-maskinnamn: itsx26-Jesper-vm
- Operativsystem: Canonical Ubuntu
- Shape (Hårdvara, gäller alla): VM.Standard.E2.1.Micro
- Inloggningsmetod: SSH med nyckel

Här är en screenshot på min compartment och vad som finns i jesperthomsen (root):<p>
![Compartments](Screenshots/v36/Compartments.png)

Här är en bild på att min VM är uppe och kör:<p>
![alt text](Screenshots/v36/itsx26-vm.png)

---
## 3.4 Linux-kommandon

| Kommando | Vad visar det? | CIA-koppling |
|-----------|-----------|-----------|
| whoami | inloggad som ubuntu | (Konfidentialitet) Visar användaren som är inloggad och visar vem det är som skriver kommandot och visar hur enkelt det är att få tag på namnet på en användare.  |
| hostname | servern heter instance-20260901-1629 | (Konfidentialitet) Att detta kommando visar namnet på datorn eller namnet som tillgets i nätverket kan skapa problem som ingående attacker som kan se nätverket. |
| pwd | /home/ubuntu | (Konfidentialitet/ Riktighet) Då detta visar innehåll i mappen man kör kommandot kan detta skapa frågor kring riktigheten i mappen om det skulle vara så att andra har tillgång till din användar mapp och behöver ta extra steg för att försäkra sig att informationen är riktig. |
| uname -a |OS som körs är Linux instance-20260901-1629 7.0.0-1009-oracle #9-Ubuntu SMP PREEMPT Thu Jul 23 02:43:14 UTC 2026 x86_64 GNU/Linux | (Konfidentialitet) Då -a gör att du får en hel överblick om datorn eller nätverket kan detta visa sårbarheter så som versionsnummer, maskin name, samt på vilken OS den kör kan detta. |
| uptime | Servern har varit uppe i 19 timmar och 4 minuter, 09:47:01 up 19:04,  1 user,  load average: 0.11, 0.10, 0.09 | (Tillgänglighet) På uptime får man information hur många användare som finns på servern samt hur ansträngd servern är kan detta vara ett bra verktyg för att säkerställa att behöriga som behöver åtkomst kommer in och en översikt så servern inte blir överbelastat. |

## 4 utforska Linux

| kommandon: | Vad kommandot gör | Vad resultatet betyder | Vilken del av CIA-triaden det kan kopplas till |
|-----------|-----------|-----------|-----------|
| ls -la | Skapar en lista på allt innehåll | Resultatet visar allt som finns i ett directory | (konfidentialitet / riktighet) |
| date | Visar dagens datum & tid | --|-- | (riktighet) Hur jag resonerar runt riktighet är att om nätverket eller din VM är attackerad så kan attackeraren ändra loggar eller ändra datum och tid så informationen sparas fel|
| id | Skriver användare & grupp info| Detta betyder att den som skriver in detta kan se vem användaren är samt vilken grupp användaren tillhör samt dess sekondära grupper| (Konfidentialitet) Detta scenario är väldigt lik whoami där informationen som visar här kan skapa sårbarheter där attackeraren kan se ännu mer information som kan utnyttjas än whoami där information visar tillhörigheter både vart den huvudsaklgen tillhör ochhar rättigheter men också andra grupped den har rättigheter i|
| groups | Visar vilken grupp användaren tillhör | Visar endast primära grupper som användaren tillhör | (konfidentialitet) Även om detta är ett lindrigare kommando än id så visar denna kod återigen känslig information om tillhörande och rättigheter som användaren är anknyten till|
| "ps aux | head" | Visar 10 processer | visar alla processer för alla användare, visar ägandeskap samt processer som ej är kopplade till terminalen. Head visar de 10 första högst krävande processerna | (Konfidentialitet, tillgänglighet) ps aux visar alla processer oberoende på användare och kan visa känslig information kopplade till oilka användare och med rätt kommandon kan ett angrepp enkelt slå av viktiga processer som är aktiva|

---
## 5. Hardening
| Kontroll | Risk | Vad gjorde jag? | Hur verifierade jag? | CIA |
|-----------|-----------|-----------|-----------|-----------|
| whoami && id && groups | ubunutu är root och sudo rättigheter | Konsolen verifierar att detta input är korrekt | konfidentialitet |
| chmod 600 | Kan låsa andra ute som behöver åtkomst | skapade en fil och ändrade rättigheter | (Tillgänglighet) Kan låsa andra ute som behöver åtkomst till en specifik fil eller mapp|
| sudo apt update | risk för attacker utan regelbunden uppdatering | uppdaterade min VM till senaste verionen | (Tillgängligher, Konfidentialitet) |

Kontroll 1:<p>
![alt text](Screenshots/v36/whoami.png)
Ubuntu är användaren
Användaren tillhör adm, cdrom, sudo, dip & lxd
Administrativa rättigheter kan skapa stora problem om syntaxen eller kommandot är felskrivet

Kontroll 2:<p>
![alt text](Screenshots/v36/testtxt.png)

Vem får läsa filen?
Chmod 600 ändrar så bara ägaren får läsa filen.

Vem får ändra filen?
Endast ägaren.

Kontroll 3:

Varför är uppdateringar viktiga?
Att uppdatera regelbundet skapar en säkrare miljö där mjukvara kan exploiteras
Vilken del av CIA påverkas?

Att uppdatera sin miljö regelbundet påverkar både användarens tillgänglighet då större uppdateringar kan ta längre tid och konfidentialiteten behålls säkert då uppdateringen kan minska risken för attacker. 

---

## 4. Recovery-plan
### Vad kan gå fel?
### Hur upptäcker jag problemet?
### Vad kontrollerar jag först?
### Hur återställer jag åtkomst?
### När behöver jag hjälp?
---
## 5. Backup
### Vad har jag sparat?
### Vad finns i GitHub?
### Vad kan återskapas?
### Vad går inte att återskapa?
---
## 6. Cleanup
### VM-instans
### Diskar
### Backuper
### Publika IP-adresser
### GitHub-evidens
---
## 7. CIA-reflektion
### Konfidentialitet
### Integritet
### Tillgänglighet
---
## 8. Reflektion
### Vad fungerade bra?
### Vad var svårt?
### Vad lärde jag mig?