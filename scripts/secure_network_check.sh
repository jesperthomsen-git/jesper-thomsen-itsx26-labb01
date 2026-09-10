
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






#NY VERSION: 10-09
cleanup() { #raderar fil
        rm network_check_log.txt
}

function y_n { #skapar en ja eller nej prmpt där ja kallar på cleanup funktionen
        read -e -p "Ska filen '$logg' raderas [y/n]" val

        if [[ "$val"  == [Yy]* ]]; then
                log "Raderar filen $logg"
                cleanup
        else
                log "Avbryter raderingen."
fi
}


mf #kontrollerar om filen finns

if [ "$(grep -c '|' $logg)" -gt 20 ]; then

        log "Filen har för mycket information och bör raderas, fortsätta med raderingen?"
        y_n
        mf
#kallar på funktionen som skapar ny fil eller låter det vara baserat på wordcount i if statementen ovan
fi



log "[INFO] kontrollerar hemsida"

target="$1" #target blir den hemsida du skriver utanför skriptet



if [[ -z "$target" ]]; then #kontroll att skriptet inte körst tomt

        log "[FAIL] fältet $target är tomt, skriv en hemsida med ett mellanslag efter skriptet."
        exit 1

fi


if getent hosts "$target" > /dev/null; then #kontrollerar att hemsidan kan nås

        log "[INFO]kontroll startat"
        log "[INFO] kollar att $target finns"
        log "[OK] DNS fungerar."

        else
        log "[FEL] DNS fungerar inte"
        exit 1

fi

if ss -tuln | grep 8080 >/dev/null; then #kontrollerar om ens lokala port är öppen eller ej

        log "[INFO] Porten är öppen"

        else
        log "[FEL] Porten är inte öppen"
        exit 1
fi


log "[INFO] kontroll avslutad."