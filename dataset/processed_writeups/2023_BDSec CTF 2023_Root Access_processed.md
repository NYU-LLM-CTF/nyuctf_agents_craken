# Root Access

> What is the Linux version of the server?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Linux` like this


[Image extracted text: [Image not found]]


Seem the binary command is `sudo vim -c ':!/bin/sh`

Because the format is `BDSEC{Flag}`, which is space is get replaced by underscore 

Then flag is

```
BDSEC{sudo_vim_-c_':!/bin/sh}
```