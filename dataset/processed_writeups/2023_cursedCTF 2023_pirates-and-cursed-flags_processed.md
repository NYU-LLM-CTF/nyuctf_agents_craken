# pirates-and-cursed-flags
> Please don't steal our book. Only authorized users can open this.

## About the Challenge
We were given a html file (You can download the file [here](book.html)) and we need to find the flag there

## How to Solve?
If you check the source code of the website, we know the pin is `hunter2`


[Image extracted text: aocventlistener(
Sudmit
Tunction
(e,
preventDefault()
Secure
PIN
if
(document getElementById( "pin") _
value
hunter2")
document.getElementById
book
innerText
atob(book) ;
else
alert("
Incorrect
PIN
Please
again
");
try]


Now input `hunter2` in the form and we will obtain the flag


[Image extracted text: Enter PIN to proceed with DRM decryption:
Submit
Pirates
and
Cursed Flags
Ae 2023
CursedCTF
Organizers
All Rights
Reserved
All
material
appearing
below
is protected
copyright
under U.S_
Copyri
Organizers
You
may
not
copy _
reproduce_
distribute, publish,
display,
transmit,
in
any way
exploit
any
such
content
nor
may
yOu
distribute
including
local
area
network,
sell
or
offer it
for
sale,
use
such
may
not
alter
remove
any
copyright
other
notice
Copying
storing
Once
upon
time
in
world that
seamlessly blended
the high
seas
of
pirac
mysterious
group
of
pirates
roamed
the oceans, guided
unlike
any
terrible
curse:
cursedflag{did_
you_
know_that_hacking_is_illegal}
It
was
would
wield
unmatched
power
over
the digital
seas,
but
terrible
price
flag]


```
cursedflag{did_you_know_that_hacking_is_illegal}
```