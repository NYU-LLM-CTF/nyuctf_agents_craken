# Hidden Path

> Where did the attacker hide the reverse shell in the web server?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `rev.php` like this


[Image extracted text: [Image not found]]


Seem the file is renamed to `.backdoor.php`

After that make a new dir named `foo` and move the reverse file path


[Image extracted text: [Image not found]]


And rename the directory


[Image extracted text: [Image not found]]


Because the format is `BDSEC{/path}`

Then flag is

```
BDSEC{/opt/lampp/htdocs/app/admin_panel/.foo/.backdoor.php}
```