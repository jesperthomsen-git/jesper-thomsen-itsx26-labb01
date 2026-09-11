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
#Slutsammanfattning    | Visa hur många kontroller som lyckades och var loggen finns.



#***********************************************************************************************#
# VIKTIG INFO: HEMSIDAN SKRIVS UTANFÖR SKRIPTET, EXEMPEL: ./secure_network_check.sh example.com #
#***********************************************************************************************#
#cat $HOME/evidence/README.md för att se loggen.
#nohup python3 -m http.server 8080 >/tmp/http.log 2>&1 & för att starta en lokal testserver från studiematerialet.

#skapar variabler som räknar ihop en sammanfattning i slutet av skriptet.
Success=0
Warning=0
Fail=0

readme="$HOME/evidence/README.md"
evidence="$HOME/evidence"

cleanup() { #raderar fil
        rm $readme
}

log() { #skapar en funktion som lagrar loggen mot README.md med en enkel seperation för datum + kommentaren jag kör log mot
        printf '%s | %s\n' "$(date '+%T')" "$*" |
        tee -a "$readme"
}

harden() { #skapar snabbt rättigheter på mappen & filen readme
        chmod 700 "$evidence" &&
        chmod 700 "$readme"
}

mksetup(){

printf '%s | %s\n' "$(date '+%T')" "[INFO] Påbörjar verifiering av directory...(Denna info loggas ej i README.md)" >&2

countdown=("5" "4" "3" "2" "1") #skapar en array som räknar ner innan verifieringen av filerna sker.
        
        for x in "${countdown[@]}"; do

                if [[ ! -f "$readme" ]]; then
                        printf '%s | %s\n' "$(date '+%T')" "$x..." >&2
                else
                        log "$x..."
                fi
        done

        for evidence in "$evidence"; do #Skapar en kontrollerad loop som kollar om README.md finns.

                #Denna loop idé var inspirerad från https://oneuptime.com/blog/post/2026-03-02-how-to-create-loops-for-while-until-in-bash-on-ubuntu/view
                #Testar en ny metod för att kontrollera om mappen och filen finns.


    
                [[ -d "$evidence" ]]  || {

                        printf '%s | %s\n' "$(date '+%T')" "[INFO] Hittar inte evidence mappern, skapar den nu.(Denna info loggas ej i README.md)" >&2 
                #mkdir för att skapa mappen.
                        mkdir -p "$evidence" || {

                        Fail=$((Fail + 1))
                        log '[FAIL] Kunde inte skapa mappen, saknar permissions.' >&2
                        }
        
                        Success=$((Success + 1))
                        printf '%s | %s\n' "$(date '+%T')" "[OK] Lyckades skapa evidence mappen.(Denna info loggas ej i README.md)" >&2
                }
        
                if [[ ! -f "$readme" ]]; then
                        printf '%s | %s\n' "$(date '+%T')" "[INFO] Evidence mappen finns redan.(Denna info loggas ej i README.md)" >&2
                else
                        log "[INFO] Evidence mappen finns redan."
                fi

                [[ -f "$readme" ]] ||  {
                #touch för att skapa filen.
                        touch "$readme" || {
        
                        Fail=$((Fail + 1))
                        log '[FAIL] Kunde inte skapa README.md i evidence directory, saknar permissions.'
                        }
                        printf '%s | %s\n' "$(date '+%T')" "[INFO] Hittar inte README.md, skapar den nu.(Denna info loggas ej i README.md)" >&2 

                        Success=$((Success + 1))
                        log "[OK] Lyckades skapa README.md filen."
        
                } 

                if [[ ! -f "$readme" ]]; then
                :
                else
                        log "[INFO] README.md finns redan, loggningen kommer återupptas."
                fi

                Success=$((Success + 1))
                log "[OK] Verifiering av filerna lyckades."

                break #skapar en breakpoint här när kravet möts. 
        done
}

version() { #skapar en funktion för att skapa en lista av release samt vilken distro min OCI kör
        lsb_release -a &&
        grep 'VERSION_ID' /etc/os-release
}

deletefiles() { #skapar en ja eller nej prmpt där ja kallar på cleanup funktionen
        read -e -p "Ska filen '$readme' raderas [y/n]" val

        if [[ "$val"  == [Yy]* ]]; then
                log "[INFO] Raderar filen $readme"
                cleanup
        else
                Success=$((Success + 1))
                log "[OK] Raderingen avbryts."
fi
}


structurecheck(){ #kallar på funktionen som skapar ny fil eller låter det vara baserat på wordcount i if statementen ovan
       
        mksetup
        harden

        if [ "$(grep -c '|' $readme)" -gt 20 ]; then
                Warning=$((Warning + 1))
                log "[WARN] Filen har för mycket information och bör raderas, fortsätta med raderingen?"

                deletefiles
                mksetup
                harden
        fi

        if harden; then #kallar på harden funktionen
                Success=$((Success + 1))
                log "[OK] Hardening lyckades"

        else
                Fail=$((Fail + 1))
                log "[FAIL] Kunde inte göra hardening på dessa filer. Antingen saknas permissions eller så är dem redan satta."
        fi

}

printf '%s | %s\n' "$(date '+%T')" "[INFO] Kontrollerar loggen och strukturen på filerna.(Denna info loggas ej i README.md)" >&2
structurecheck

log "[INFO] Kontrollerar mjukvara:$(version)"

log "[INFO] kontrollerar om hemsidan existerar."

target="$1" #target blir den hemsida du skriver utanför skriptet



if [[ -z "$target" ]]; then #kontroll att skriptet inte körst tomt

        Fail=$((Fail + 1))
        log "[FAIL] fältet $target är tomt, skriv en hemsida med ett mellanslag efter skriptet."
        exit 1

fi


if getent hosts "$target" > /dev/null; then #kontrollerar att hemsidan kan nås
        
        Success=$((Success + 1))
        log "[OK] Hemsidan $target är tillgänglig."
        log "[INFO] kontroll startat"
        log "[INFO] DNS fungerar."

        else
        Fail=$((Fail + 1))
        log "[FAIL] DNS fungerar inte"

fi

while true; do #skapar en loop som kollar om olika portar är öppna eller ej samt om det finns portar som lyssnar.

        log "[INFO] Startar en lokal check lokalt"

        if ss -tuln | grep 8080 >/dev/null; then #kontrollerar om ens lokala port 8080 är öppen eller ej

                log "[INFO] Kontrollerar porten 8080 är öppen"
                Success=$((Success + 1))
                log "[OK] Porten är öppen"

        else
                log "[INFO] Kontrollerar porten 8080 är öppen"
                Fail=$((Fail + 1))
                log "[FAIL] Porten är inte öppen"

        fi

        listen_count=$(ss -tuln | grep LISTEN | wc -l) #räknar antalet lyssnande portar

        if [[ "$listen_count" -gt 0 ]]; then #skriver ut antalet lyssnande portar om det finns.

                log "[INFO] Kontrollerar om det finns lyssnande portar"
                Success=$((Success + 1))
                log "[OK] Det finns $listen_count lyssnande portar"
                break #skapar breakpoints här för att avsluta loopen om kravet möts.
                else
                
                log "[INFO] Kontrollerar om det finns lyssnande portar"
                Fail=$((Fail + 1))
                log "[FAIL] Det fanns inga lyssnande portar"
                break #Skapar en till breakpoint här för att avsluta loopen.
        fi
done

log "[INFO] kontroll avslutad."
log "[INFO] Sammanfattning av kontrollerna: $Success lyckades, $Warning varningar, $Fail misslyckanden."

log "[INFO] Loggen finns i $readme"