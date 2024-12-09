# Red Team Activity 2
> Q2: Name of the malicious service?

> Note: Flag format is RS{MD5sum(<answer string>)}

## About the Challenge
We were given a log file (You can download the file [here](auth.log)) and we need to find the malicious service

## How to Solve?
To do this, I attempted to search the log file using the keyword `.service`, and discovered a strange service named `bluetoothd.service`

That's because there is a `vim` command executed before enable the service, So the user creating `bluetoothd.service` in the `/usr/lib/systemd/system/` directory to convince that is a legit service.


[Image extracted text: = auth log
rlbin/ locale-check
C.UTF- 8
ale
service
Aa ab ,
13 of 110
1 + = *
spipe
ename
~/bin/lesspipe
name
usr/bin/lesspipe
colors
~b
Ilib/x86
64-linux-gnu/utempter/utempter del
color-auto
ls
color-auto
vim authorized_keys
cat /var/log/auth_
cat
Ivar/log/auth
vim /dev/shm/_script2980.sh
cat
Ivar/log/auth.
vim
lusr/lib/systemd/ system/bluetoothd_
service
systemctl enable bluetoothd
service
cat
~/log/auth.log
install
anache?
lusre
1og
log
log
Ivare
ant]


Hash the service name using `md5sum`. Here is the command

```shell
echo -n bluetoothd.service | md5sum
```

And then wrap the output with `RS{.*}`

```
RS{a9f8f8a0abe37193f5b136a0d9c3d869}
```