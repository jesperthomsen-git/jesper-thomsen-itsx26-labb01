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
#less $HOME/evidence/README.md för att se kopia på README filen från repot.
#cat $HOME/evidence/logfile.md för att se loggen.

#nohup python3 -m http.server 8080 >/tmp/http.log 2>&1 & för att starta en lokal testserver från studiematerialet.

#skapar variabler som räknar ihop en sammanfattning i slutet av skriptet.
Success=0
Warning=0
Fail=0

logfile="$HOME/evidence/logfile.md"
readme="$HOME/evidence/README.md"
evidence="$HOME/evidence"





cleanup() { #raderar fil
        rm $logfile
}

log() { #skapar en funktion som lagrar loggen mot logfile.md med en enkel seperation för datum + kommentaren jag kör log() mot
        printf '%s | %s\n' "$(date '+%T')" "$*" |
        tee -a "$logfile"
}
logr() { #skapar en funktion som lagrar loggen mot README.md med en enkel seperation för datum + kommentaren jag kör logr() mot
        printf '%s | %s\n' "$(date '+%T')" "$*" |
        tee -a "$readme"
}

harden() { #Skapar snabbt rättigheter på mappen & filen readme + logfile.
        chmod 700 "$evidence" &&
        chmod 700 "$readme" &&
        chmod 700 "$logfile"
}

