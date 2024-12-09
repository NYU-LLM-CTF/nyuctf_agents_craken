# David Cicode 2/2
> You found David's gmail account in the first part of the challenge, let's see what informations you can recover from it.

> Flag format : dvCTF{part1_part2_part3}

## About the Challenge
We need to do an OSINT on david's gmail account (dav1d.c1cod3@gmail.com). You need to get the email first from `David Cicode 1/2`


[Image extracted text: origin_url
action_url
username_element
username_value
password_element
pas
Filter
Filter
Filter
Filter
Filter
Filter
https: | /www:youtube.com/
david.clcod3@gmail com
BLOL]


## How to Solve?
Usually to do OSINT on gmail, some people using tool called `GHunt`. But in this case i'll be using [Epieos](https://epieos.com/)


[Image extracted text: Google account finder will show you if the requested email
Google
is linked to
Google account
if the person left
reviews on Google Maps_
Query
davld.clcod3@gmailcom
Photo
Sign YP
Name
David Cicode
116570179360508069806
Last Update
Sign Up
Services
EaS
Google Maps
https:| [wwwgoogle comkmaps/contrib/116570179360508069806
Google Calendar
https:| calendargoogle com/calendar/u/o/embed?src-davldclcod3@gmailcom
andlor]


There are 2 services (Google Maps and Calendar). Check each service to get the flag

First I checked the Google Maps first and we will find the first part of the flag in the latest review


[Image extracted text: ALDI Nanterre
David Cicode
Photo
Dec 2022
LIVING ART
LIVING ART
Figurines de Noel
Figurines de Noel
metal
metal
86
Jou de
Uvctflet}_
ChaRIOT
20.23
ALDI Nanterre
6.00
27
DNTENELLES
ire des
Google
Image capture:Dec 2022
Images maybe subject t0 copyright
Indonesia
Terms
Privacy
Report _
problem
mathematques
CivNG
ART]


And then I checked on the google calendar service and we will find the second part of the flag (To get the flag check 14th February 2023)


[Image extracted text: VERY IMPORTANT
Restaurant
When
Tue, February 14, 8pm _
M1pm
Where
Ritz Palace (map)
Description
Reservation Code
PART 2 => cAN_b3_U53fU1 _
more_detailse copy_to my_calendad
8pm VERY IMPORTANT
Restaurant]


And if you check another calendar, you will get link about Google Groups named `David Cicode`. There are 2 conversations and to get the flag, check the latest conversations


[Image extracted text: 0
1 of 2
Hello guys, In March
wanted to organize an event on the Cyberpunk theme and create cool
challenges
voyag__@gmail com
Jan 19,2023,8.24.35PM
Hi David, This can be really cool:
have & few ideas in mind and Im preparing this for next
David Cicode
Jan 19,2023, 8.31.12PM
Oh great
TIl set up
meeting for us in
week Le
jeudi 19 janvier 2023
14.24.35 UTC+1,
mick___@gmail.com
Jan 19,2023, 8.40.06 PM
to David Cicode
sawyour guest for next weeks
meeting:
already have an idea for you:
For
challenge it would be necessary to use the different tools of Google (Drive; Mail, Agenda; Groups_) to put pieces of
And with that we'd have to find the accounts and rebuild the final
Can that be an idea?
For example:
Drive => A PDF with a flag
Mail => Hide a piece of the
in an email
Agenda
=>
Planning events
Groups
Send a piece of the
as: jYyMjk4NWRk}
flags:
flag:
flag
flag]


```
dvCTF{gHun7_c4N_b3_U53fU1_jYyMjk4NWRk}
```