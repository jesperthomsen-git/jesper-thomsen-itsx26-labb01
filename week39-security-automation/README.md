
## Syfte
--------------------------------------------

Syftet med detta program är att skapa en automatisering utav dataextrahering och sedan skapa en konsis rapport som matchar IOC filen som matas in. 

Indata som matas in i programmet är inte nödvändigtvis

## Datasetval
--------------------------------------------

I mitt program har jag då valt att använda mig utav "Dataset B: Advanced" som jag skapade ett ramverk mot.

## Pythonversion
--------------------------------------------

Programmet körs genom Python verison 3.14.7.

## körinstruktion
--------------------------------------------

Körinstruktion har definerats via funktioner för att skapa en översikt som både skapar läsvänlighet men också gör att programmets kod blir överskådligt.

Programmets körinstruktion är strukturerat som följande: 
* Extrahering av data från designerad folder.
* Data samlas i en CSV databank.
* Datan extraheras från databanken till skriftlig rapport.


## projektstruktur
--------------------------------------------

Projektstrukturen ser ut som följande

week39-security-automation/<p>
├── README.md<p>
├── data/<p>
│   ├── auth.log<p>
│   ├── access.log<p>
│   ├── firewall.log<p>
│   └── suspicious_ips.txt<p>
├── src/<p>
│   └── notebook_for_security_report_py #Jupyter Notebook fil skapades för att kunna manipulera CSV dokumentet i en säker miljö utan att skriva över funktioner eller data som samlades in i dokumentet. <p>
│   └── security_report.py<p>
├── output/<p>
│   └── security_report.txt<p>
│   └── security_report.csv #Fil som skapas genom data extrahering i programmet, agerar som databas. <p>
└── docs/<p>
    └── analysis.md<p>

Följande filer som har kommentarer är filer som har lagts till för att skapa en säker miljö för databashantering samt att [security_report.csv](src/security_report.csv) är databasen som skapas efter var körning som samlar all information värt att samla in från ./data mapppen.

## testning
--------------------------------------------

Genom att utföra specifika testfall där skriptet kan visa svagheter har gjort att programmet i sig har blivit robust. Testfall som exempel har varit att kontrollera tomma linjer, linjer som har skapats på fel sätt eller extraherats fel och fått då fel data inskrivet i loggen samt att input kan verifieras och matchas mot IOC listan. 


## kända begränsningar 
--------------------------------------------

Begränsningar kommer visa liknelser som i slut rapporten.

Begränsningarna som jag kan se i detta program även om det har en gedigen ryggrad är att den inte är särskilt flexibel innanför skriptet.
Då detta program är kodad för att fungera mot windows och mot denna repo struktur kan inte detta program fungera utanför SDP mappen. Programmet är skriven för SDP och när frågan om den är körbar på OCI eller andra linux system är detta självjkart en faktor jag har tänkt på för vidare utväckling.

Då databasen i sig är textbaserat med kolumnfält så tar jag hjälp av Jupyter Notebook för at lära mig hur man kan extrahera data eller manipulera csv filen utan att radera eller ändra i filens data.
Via Jupyter kan man enkelt bläddra och sortera effektivt efter det man söker efter och finns extra information i CSV filen som jag inte har tagit med i min rapport som uträkning av total IOC som kan indikera potentiella aktiviteter. Det som behöver understrykas är att den inte indikerar en attack men mer
skapa en översikt om vad som behöver dikteras vart och vilka beslut som man behöver ta i framtiden.

Vänligen ta en stund att titta på [security_report.csv](output/security_report.csv) filen om du får tid över för att se prioritering genom poängbaserat system samt vilken risk klass den anser vissa stadier av poäng visar.



## AI-redovisning.
--------------------------------------------

Genererad resultatrapport med datakällor, antal, minst en konkret observation och minst en begränsning.