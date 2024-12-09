# Attaaaaack8
> Q8. What is the Attacker's C2 domain name and port number ? (domain name:port number)

> example : crew{abcd.com:8080}

## About the Challenge
We got `raw` image and we need to find the C2 domain and the port number

## How to Solve?
To solve this, we can use `strings` and `grep` command to find C2 domain and the port number. Here is the command I used

```
strings 300.dmp | grep -oP '.+\.\w+\:[1-9]\d+'
```

The command searches for lines in the `300.dmp` file that contain a domain and then followed by the port number


[Image extracted text: daffainfo@dapos
dumpdirf strings
300 . dmp
grep
~OP
A+.lw+l : [1-9]ld+
127.0.0.1.1604
NETDATA-{test213.no-ip.info:1604
NETDATA-{test213.no-ip.info:1604
test213
no-ip.info:1604
13.no-ip.info:1604
test213
no-ip.info:1604
NETDATA-{test213.no-ip.info:1604
HOST:
239
255
255.250:1900
HOST:
239
255
255.250:1900
HOST:
239
255
255.250:1900
HOST:
239
255.255.250:1900
HOST:
239
255.255.250:1900
HOST:
239.255.255.250:1900
HOST :
239
255 255250: 1900]


```
crew{test213.no-ip.info:1604}
```