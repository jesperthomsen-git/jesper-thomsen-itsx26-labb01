#!/usr/bin/env bash

#Kommentar som beskriver syfte och säkerhetsavgränsning.
#• Minst tre variabler.
#• Minst två funktioner, varav en används för loggning eller statusutskrift.
#• Minst två if-villkor.
#• Minst en loop över en liten, uttryckligen definierad lista med säkra kontroller.
#• Minst en kontroll av tomt eller ogiltigt värde.
#• Tydliga statusar, exempelvis INFO, OK, WARN och FAIL.
#• Tidsstämplad loggfil i en katalog som studenten får skriva till.
#• Begripliga exitkoder.
#• Citerade variabler och inga hårdkodade lösenord, nycklar eller tokens.
#• Ett cleanup-beteende som stoppar egen testtjänst eller tar bort temporära filer när det behövs.

#Obligatoriska funktioner
#-------------------------------------
#funktioner            | krav
#Miljööversikt         | Visa eller logga adressinformation och default route.
#DNS-kontroll          | Kontrollera ett säkert, godkänt domännamn och avgör om uppslaget lyckas.
#Lokal tjänstekontroll | Kontrollera localhost och en lokal testport. Det är tillåtet att starta en lokal, tillfällig webbserver.
#Portöversikt          | Sammanfatta lokalt lyssnande portar. Ingen extern portskanning.
#Slutsammanfattning    | Visa hur många kontroller som lyck



readme="$HOME/evidence/README.md"
evidence="$HOME/evidence"
makedir=$(mkdir -p "$HOME/evidence") #skapar en mapp
rights=$(chmod 700 "$evidence" && chmod 700 "$log") #skapar en variabel som både fixar hardening för mapp & evidence
version=$(lsb_release -a && grep VERSION_ID /etc/os-release) #visar full lista av release och vilken distro som kör
log="-$(date +"%T") | tee -a $readme)" #skapar en variabel som loggar datum och text skriver detta i evidence

if [[ ! -p "$evidence" ]]; then #skapar en if check som kollar om evidence mappen finns eller inte
        echo "mappen finns"
        echo "skapar rättigheter för evidence katalogen $rights $log"

else
        echo "Hittade inte mappen, skapar evidence i HOME $makedir $log"
        echo "skapar rättigheter för evidence katalogen $rights $log"

fi

echo "skapar miljööversikt $version $log"