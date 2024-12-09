# coup de réseau
> Too late. The network admin's system was compromised and we can't access our network anymore. Investigate the memory dump.

> Memory Dump Link: https://drive.google.com/file/d/1LbElkzno-FophYpkTLPL5ic2BnZgn-UN/view?usp=sharing

> Amour Plastique will be visible after solving this challenge.

## About the Challenge
We were given a dump memory file called `dump2.mem` and we need investigate the memory dump file

## How to Solve?
In this case im using `strings` and `grep` to get the flag


[Image extracted text: root@ubuntu-s-Ivcpu-Zgb-sgp1-01:~/dumpl# strings
dump2
mem
grep
"nite{"
C: |Users Inapoleon |AppData |Roaming |Microsoft IWindows |Recent Inite{8_bit_synths}
Ink
nite{8_bit_synths}
mp3
main
input debug: Creating
an
input
for
nite{8_bit_synths} '
nite{8_bit_synths}
Ink
nite{8_bit_synths}
Ink
nite{can
nite{8_bit_synths}
mp3
C: |Users |admin|Music Inite{8_bit_synths} .mp3
main
input
source
debug: creating
demux:
access=' file'
demux='any
location=
IC: /User
nite{8_bit_synths}
#EXTINF
3545,nite{8_bit_synths}
C: |Users Iadmin |Music Inite{8_bit_synths}
mp3
#nite{cant_catch_
me}
nite{8_bit_synths}
mp3]


```
nite{cant_catch_me}
```