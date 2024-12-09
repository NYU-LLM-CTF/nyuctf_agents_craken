# The Sender Conundrum
> Marcus Got a Mysterious mail promising a flag if he could crack the password to the file.

## About the Challenge
We were given an email file (You can download the file [here](TheEmail.eml)) and a password protected zip file (You can download the file [here](unzipme.zip)). We need to know the password of the zip to obtain the flag


[Image extracted text: test
The Wizard <noreply@anonymousemail.me>
TW
3/28/2023 10.30 PM
To: marcus49@
gmail.com
Hello Marcus Cooper,
You are one step behind from finding your
Here is a Riddle:
am
noun and not
verb or an adverb.
am given to you at birth and never taken away,
You keep me until you die,
come what may_
What am I?
flag:]


[Image extracted text: Name
Size
Pac
flag txt
Enter password
Enter password for the encrypted file
C:lUsers MUHAMM~1 AppData Locall Temp RarsDIb249__. flag.txt
in archive unzipme.zip
Enter password
Show password
Use for all archives
Organize passwords__
Cancel
Help]


## How to Solve?
As you can see there is a riddle inside the email, solve it to get the flag. But in this case I will brute the zip file using `JohnTheRipper`. Here is the command I used

```
zip2john unzipme.zip > hash.txt
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```

And then check the password by running this command
```
john --show hash.txt
```


[Image extracted text: kaliokali)-[~/Desktop]
john
show hashz
txt
unzipme
zip/unzipme/
txt:BrandonLee:unzipme_
txt:unzipme
zip
unzipme
zip
flag.
flag.]


The password is `BrandonLee`. Open the zip file again and input the password to read the flag

```
vishwaCTF{1d3n7i7y_7h3f7_is_n0t_4_j0k3}
```