mksetup(){

printf '%s | %s\n' "$(date '+%T')" "[INFO] Påbörjar verifiering av directory...(Denna info loggas ej i README.md)" >&2

countdown=("5" "4" "3" "2" "1") #Skapar en array som räknar ner innan verifieringen av filerna sker.
        
        for x in "${countdown[@]}"; do

                if [[ ! -f "$readme" ]]; then
                        printf '%s | %s\n' "$(date '+%T')" "$x..." >&2
                else
                        log "$x..."
                fi
        done

        for evidence in "$evidence"; do #Skapar en kontrollerad loop som kollar om README.md finns.

                #Denna loop idé var inspererad från https://oneuptime.com/blog/post/2026-03-02-how-to-create-loops-for-while-until-in-bash-on-ubuntu/view
                #Testar en ny metod för att kontrollera om mappen och filen finns.


    
                [[ -d "$evidence" ]]  || {
                        #mkdir för att skapa mappen.                                
                        printf '%s | %s\n' "$(date '+%T')" "[INFO] Hittar inte evidence mappern, skapar den nu.(Denna info loggas ej i README.md)" >&2 

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

                [[ -f "$logfile" ]] ||  {
                        #touch för att skapa filen.
                        touch "$logfile" || {

                        Fail=$((Fail + 1))
                        log '[FAIL] Kunde inte skapa logfile.md i evidence directory, saknar permissions.'
                        }
                        printf '%s | %s\n' "$(date '+%T')" "[INFO] Hittar inte logfile.md, skapar den nu.(Denna info loggas ej i README.md)" >&2 

                        Success=$((Success + 1))
                        log "[OK] Lyckades skapa logfile.md filen."
                }

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

                if [[ ! -f "$logfile" ]]; then
                :
                else
                        log "[INFO] logfile.md finns redan, loggningen kommer återupptas."
                fi

                Success=$((Success + 1))
                log "[OK] Verifiering av filerna lyckades."

                break #skapar en breakpoint här när kravet möts. 
        done
}

version() { #Skapar en funktion för att skapa en lista av release samt vilken distro min OCI kör
        lsb_release -a &&
        grep 'VERSION_ID' /etc/os-release
}

deletefiles() { #Skapar en ja eller nej prmpt där ja kallar på cleanup funktionen
        read -e -p "Ska filen '$logfile' raderas [y/n]" val

        if [[ "$val"  == [Yy]* ]]; then
                log "[INFO] Raderar filen $logfile"
                cleanup
        else
                Success=$((Success + 1))
                log "[OK] Raderingen avbryts."
fi
}


structurecheck(){ #Kallar på funktionen som skapar ny fil eller låter det vara baserat på wordcount i if statementen ovan
       
        mksetup
        harden

        if [ "$(grep -c '|' $logfile)" -gt 20 ]; then
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

target="$1" #Target blir den hemsida du skriver utanför skriptet

if [[ -z "$target" ]]; then #Kontroll att skriptet inte körst tomt

        Fail=$((Fail + 1))
        log "[FAIL] fältet $target är tomt, skriv en hemsida med ett mellanslag efter skriptet."
        exit 1

fi


if getent hosts "$target" > /dev/null; then #Kontrollerar att hemsidan kan nås
        
        Success=$((Success + 1))
        log "[OK] Hemsidan $target är tillgänglig."
        log "[INFO] kontroll startat"
        log "[INFO] DNS fungerar."

else
        Fail=$((Fail + 1))
        log "[FAIL] DNS fungerar inte"

fi

while true; do #Skapar en loop som kollar om olika portar är öppna eller ej samt om det finns portar som lyssnar.

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

        listen_count=$(ss -tuln | grep LISTEN | wc -l) #Räknar antalet lyssnande portar

        if [[ "$listen_count" -gt 0 ]]; then #Skriver ut antalet lyssnande portar om det finns.

                log "[INFO] Kontrollerar om det finns lyssnande portar"
                Success=$((Success + 1))
                log "[OK] Det finns $listen_count lyssnande portar"
                break #Skapar breakpoints här för att avsluta loopen om kravet möts.
                else
                
                log "[INFO] Kontrollerar om det finns lyssnande portar"
                Fail=$((Fail + 1))
                log "[FAIL] Det fanns inga lyssnande portar"
                break #Skapar en till breakpoint här för att avsluta loopen.
        fi
done
log "[INFO] kontroll avslutad."
log "[INFO] Sammanfattning av kontrollerna: $Success lyckades, $Warning varningar, $Fail misslyckanden."
log "[INFO] Skapar README.md som existerar i repot."

logr "##Testing"
logr "Här kommer skärmdumpar samt reflektion ske vid vissa utfall från skriptet"
logr "(Dessa är uppladdade i GitHub)."
logr ""
logr "##Tester som utförs på skriptet:"
logr ""
logr "----------------------------------------------------------------"
logr ""
logr "### Normalfall 1"
logr "Jag har gjort att man skriver en hemsida utanför skriptet utav säkerhetsskäl. I denna kontroll kommer jag använda mig utav google.com"
logr ""
logr "![alt text](../docs/Screenshots/v37/dnsfunction.png) "
logr "Här kan man se att google.com svarar genom loggen [INFO] DNS Fungerar. Förbättring här kunde vara att göra ett OK istället för INFO."
logr ""
logr "* Det förväntade resultatet: Jag förväntade mig att genom att skriva ./secure_network_check.sh google.com skulle starta skriptet och ha google.com som variabeln som sparas för sökning i skriptet."
logr "* faktiska resultatet: Utfärdades som planerat"
logr "* slutsats: att skapa target=$1 som variabel som kallas utanför skriptet fungerade utmärkt då det kändes lite osäkert i början medans jag byggde upp grunden. Som slutsats fungerade som planerat."
logr ""
logr "----------------------------------------------------------------"
logr ""
logr ""
logr "### Normalfall 2"
logr "I testet för lokala tjänster har jag gjort att om skriptet antingen hittar tjänster som lyssnar eller att specifikt port 8080 är uppe får jag en logg på att den hittar tjänster och räknar upp hur många samt om en lokal server är öppen på port 8080."
logr ""
logr "Här visar mitt skript tydligt att port 8080 är öppen:"
logr "![alt text](../docs/Screenshots/v37/port8080.png)"
logr ""
logr "Här visar den hur många lyssnande portar som finns aktiva vid tillfället:"
logr "![alt text](../docs/Screenshots/v37/listenports.png)"
logr ""
logr "* Det förväntade resultatet: Jag förväntade att den skulle kunna hitta en specifik tråd där jag använde mig av grep funktionen."
logr "* faktiska resultatet: Den hittade porten samt hur många lyssnare som finns genom grep och wc -l som underlättade enormt."
logr "* slutsats: Att använda grep och wc -l är bra verktyp för att extrahera hård data utan att skapa potentiell exponering av känslig information." 
logr ""
logr "----------------------------------------------------------------"
logr ""
logr "### Felfall 1"
logr "Då jag har skapat ett skript som kontrollerar hemsidan utanför skriptet skapar detta en enkel kontroll om hemsidan finns eller inte, samt om skriptet körs utan att skriva något efter du exekverar skriptet:"
logr ""
logr "Ogiltig hemsida:"
logr "![alt text](../docs/Screenshots/v37/dnsoff.png)"
logr "Här kan man se på ett enkelt sätt att DNS funktionen inte fungerar och visar då att hemsidan man skrev är onåbar."
logr ""
logr "![alt text](../docs/Screenshots/v37/emptyadress.png)"
logr "Jag har också gjort så att om adressfältet är tomt så stoppas skriptet för att se till att man antingen skriver rätt adress man vill kontrollera eller om man helt enkelt glömde att skriva in det till att börja med. "
logr ""
logr "* Det förväntade resultatet: Jag hade hoppats att den gav mig något form of felmeddelande som t.ex att den inte hittade DNS servern"
logr "* faktiska resultatet: Skriptet hittade inte hemsidan som nämnt."
logr "* slutsats: Jag testade aldrig att skriva fel output som en kombination av bokstäver och nummer, detta är bra då den svarar ändast på existerande hemsidor och skyddar sig mot injecering eller strings som kan utföra skada mot koden."
logr ""
logr "* notering: jag skapade också en extra funktion som stoppade skriptet om man lämnade fältet tomt och fungerade utan komplikationer."
logr "----------------------------------------------------------------"
logr ""
logr "### Felfall 2"
logr ""
logr "Här visar mitt skript tydligt att port 8080 inte är öppen:"
logr "![alt text](../docs/Screenshots/v37/port8080closed.png)"
logr "Här behövde jag stänga ner servern för att kontrollera att skriptet känner igen att porten 8080 är nere ooch fick då ett felmeddelande samt att detta lägger till i summeringen hur många fel det uppstår under skriptets process."
logr ""
logr "Här visar mitt skript tydligt att port 8080 är stängd genom antalet LISTEN som den kan hitta genom ss -tuln:"
logr "![alt text](../docs/Screenshots/v37/listenportclosed.png)"
logr "Med denna räkning från felfallet i jämförelse med när porten 8080 var öppen i normalfallet så kan man se att porten faktiskt är stängd."
logr ""
logr "* Det förväntade resultatet: Då grep fungerade i normal fallet så förväntade jag mig att denna funktion också kunnde skriva en felkod då jag gjorde en "else" i if satsen."
logr "* faktiska resultatet: Den skrev ut det som var planerat och loggade det i filen jag ville."
logr "* slutsats: Funktionen fungerade som planerat."
logr ""
logr "----------------------------------------------------------------"
logr ""
logr "## Koppling till vecka 36"
logr ""
logr "* Hardening: jämför lyssnande portar och tjänster med vad du förväntar dig efter genomförd hardening. Motivera minst en tjänst som behöver finnas kvar."
logr ""
logr "Reflektion: Efter att jag har kört igenom mitt skript och kontrollerat att min HTTP server på 8080 är nere kan jag se att portarna 53, 22 och 111 är öppna. Jag har gjort lite research på howtouselinux.com som beskriver port 111 som är någon form av portmap."
logr "Jag trodde först att det var en port jag möjligtvis kunde stänga men ser ut som att det är en tjänst som bör vara öppen ifall jag vill skicka filer mellan system. Dessa tre portar verkar vara väldigt viktiga för drift, specifikt port 22 som är för ssh. Port 53 är viktig då denna hanterar DNS så ingen tvekan om att denna behövs."
logr ""
logr "*Backup och recovery: förklara vilka två nätverkskontroller i ditt verktyg som du skulle köra först efter en återställning och vad de verifierar. Ingen ny restore krävs."
logr ""
logr "Reflektion: Om jag kör mitt program kommer den alltid kontrollen om mapp strukturen finns eller inte samt om den har ändrade rättigheter. Detta skapar en bra grund för att skriptet kan fortsätta samt att den kontrollerar att vissa portar är aktiva, eller om den är kopplad till internet kan vara nog information för att kunna börja med felsökningar."

log "[INFO] Loggen finns i $logfile"
log "[INFO] README.MD finns i $readme"