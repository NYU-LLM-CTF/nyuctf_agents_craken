# vulpes-vulpes
> The red fox (Vulpes vulpes) is the largest of the true foxes and one of the most widely distributed members of the order Carnivora, being present across the entire Northern Hemisphere including most of North America, Europe and Asia, plus parts of North Africa. It is listed as least concern by the IUCN. Its range has increased alongside human expansion, having been introduced to Australia, where it is considered harmful to native mammals and bird populations. Due to its presence in Australia, it is included on the list of the "world's 100 worst invasive species".

## About the Challenge
We were given a `zip` file that contain about firefox data such as history browser, add-on mozilla, etc. (You can download the file [here](vulpes-vuples.zip))

## How to Solve?
We need to import the file first into

```
C:\Users\USERS\AppData\Roaming\Mozilla\Firefox\Profiles
```

And then you will see that there is some history in May, and there is also a Mozilla add-on called `Tampermonkey`


[Image extracted text: May
wwwgoogle com/url?sa=t&rct-j&q-&esrc=s&source=web&cd=&.
wwwgoogle com/url?sa=t&rct-j&q=&esrc=s&source=web&cd=&.
<New userscript>
<New userscript>
Cryptography for Absolute Beginners
by parserite
Medium
Defuse Security's Encrypted Pastebin
easy cryptography
Google Suche
easy cryptography
Google Suche
Encrypted Pastebin
Keep your data private and securel
Defuse
Firefox Privacy Notice
Mozilla
how to cryptography
Goog
Suche
Instal
ed Userscripts
Introduction to Cryptography: Simple Guide for Beginners
TheBes.
JuSt
moment_
Just
moment:
pastebin with encryption
Google Suche
W Substitution cipher
Wikipedia
tampermonkey
Google Suche
Tampermonkey
Holen Sie sich diese Erweiterung fur
Firefox]


You will notice there is a website called `defuse.ca`

```
https://defuse.ca/b/tpYyyE0Qgg04KNcjXTJBZc
```


[Image extracted text: Defuse Security's Pastebin
This post will be deleted in 16
Enter Password:
Decrypt
Post Without Password Encryption
Use shorter URL. Expire in
10 Days
Password:
Verify:
Encrypt & Post
Important Note: This page contains user-submitted content_
In no way is Defuse Security responsible for its contents_
information please report itto_US]


Enable the addon and then press `Fill Password` button


[Image extracted text: dela
Enabled
minute
Password Manager
Save Password
Fill Password
Find new scripts_
Create a new script__
Please send a donation
Utilities
Dashboard
Help | Changelog /00]


Then you need to press `Decrypt` button on the website to obtain the flag


[Image extracted text: Defuse Security's Pastebin
flag{dunning
kruger?_is_that
some_kind_
of_bird?}
[flag{dunning_kruger?_is_that
some_
kind
of_bird?}]


```
flag{dunning_kruger?_is_that_some_kind_of_bird?}
```