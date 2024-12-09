# Zombie
> Oh, shoot, I could have sworn there was a flag here. Maybe it's still alive out there?

## About the Challenge

We given some machine and find the flag

## How to Solve

First we gonna look up the directory with `ls -la`

And you will find some interesting script


[Image extracted text: user@zombie:~$ 1s
user@zombie
~$ 15
la
total 24
drwxr
sr-X
user
user
4096 Jun 17 16:08
drwxr
Xr _
1 root
root
4096
Jun 14 17.52
rwxr
Xr -
user
user
3846 Jun 14 17.52
bashrc
rw-rr
user
user
17
Jun 14 17.52
profile
rwxr
Xr-X
root
root
131
Jun 14 17:52
user
entrypoint
sh
user@zombie
~$
cat
user-entrypoint.sh
#!/bin/bash
nohup tail
/home
/user/flag-txt >/dev/null 2281 & #
disown
rm
/hone
user/flag-txt 2,81
>[dev/null
bash
exituser@zombie:~$]


From that script, we analyzed the flag is already deleted, but we can use `ps aux` to see the process of script


[Image extracted text: usert
@zombie:~$
aux
PID
USER
TIME
COMMAND
root
0:00
lusr/sbingsshd
root
sshd:
user
[priv]
user
sshd
user@pts/o
10
user
user-entrypoin} /bin/bash
/home/user/
user
entrypoint.sh
11
user
tail
f /home/user/flag-txt
13
user
bash
20
user
0:00 pS
aux
usere
@zombie:~$]


After that we can see the process in `/proc/` directory


[Image extracted text: user@zombie: $ ls
~la
Iproc/11/fd
total
dr-X-
user
user
Jun
17 16:12
dr-xr-Xr-X
9 user
user
Jun
16:08
lr-X-
user
user
64
Jun
17 16:12
[devfnull
~WX
1 user
user
64
Jun
17 16:12 1
[dev/null
~WX
user
user
64
Jun
17 16:12 2
[dev/null
user
user
64
Jun
17 16:12 3
[home/user
txt (deleted)
usere
@zombie:~$
/flag]


Last we just can cat the flag with `cat /proc/PID/fd/numbers`


[Image extracted text: user@zombie:~$
Iproc/11/fd/3
{6387e800943b0b468c2622ff858bf744}
user@zombie:~$
cat
flag]


```
flag{6387e800943b0b468c2622ff858bf744}
```