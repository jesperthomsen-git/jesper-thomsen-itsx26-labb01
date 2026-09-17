## IP tester

ip -br address

lo 127.0.0.1 
ens3 up 10.0.0.235/24

observationen visar att jag är i ett privat subnät 255.255.255.255
UP ens3 nätverkskortet kör

Visar inte gateway eller om man har tillgång till internet

Jag kör OCI

-----------------------------------------------

ip route

10.0.0.0/24 dev ens3 proto kernel scope link src 10.0.0.235 metric 100
10.0.0.1 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100
169.254.0.0/16 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100
169.254.169.254 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100

Visar vägen ut till nätet genom default gateway och att gateway är nåbar

Den visar inte om man har tillgång till internet 

-----------------------------------------------

getent hosts example.com

2606:4700:10::ac42:93f3 example.com
2606:4700:10::6814:179a example.com

Visar ipv6 samt att man har tillång till internet.
DNS hittar hemsidan

Visar inte ipv4, ip addressen som DNS konverterade från example.com

-----------------------------------------------

curl -i https://example.com

HTTP/2 200
date: Mon, 14 Sep 2026 07:29:10 GMT
content-type: text/html
server: cloudflare
last-modified: Fri, 11 Sep 2026 17:42:00 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 1958
cf-cache-status: HIT
cf-ray: a3adadd61cdc323b-ARN

<!doctype html><html lang="en"><head><title>Example Domain</title><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>

Visar HTTP protokollet, strukturen av hemsidan via html kod, visar Head och body, och vilken server som hostar hemsidan

Visar default gateway fungerar, DNS hittar hemsidan och du är kopplad till internet
Beroende på om man curlar http vs https får man olika http protokoller

Den visar inte hur vägen till hemsidan?

-----------------------------------------------

## interface med avsikt

IP ROUTE

lo               UNKNOWN        127.0.0.1/8 ::1/128
ens3             UP             10.0.0.235/24 metric 100 fe80::17ff:fe02:f9e8/64

IP ROUTE

default via 10.0.0.1 dev ens3 proto dhcp src 10.0.0.235 metric 100
10.0.0.0/24 dev ens3 proto kernel scope link src 10.0.0.235 metric 100
10.0.0.1 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100
169.254.0.0/16 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100
169.254.169.254 dev ens3 proto dhcp scope link src 10.0.0.235 metric 100

TCPDUMP -D

1.ens3 [Up, Running, Connected] - ens3 UP 10.0.0.235/24 metric 100 fe80::17ff:fe02:f9e8/64
2.any (Pseudo-device that captures on all interfaces) [Up, Running]
3.lo [Up, Running, Loopback] 
4.bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
5.nflog (Linux netfilter log (NFLOG) interface) [none]
6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
7.dbus-system (D-Bus system bus) [none]
8.dbus-session (D-Bus session bus) [none]

-----------------------------------------------

## begränsa fångsten

sudo timeout 30 tcpdump -i any -s 0 -w traffic_week38.pcap
