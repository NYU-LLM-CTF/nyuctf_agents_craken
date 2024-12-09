# Follow the Path

> What is the path of the Admin endpoint?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `admin_panel` like this


[Image extracted text: [Image not found]]


Because the format is `BDSEC{/path}`

Then flag is

```
BDSEC{/app/admin_panel}
```