# Glasses
> Everything is blurry, I think I need glasses!

## About the Challenge
We've got a simple website like this and inside the website there is an obfuscated javascript


[Image extracted text: Cart
Glasses
Purchase
SKU: BST-1337
Dark Frame Glasses
5250.88 $224.00
Cant see things because
are too blurry? Is your vision
and
everything looks like this?
Test your vision with glasses! Try on this pair and see if you can see the
previous sample text.
you might find a lot of value! Imagine the world
where you can see
clearlyl
Now
Buy
they -
foggy;
Buy]


## How to Solve?
To solve this chall, we need to open `inspect element` and then find the flag below `<em>this?</em>` tag HTML


[Image extracted text: <html lang=
<head>
<lhead>
<body>
<! -- Navigation-
{nav
class=
navbar
navbar
expand-lg navbar-light bg-light">
<lnav>
<1-- Product
section-->
<section class="py-5"
(div class_"container pX-4 pX-lg-5
(div
class=
roul
gX-lg-5 align-items-center
<div
class=
col-md-6" >
(ldiv>
<div class=
col-md-6
(div class=" small
mb-1">SKU: BST-1337</div>
<hl
class-"display-5
fij-bolder
~Dark Frame
Glasses</hl>
(div class-"fs-5 mb-5"_
({div>
<p class="lead"-
Can't
see things because they are
too blurry?
your vision
and
everything looks like
<em>this?</em>
<span style=
color:
transparent;text-shadou:
Spx rgba(0,0,8,8.89);text
decoration:
line-through;
flagKR8084e4530cf649814456f2a291eb81e97_
<ispan>
<br>
Test
your vision with glasses!
Try
this pair
and
see if YOU
can see
tnc
nncutouc
Onnt
TevI
vcm
miont
Tind
TOt
i2
Tmacin
tns
div containerpx-4.px-Ig-S.my-5
div row gx-4.gx-Ig-5.align-items-center
div col-md-6
plead
my -5" >
gX-4
foggy ,]


```
flag{8084e4530cf649814456f2a291eb81e9}
```