# Red Team Activity 1
> Q1: what was the script name that was dropped?

> Note: Flag format is RS{MD5sum(<answer string>)}

## About the Challenge
We were given a log file (You can download the file [here](auth.log)) and we need to find the script name

## How to Solve?
To do this, I attempted to search the log file using the keyword `.sh`, and discovered a strange script named `_script2980.sh`.


[Image extracted text: = authlog
Hlat
lesspipe
ab
? of 13
basename
lusr_
~/bin/lesspipe
dirname
usr/bin/lesspipe
dircolors
mesg
lusr/lib/x86
64-linux-gnu/utempter/utempter del
1s
color-auto
ssh]:
ls
color-auto
ssh] 
vim authorized_keys
ssh] 
cat
Ivar/log/auth.log
ssh]:
cat
Ivar/log/auth.-
ssh]
vim
Idev/shm/_script2980.shl
ssh]:
cat
Ivar/log/auth_
ssh]
vim
lusr/lib/systemd/system/bluetoothd. service
ssh]
systemctl enable bluetoothd
service
ssh]e
cat /var/log/auth.log
ssh]e
apt install apachez
CckI
Ilincl
Jecrlinlonan
Lucrilin
aduice
Ttt
frem
Mdcnul
1og
log
Icnan
ant]


Hash the script name using `md5sum`. Here is the command

```shell
echo -n _script2980.sh | md5sum
```

And then wrap the output with `RS{.*}`

```
RS{5d8b854103d79677b911a1a316284128}
```