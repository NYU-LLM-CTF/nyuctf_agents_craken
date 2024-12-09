# chrono
> How to automate tasks to run at intervals on linux servers?

## About the Challenge
We were given an access to SSH server and then we need to find the flag in the server

## How to Solve?
If we read the description of the flag, we can assume the flag was located on the cron file, so to solve this chall im using this command

```
cat /etc/cron*
```

This command will read any file that start with `cron`. And here is the output


[Image extracted text: picop
@challenge:~$
cat
letc/cron*
cat:
letc/cron-d: Is
directory
cat:
[etc/cron-daily:
Is
directory
cat:
letc/cron.hourly: Is
directory
cat:
[etc/cron-monthly: Is
directory
cat:
[etc/cron.weekly: Is
directory
picoCTF{SchBDULZNG_T4SK3
LINUX_5b7059d0}
layere]


```
picoCTF{Sch3DUL7NG_T45K3_L1NUX_5b7059d0}
```