# Red Team Activity 4
> Q4: Which binary (full path to binary) was modified by redteam to later escalate privileges?

> Note: Flag format is RS{MD5sum(<answer string>)}

## About the Challenge
We were given a log file (You can download the file [here](auth.log)) and we need to find the binary files to do privilege escalation

## How to Solve?
To do this, I attempted to search the log file using the keyword `su redteam` to find the `redteam` user first


[Image extracted text: pts/3
(o/root) uid:root(0)/root(0)
cwd: /root ]
su redteam
uid-0
pts_
(o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
bash
pts_
o/root) uid:redteam(
001)
/redteam(1001)
CWd
Troot ]
groups
pts
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
lesspipe
pts
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
basename
[usr/bin/lesspipe
pts
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
dirname /usr/bin/lesspipe
pts
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
dircolors
~b
pts_
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
cat /var/log/auth_
tmx
o/root)
uid
root
Iroot(0)
CWd
Iroot]:
lusr/
'lib/x86
64-linux-gnufutempter/utempter add
tmux ( 2392)
pts_
o/root)
uid:root
Iroot
cwd: /root ]
groups
pts_
o/root) uid:root 
o)/root
cwd: /root ]
lusr/bin/locale-check
C.UTF
pts
o/root) uid:root
0)/root(0 
cwd: /root ]
locale
pts
o/root) uid:root
0)/root(0 
cwd: /root ]
lesspipe
pts
o/root) uid:root
0)/root(0 
cwd: /root ]
basename
usr/bin/lesspipe
pts
o/root) uid:root
0)/root(0 
cwd: /root ]
dirname
[usr/bin/lesspipe
pts_
o/root)
uid:root(0
Iroot (0_
CWd
Troot ]
dircolors
~b
pts/4
o/root)
uid:root(0
Iroot(0
cwd: /root ]
mesg
by (uid-0)
(none) / (none) ) uid:root(0)/root(0_
Cwd: / ]:
run
parts
~report /etc/cron.hourly
pts
o/root) uid:root(0)/root(0)
cWd: /root]: cat Ivar/log/auth.log
pts
o/root) uid:redteam(1001) /redteam(1001_
cwd: /root]
whoami
pts
o/root) uid:redteam(1001) /redteam(1001)
cwd: /root]
id
pts_
o/root) uid:redteam(1001) /redteam(
001
cwd: /root]
ls
color-auto -la /usr/bin/find
pts/3
(o/root) uid:redteam(1001) /redteam(1001_
cwd: /root]
find
exec /bin/sh -p
quit
pts_
o/root) uid:root
0)/root(0 
cwd: /root ]
vim /var/log/auth 
(none
(none)
uid root(o)/root(0
CWd: /1.
Ibin /mount hugetIbfs Idev/hugenages
t hugetlbfs
log
log]


As you can see before `redteam` user became `root` that user running this command

```shell
find . -exec /bin/sh -p ; quit
```

If we check on [GTFOBins](https://gtfobins.github.io/gtfobins/find/). That command used to spawn shell or to do privilege escalation. Before `root` user login to as `redteam` that user change the SUID permission so non-root user such as `redteam` can use that file to do privilege escalation


[Image extracted text: t) uid:root(0)/root(0)
cwd: /root ]
nscd
1 paSswd
t) uid:root(0)/root(0_
cwd: /root ]
sss cache
~U
t) uid:root(0)/root(0_
cwd: /root ]
chmod
U+s /usr/bingfind
t) uid:root(0)/root(0_
cwd: /root ]
su redteam]


Hash the binary name using `md5sum`. Here is the command

```shell
echo -n /usr/bin/find | md5sum
```

And then wrap the output with `RS{.*}`

```
RS{7fd5884f493f4aaf96abee286ee04120}
```