# Bad Waf No Donut
> I made a simple little backdoor into my network to test some things. Let me know if you find any problems with it.

## About the Challenge
We were given a very simple website without any source code, here is the preview of the website


[Image extracted text: < 
C
nessus-badwaf_chalsio
We 1 € ome !
Please select an option:
Explore
Render site
Check connection]


## How to Solve?
At first i went to `/explore` endpoint and in the source there are another endpoint called `/secrets`


[Image extracted text: ( >
C
view-source https [ /nessus-badwafchals io/explore
Line
wrap
<html>
<body>
<hlExplore< /hl>
<div
id=
content
<div>
<[body>
<script>
function isAdmin( )
let
ookie
decodeURIComponent(document
cookie) ;
let
cookie_values
cookie.split(';');
for(let
0; i
<cookie_values.length; i++)
let
cookie_values[i];
while
(c.charAt(0)
substring(1);
(c.indexOf ( "admin" )
if
(c.substring(name.length,
C.length) .indexof(
true") )
return true;
return false;
if (isAdmin()) {
document getElementById( "content
innerHTML
href=" / secrets
>secretsk/a>
else
document.getElementById( "content
innerHTML
<ulx<lixa
href=" /books
>books< /a></lix<lixa
<[script>
<intm>]


In the `/secrets` endpoint there is a HTML comment tells us to use `POST` method with `secret_name` as a parameter


[Image extracted text: 7
C
0 view-sourcehttps:| /nessus-badwaf chals io/secrets
Line
wrap
<html>
<body>
<h1,6000000</hl>
<p>I
only
Know
one
secret,
but
you
Know
how
to
ask.< /p>
asking
with
secret_
name
post parameter
<[body>
<html>
gotta
<i-=
Try]


When I tried to send a `POST` request with `secret_name` as parameter, the reseponse was a little bit weird


[Image extracted text: daffainfo@dapos:
$
curl
~XPOST "https:
Inessus-badwaf.chals.io/secrets"
~d
secret
name-flag"
You know what
to ask for
but
you
re
not
asking correctly.daffainfo@dapos
$]


What does it mean? And then i tried to go back to the homepage and I found a werird things


[Image extracted text: <html>
<body>
<hlxW e 1
C ome
<[hl>
<h2>Please
select
an
option : < /h2>
<u1>
<lix<a
href=" Lexplore
>Explore< /ax<[li>
<lixka
href=
[render
>Rencer
site</a></li>
<lix<a
href=
Lping?hostzgoegle
com
>Check
connection< /a></li>
<Jul>
</body>
<fhtml>]


Why this website uses a unicode as a font? That means we need to use unicode to in `secret_name` parameter? Hmm, let's try to change the `flag` string using gothic font


[Image extracted text: daffainfo@dapos
$
curl "https
Inessus-badwaf
chals.io/secrets
~h
"Cookie:
admin-true
~d
"secret_name=f
{hOw_dOes_this_even_WOrk}daffainfo@dapos
$
Iag'
flag]


```
flag{h0w_d0es_this_even_w0rk}
```