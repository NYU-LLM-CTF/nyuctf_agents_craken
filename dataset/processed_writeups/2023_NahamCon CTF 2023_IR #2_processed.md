# IR #2
> Can you figure out how the malware got onto the system?

## About the Challenge
We have to find out how the malware can be downloaded

## How to Solve?
As you can see on the VM, the malware was located in `Downloads` folder


[Image extracted text: This PC
Downloads
Name
Date mo
Quick access
updates p:T
6/9/2023
Desktop
Download;
Documents
Picture;]


So I tried to check the browser download history and I got nothing, and then I tried to open the mail server on the VM, and I got 4 weird emails. 2 of them contain the flag


[Image extracted text: Searcn
Reply
Reply all
Forwara
Archii
Focused
Other
Updates to install
June 9
2023
NexGen Innovation <nexgeninnovation@outlook.com>
6/9/2023 12.52 PM
nexgeninnovation@outlook.com
To: nexgeninnovation@outlook.com
Updates to install
Fri 6/9
updates ps1
nexgeninnovation@outlook.com
File Type Not Supported
Hey therel Here are the requested upda
Fri 6/9
Hey therel
NexGen Innovation
Hey therel Here are the requested update
Sent
Here are the requested updates for your computer to keep it secure: Please download the file and run it:
If someone is
looking for
secret message, here it is ->
flag{75f086f265fff161f81874c6e97deeOc}
nexgeninnovation@outlook.com
test email
Fri 6/9
Regards_
This is the body of the email:
IT team
Microsoft Account
Confirmation: Your Microsoft account is   Fri 6/9
Your one account for all things Microso"
Outlook Team
Friday:-]


```
flag{75f086f265fff161f81874c6e97dee0c}
```