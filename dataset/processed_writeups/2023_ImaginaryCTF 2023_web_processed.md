# web
> We recovered this file from the disk of a potential threat actor. Can you find out what they were up to?

## About the Challenge
We got a zip file (You can download the file [here](web.zip)) and it contains a mozilla firefox data


[Image extracted text: Vame
Type
Compressed size
Password p=
8ubdbl3q default
File folder
Crash Reports
File folder
Pending Pings
File folder
profilesini
Configuration settings
No]


## How to Solve?
We need to import the data first in our mozilla, but how? First, access `C:\Users\test\AppData\Roaming\Mozilla\Firefox\Profiles` if you are using 


[Image extracted text: Name
Date mo
8ubdbl3q default
7/22/202
igj1ito3.default
6/5/2023
topypclm default-release
7/22/202]


And then copy `8ubdbl3q.default` into the `Profiles` folder, and then you need to adjust the profile name on `profile.ini` file, the file location is in `C:\Users\test\AppData\Roaming\Mozilla\Firefox\`


[Image extracted text: profilesini
File
Edit
View
[Install3o8046BOAF4A3ICB]
Default-Profiles/8ubdbl3q.default
Locked=1
[Profilel]
Name-default
IsRelative=1
Path-Profiles/8ubdbl3q.default
Default=1
[Profileo]
Name-default-release
IsRelative=1
Path-Profiles/8ubdbl3a.defaultl]


And then, open Mozilla and check the history browser by pressing `Ctrl + H`


[Image extracted text: History
Search history
View ~
This month
WWW.merriam-webster com/games/quordle/
chatgpt jailbreak - Google Search
ChatGPT-Dan-Jailbreakmd
GitHub
Firefox Privacy Notice
Mozilla
PALMS Backchannel Chat
The new alternative to Todaysmeet
PALMS Backchannel Chat
The new alternative to Todaysmeet
PALMS Backchannel Chat
The new alternative to Todaysmeet
Quordle
quordle
Google Search
wordle
Google Search
Wordle
The New York Times]


Hmm what is `PALMS Backchannel Chat`? Lets open the website


[Image extracted text: 6 7 6
8
https:/ /yoteachapp com /password/64ab3965b13dfb00148ea72f
Room: supersecrethackerhideout_
HOME
Please enter room entry password
For admin, please enter admin password
Go
Have a teacher account?
If you own this room; you may login before entering the rooml]


The room name was very suspicious and there was an autofill password. Login into the room using the password to obtain the flag


[Image extracted text: [*] Successl
root
15 days ago
[*]
found: ictf{behold_th3_forensics_g4untlet_827b3f13}
root
15
ago
[*] hacking
root
15 days ago
flag ~
days]


```
ictf{behold_th3_forensics_g4untlet_827b3f13}
```