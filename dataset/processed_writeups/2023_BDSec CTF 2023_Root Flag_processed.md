# Root Flag

> What binary had the root permission?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Linux` like this

And `flag` filter at the streams


[Image extracted text: [Image not found]]


Because the format is `BDSEC{flag}`

Then flag is

```
BDSEC{Y0u_NaILeD_IT_HaCkEr}
```