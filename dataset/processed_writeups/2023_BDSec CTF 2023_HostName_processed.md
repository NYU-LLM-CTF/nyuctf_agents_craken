# HostName

> What is the host name of the web server?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http stream like this


[Image extracted text: [Image not found]]


Because the format is `BDSEC{hostname}`

Then flag is

```
BDSEC{nanomate-solutions.com}
```