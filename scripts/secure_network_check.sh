
harden() { #skapar snabbt rättigheter på mappen & filen readme
        chmod 700 "$evidence" &&
        chmod 700 "$readme"
}


log() { #skapar en funktion som lagrar loggen mot README.md med en enkel seperation för datum + kommentaren jag kör log mot
        printf '%s | %s\n' "$(date '+%T')" "$*" |
        tee -a "$readme"
}

version() { #skapar en funktion för att skapa en lista av release samt vilken distro min OCI kör
        lsb_release -a &&
        grep 'VERSION_ID' /etc/os-release
}



if [[ ! -d "$evidence" ]]; then #skapar en if check som kollar om evidence mappen finns eller inte

#om den inte finns:

        echo "skapar evidence mappen"

        mkdir -p "$evidence" || {
                        log 'Kunde inte skapa mappen, saknar permissions.' >&2
                exit 1
                }

                echo "Lyckades skapa evidence mappen."

        else #om den finns:

                log "Kontrollerar att strukturen finns."
                log "Mappen evidence finns redan. Hoppar över detta steg."

fi

if [[ ! -f "$readme" ]]; then #kontrollerar så att README.md finns eller inte
#om den inte finns:

        echo "Skapar README.md filen"

        touch "$readme" || {
        log "Kunde inte skapa README.md i evidence directory, saknar permissions."
        exit 1
        }

else #om den finns:

        log "README.md finns redan. Hoppar över detta steg."

fi


if harden; then #kallar på harden funktionen

        log "Hardening lyckades"

else
        log "Kunde inte göra hardening på dessa filer. Antingen saknas permissions eller så är dem redan satta."
        exit 1
fi


log "$(version)"