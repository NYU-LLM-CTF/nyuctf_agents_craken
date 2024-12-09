# Windows Pane - 1
> Jubilife's information technology (IT) team has seen unusual login event activity and would like your help identifying any suspicious activity in the attached logs.

> Jubilife has a strict company policy that each employee is assigned a single device and unique user account, and is only permitted to access the network from their device.

> This policy is in place to help IT by limiting each user to only be logged into one device at any given time; therefore, no user can be logged in twice at the same time.

> What is the username of the account that is noncompliant with this company policy?

> Flag format: username of the noncompliant account. If the username is MARK_ZUCKER, the flag would be MARK_ZUCKER

## About the Challenge
We were given a CSV file (You can download the file [here](LogonEvents.csv)) that contains windows event logs. We need to find the username of the account that is noncompliant with the company policy


[Image extracted text: ICSJWG CTF 2023
Windows Pane
1 > @ LogonEvents csv
Fimecreated,Id,LevelDisplayName,Message,Source,Taskcategory
Username
1681731481,4624,Information,
An account
was successfully logged
on .
Subject:
Security
ID:
5-1-5-18
Account Name:
JUBI86597$
Account
Domain:
JUBILIFE
Logon ID:
OX6DZS6D
10
Logon Type=
12
Impersonation
Level:
Impersonation
13
14
New Logon:
15
Security
ID:
5-1-5-21-4223521121-1109782943-2127437603-1482
16
Account
Name :
FLORENCEEDWARDS
17
Account
Domain:
NT   AUTHORITY
18
Logon ID:
OX6DZS6D
19
Logon GUID:
B285EDFA-4370-45B6
B1ZA-4FAZ6E97410B
20
21
Process
Information:
22
Process
ID:
0x56
23
Process
Name :
C: IWindows | System32|svchost
exe
24
25
Network Information:
26
Workstation
Name
27
Source Network Address:
28
Source
Port:
29
30
Detailed Authentication Information:
Logon Process:
Kerberos
Authentication Package: Kerberos
2
Transited Services:
Package Name (NTLM only):
35
Key Length:
36
37
This event is generated when
session is created.
It is generated
on
the computer that Was accessed
logon]


## How to Solve?
If we check the company policy, there are some rules:
* Each employee is assigned a single device and unique user account
* Only permitted to access the network from their device.
* No user can be loged in twice at the same time

So, to find the suspicious user we need to find the user that breaks the company policy.

The idea is to find the users who logged in at the same time. By analyzing the Windows event logs, you can observe that the ID for a user logging into the server is `4634` whereas the ID for a user logging out from the server is `4624`. This is a normal user log:


[Image extracted text: 1681995967
4624 Information
C: Windows  System32 svchost exe
12544 ALBERTA
DUNN
1682029339 4634
Information
C:|Windows| System32|svchost exe
12545 ALBERTA_DUNN
1682084933
4624 Information
C:lWindows| System32lsvchost exe
12544 ALBERTA_DUNN
1682115105 4634 Information
C:|Windows| System32|svchost exe
12545 ALBERTA
DUNN]


Normally you will see the code is `4624` that means the user logged in, and then logged out, and so on.

I attempted to sort the usernames first. Upon reviewing the information for `ABIGAIL_FORBES`, I noticed that the code `4624` appeared twice, and the timestamps were very close to each other. So, I suspect that this user may be suspicious.

```
ABIGAIL_FORBES
```