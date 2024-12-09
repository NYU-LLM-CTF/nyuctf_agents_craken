# Restricted
> You 're still trying to collect information for your research on the alien relic. Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. The software containing all these memories seems to be running on a restricted environment which limits your access. Can you find a way to escape the restricted environment ?

## About the Challenge
We were given a source code (You can download the file [here](misc_restricted.zip)) that contains `sshd_config` and `bash_profile`

## How to Solve?
If we login normally using this command

```
ssh -p PORT restricted@IP
```

You still can get into the server, but there is some restriction (You can't use some commands, you can move into another directory, etc.)


[Image extracted text: permitted by applicable
law _
restricted@ng-restricted
-7b5f545587-pm2tv:~$
1s
~rbash:
ls:
command not
found
restricted@ng-restricted-thgsc-7b5f545587-pm2tv:~$
[home/restricted
restricted@ng-restricted-thgsc-7b5f545587-pmztv:~$
env
thgsc
pwd]


And to bypass this, Im using this [website](https://www.hackingarticles.in/multiple-methods-to-bypass-restricted-shell/) as a reference. Here is the command

```
ssh -p PORT restricted@IP -t "bash --noprofile" 
```


[Image extracted text: The authenticity
of host
[165.227.224.40]:31750 ([165.227.224.40]:31750)
can
be estal
ED25519
key
fingerprint is SHA256: cAQBhvlkikmVEqxHIApvLxteba/azXZqRPOkSv+ZWak_
This host
key is
known
by the following
other names
addresses
ssh/known_hosts
36: [hashed
name]
Are you
sure
you want to
continue
connecting (yes/no/ [fingerprint]) ?
yes
Warning=
Permanently added
[165.227.224.40]:31750
(ED25519) to the list of
known hosts
restricted@ng-restricted-ihelp-844c859d8f
77t5n:~$
15
restricted@ng-restricted-ihe7p-844c859d8f-77t5n:~$
15
~la
total 28
drwxr
xr-X 1 restricted restricted 4096 Mar 16 16:10
drwxr
xr-X 1
root
root
4096 Mar 16 16:10
rW-r--r-
restricted
restricted
220 Mar 16 16.10 .bash_logout
rwxr-Xr-X 1
root
root
15 Mar 15
21.39
bash_profile
rW-r--r-
restricted
restricted 3526 Mar 16 16:10
bashrc
drwxr
xr-X 1
restricted
restricted 4096 Mar 16 16:10
bin
rW-r-
restricted
restricted
807 Mar 16 16:10 .profile
restricted@ng-restricted-ihe7p-844c859d8f-77+5n:~$ sudo
bash:
command not
found
restricted@ng-restricted-iheZp
844c859d8f-77t5n:~$
cd
restricted@ng-restricted-ihe7p-844c859d8f-77+5n:/$
15
bin
dev
flag_8dpsy
lib
media
mnt
proc
run
Srv
tmpl
var
boot
etc
home
lib64
memories . dump
opt
root
sbin
Sys
usr
restricted@ng-restricted-ihe7p-844c859d8f-77+5n:/$ cat
8dpsy
HTB{r35trlctlOn5_4r3_pOw3r1355}
restricted@ng-restricted-iheZp
844c859d8f-77t5n:/$
sudo
flag]


```
HTB{r35tr1ct10n5_4r3_p0w3r1355}
```