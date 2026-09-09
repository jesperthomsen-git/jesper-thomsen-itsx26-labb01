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
