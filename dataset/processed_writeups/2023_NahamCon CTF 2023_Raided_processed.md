# Raided
> The police raided a server belonging to a very 1337 hax0r that was used to stage attacks. Upon further investigation, this server turned out to be a jump server for the attacker to access more infrastructure.

> A memory snapshot was taken of the machine. See if you can figure out what the attacker was doing and what other systems the hacker was accessing.

## About the Challenge
We've got a memory dump file, and if we check on the description of the chall. Looks like we need to find the attacker server

## How to Solve?
In this case, im only using `strings` and `grep`, First we need to find the attacker server by using this command

```shell
strings raided-challenge-dump-vmem | grep "ssh "
```


[Image extracted text: daffainfo@LAPTOP-F9L3RGSH =
$ strings raided-challenge-dump-vmem|
I(1h)
grep
"ssh
ssh
~1
~/  sshlid_ed25519 133t0167.172.12.154
ssh
Zi
~/ .sshlid_ed25519 133t016
orce ssh to
use IPv4 addresses only]
(-6)-4[force ssh to
use IPv4 addresses only]
(-4)-6[force ssh to
use IPv6 addresses only]
ca
ll_program macs ssh ~Q mac
cal
L_program ciphers ssh ~Q cipher
ssh
Zi
~] .ssh
id
133t@
usage
ssh [~46AaCfGgKkMNnqsTtVvXxYy]
[~B bind_interface]
RTUALssh
-i
~]  ssh/id_ed25519
133+@167.172.12.154
ssh
~1 ~I sshlid
ssh
Zi
~/ .sshlid_ed25519 133+0167.172.12.154
force ssh to
use IPv4 addresses only
force ssh to
use IPv6 addresses only
c+enocify
cck
croctam]
rath
o
Ccp
Command
Damoe]


The IP address of attacker server was `167.172.12.154` and the username was `l33t`. Now we need to find the private key using this command

```shell
cat raided-challenge-dump-vmem\ \(1\) | grep -Ei "BEGIN OPENSSH PRIVATE KEY-----" -a -A 7
```

This command will find a `BEGIN OPENSSH PRIVATE KEY-----` and then it will print 7 line after matched word


[Image extracted text: fD?DOHeHgeoMovoeT
TuolooDIBuoooDloo[jooIo?HoooooooHoHooHoooqjooHoHooHooobjooAoDlooollu:0 uYIo?HooleloogooHe
loooHoHooHoooviooAollo toHo-OODogoooHoHooHooovioooDloHo_oODoDoooHoooAooAoo@oO@oPOoPHo_Ho_
pvevve-=
BEGIN OPENSSH PRIVATE KEY
bzBLbnNzaClrZXktdjEAAAAABGSvbmUAAAAEbMguZQAAAAAAAAABAAAAMWAAAAtzc2gtZW
QyNTUXOQAAACDx5+PcHHdCbysQVTdmPbKydlqZBRe4OEhDOYoBDHZIKgAAAJBE8ISyRPNU
SgAAAAtzc2gtZWQyNTUxOQAAACDxS+PcHHdCbysQVTdmPbKydlqZBRe4OEhDOYoBDHZIKg
AAAEBFMHMBRmsUnpUBeiO9lvIYYjICQHypyprNdh9IOONK3fHn4gwcdOJvKxBVNZY9srJ3
WpkFFTg4SEPRigEMfYgqAAAACMWZM3RAaDR4MHIBAgM=
END OPENSSH PRIVATE
KEY-
poooUDLa ! @vallevoa !Lucida Sans Unicodel
p UDeooooU! Yudit Unicode@ovalpeeeoUDoPooooUdova
Kerkis
Te1 'Ulo#oooUDlooooooUooOlArmNet He]


Use that privkey and login to the server by using this command

```shell
ssh l33t@167.172.12.154 -i id_rsa
```


[Image extracted text: The authenticity
of host
167.172.12.154 (167.172.12.154)
can't
be established _
ED25519
fingerprint is SHA256:X/3QeCLYnvqvkr7RILeyzbViywdsUKuo8g+BVv3Xi68 _
This
is not known by any other
names
Are you
sure you want to cont-
connecting (yes/no/ [fingerprint])? yes
Warning
Permanently added
167.172.12.154' (ED25519) to the list of known hosts
{654e9dc4c424e25423c19cSe64fffb27}
Aennnnnt
t
En
7O
7n
DI
C7ccic
key
key
inue
flag]


```
flag{654e9dc4c424e25423c19c5e64fffb27}
```