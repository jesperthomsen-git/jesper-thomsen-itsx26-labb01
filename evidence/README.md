## Testing

Här kommer skärmdumpar samt reflektion ske vid vissa utfall från skriptet


## Tester som utförs på skriptet:

### Normalfall 1
Jag har gjort att man skriver en hemsida utanför skriptet utav säkerhetsskäl. I denna kontroll kommer jag använda mig utav google.com

### Normalfall 2
I testet för lokala tjänster har jag gjort att om skriptet antingen hittar tjänster som lyssnar eller att specifikt port 8080 är uppe får jag en logg på att den hittar tjänster och räknar upp hur många samt om en lokal server är öppen på port 8080.

Här visar mitt skript tydligt att port 8080 är öppen:

Här visar den hur många lyssnande portar som finns aktiva vid tillfället:

### Felfall 1
Då jag har skapat ett skript som kontrollerar hemsidan utanför skriptet skapar detta en enkel kontroll om hemsidan finns eller inte, samt om skriptet körs utan att skriva något efter du exekverar skriptet:

Ogiltig hemsida:

Lämnar fältet tomt:


### Felfall 2

Här visar mitt skript tydligt att port 8080 into är öppen:

Här visar mitt skript tydligt att port 8080 är stängd genom antalet LISTEN som den kan hitta genom ss -tuln: