# Inspector Gadget
> While snooping around this website, inspector gadet lost parts of his flag. Can you help him find it?

## About the Challenge
We were given a website without any source code, and the flag has been split into 4 parts. We need to find all of them

## How to Solve?
* Part 1/4:

We can find this in one of the hyperlink (/gadgetmag.html)


[Image extracted text: view-source:https:[linspector-gadget chal nbctf com/gadgetmag html
Line wrap
<!DOCTYPE html>
<html Lang-"en">
<head>
<meta
charset="UTF-8">
<meta
name=
viewport"
content-"width-device-width,
initial-scale-1.0">
<title-Flag
Part 1/4:nbctf{Go0d_</title>
<link
rel-"preconnect"
href_"https:
fonts_googleapis_com'
<link
rel-"preconnect
href_"https:
fonts_gstatic_com
crossorigin>
<link href-"httpsiL
fonts_googleapis_
COmLcss22-
family_RobotosdisplayzSwap'
<stvle>]


* Part 2/4:

There's a hidden file called `supersecrettopsecret.txt` inside `getFlag()` function


[Image extracted text: 0pr"9449  479I, -799
AE nienin
window. location.href_"gadgetmag.html"
f
function opengadgetphone() {
window. location.href-"gadgetphone.html"
f
function getflag() {
window. location.href-"supersecrettopsecret.txt"
}
<lscript>
Ihead>]



[Image extracted text: 0=
E0
inspector-gadget chal nbctf comgsupersecrettopsecret txt
Flag
Part 2/4:
J06_]

* Part 3/4:

We can find this in the homepage


[Image extracted text: on
class-"blue largetext">
1-Greetings
Dr Claw!</hl>
mg
src-"Krooter Gadget_jpg"
alt-"Flag Part
3/4:
D3tectlv3_
>We
ve
found
tons
of
information about
your archnemisis, Inspector Gadget
utton
onclick-"openotherpage( ) ">Introduction</button>
ion>
on
clace="red">]


* Part 4/4:

There's a new file called `/mysecretfiles.html` inside `robots.txt`


[Image extracted text: E0
inspector-gadget chal nbctf comgmysecretfiles html
You found my secret pagel
Here's part of the
for
troubles,
4/4 G4dg3t352}
filag
part
your]


```
nbctf{G00d_J06_D3tect1v3_G4dg3t352}
```