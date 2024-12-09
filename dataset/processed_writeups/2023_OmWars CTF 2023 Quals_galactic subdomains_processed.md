# galactic subdomains
> Find the secret dns record for the domain omwars.org

## About the Challenge
We need to find information about omwars.org dns record

## How to Solve?
To solve this, im using subdomain enumeration tool. In this case im using `subfinder`


[Image extracted text: (kaliokali)-[~]
subfinder
omwars.org"
SulicoGix
projectdiscovery.i0
[WRN]
Use With caution.
You
are
responsible for
your actions
[WRN ]
Developers
assume
no liability
and
are
not
responsible for
any
misuse
or damage
[WRN ]
By using subfinder
you also agree
to the
terms of the APIs
used
[INF
Enumerating subdomains for
omwars.org
ctf
omwars
org
c76aa069ab3f4561801e70b47718093b.ctf
omwars
org
Ju
c76aa069ab3f4561801e70b47718c93b
ctf
omwars
org
Hoamau
ctf
omwars
org
(kaliokali)-[~]]


As you can see there is a weird subdomain. If we access the subdomain we will get the flag


[Image extracted text: < > C
c76aa069ab3f4561801e70b47718c93b.ctfomwars org
OmWars{ssl_c3rt_Iak_SubdOm@lnS}]


```
OmWars{ss1_c3rt_l3ak_$ubd0m@1n$}
```