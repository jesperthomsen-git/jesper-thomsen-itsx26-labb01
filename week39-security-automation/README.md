
## Syfte
--------------------------------------------

Syftet med detta program är att skapa en automatisering utav dataextrahering och sedan skapa en konsis rapport som matchar IOC filen som matas in. 

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


## kända begränsningar 
--------------------------------------------


## AI-redovisning.
--------------------------------------------

Genererad resultatrapport med datakällor, antal, minst en konkret observation och minst en begränsning.