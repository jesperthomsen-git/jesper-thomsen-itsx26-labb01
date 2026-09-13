## Sanerad exempelutdata från loggen

Detta är vad loggen skriver ut när man har en giltig hemsida som man kör skriptet med, port 8080 är inte aktiv.

15:27:11 | [INFO] Kontrollerar loggen och strukturen på filerna.(Denna info loggas ej i README.md)
15:27:11 | [INFO] Påbörjar verifiering av directory...(Denna info loggas ej i README.md)n
15:24:07 | 5...
15:24:07 | 4...
15:24:07 | 3...
15:24:07 | 2...
15:24:07 | 1...
15:24:07 | [INFO] Evidence mappen finns redan.
15:24:07 | [INFO] logfile.md finns redan, loggningen kommer återupptas.
15:24:07 | [OK] Verifiering av filerna lyckades.
15:24:08 | [WARN] Filen har för mycket information och bör raderas, fortsätta med raderingen?
15:24:09 | [OK] Raderingen avbryts.
15:24:09 | 5...
15:24:09 | 4...
15:24:09 | 3...
15:24:09 | 2...
15:24:09 | 1...
15:24:09 | [INFO] Evidence mappen finns redan.
15:24:10 | [INFO] logfile.md finns redan, loggningen kommer återupptas.
15:24:10 | [OK] Verifiering av filerna lyckades.
15:24:10 | [OK] Hardening lyckades
15:24:10 | [INFO] Kontrollerar mjukvara:Distributor ID: Ubuntu
Description:    Ubuntu 26.04 LTS
Release:        26.04
Codename:       resolute
VERSION_ID="26.04"
15:24:10 | [INFO] kontrollerar om hemsidan existerar.
15:24:10 | [OK] Hemsidan google.com är tillgänglig.
15:24:10 | [INFO] kontroll startat
15:24:10 | [INFO] DNS fungerar.
15:24:10 | [INFO] Startar en lokal check lokalt
15:24:10 | [INFO] Kontrollerar porten 8080 är öppen
15:24:10 | [FAIL] Porten är inte öppen
15:24:10 | [INFO] Kontrollerar om det finns lyssnande portar
15:24:10 | [OK] Det finns 6 lyssnande portar
15:24:10 | [INFO] kontroll avslutad.
15:24:10 | [INFO] Sammanfattning av kontrollerna: 6 lyckades, 1 varningar, 1 misslyckanden.
15:24:10 | [INFO] Loggen finns i /home/ubuntu/evidence/logfile.md
15:24:10 | [INFO] README.MD finns i /home/ubuntu/evidence/README.md
15:24:10 | [INFO] Skapar README.md som existerar i repot.