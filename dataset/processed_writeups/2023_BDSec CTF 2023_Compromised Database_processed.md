# Compromised Database

> How did the attacker enumurate & compromised the database?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `UNION` because according the description database is more like SQL Injection POC


[Image extracted text: [Image not found]]


Then we look the header of request


[Image extracted text: [Image not found]]


Because the format is `BDSEC{name/version}`

Then flag is

```
BDSEC{sqlmap/1.6.10#stable}
```