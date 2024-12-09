# Paper? Digital? same diff to me

> Two of our members, Simon and Anna were arguing about where's better to take notes.

> Simon thinks that Github isn't the best place to take your notes because you might leave something public behind by accident, like maybe a note about someone you didn't want public.

> Anna disagrees because you can just delete it and recommit anyway, and it looks good to be active on Github!

> Simon reminded them that we can see the changes... even what they wrote about Tom.

> Anna rushed off, but now we're not sure what they're talking about. Could you figure it out?

## About the Challenge
We need to find the flag by doing an OSINT

## How to Solve?
In the description it stated we need to find the flag on GitHub. First I went to [NJITCC GitHub](https://github.com/NJITICC) and then in the `People` section there are 2 members


[Image extracted text: People
Report abuse]


I check `AlfredSimpson` account first but I found nothing. And then I decided to check the account and that account just have 1 repository named `AdvancedEncryptionsNotes`


[Image extracted text: A AnnaCircoh
AdvancedEncryptionsNotes
Public
Watch
Fork
Star
Code
Issues
82  Pull requests
Actions
Projects
Security
Insights
main
branch
tags
Go to file
Add file
Code
About
No description; website, or topics provided
AnnaCircoh
Adding types of cryptanalytic attacks
f4fde0z
2 weeks ago
5 commits
Readme
Chapter INotesmd
Adding types of cryptanalytic attacks
2 weeks ago
stars
2 watching
READMEmd
Update READMEmd
2 weeks ago
forks
READMEmd
Releases
AdvancedEncryptionsNotes
No releases published
Just using this to take notes about advanced encryption algorithms; cryptography; and things like that!
Packages
No packages published]


I checked the commits list and there is a flag in 1 of the commits

https://github.com/AnnaCircoh/AdvancedEncryptionsNotes/commit/5937685a0a9e0a42563279a5198574cac1b04a7c


[Image extracted text: Cipner
Luld _
Enc  }plsiuec  JpLs
DIUL ?,
TonMally
04 D1 S
LIE
031n8
IUL
Note:
wonder hOW much will change When quantum releases?
Examples
What if
wanted
to encrypt tOm_is_@cting_W3ird
because he is.
How could I
Guess
that
covered later_
ents on commit 5937685]


```
nicc{t0m_is_@cting_w3ird}
```