# The Vault of Asgaard
> The flag used to fly high in the morning light, but the undead (bots) kept trying to steal it. Now we keep it in the vault of Asgaard itself! No undead fiends dare pass the test at the gates.

## About the Challenge
We were given a website that contain a login form and a captcha


[Image extracted text: The Vault
Enter Login Details
user
***
Solves remaining: 50
2 8 D
Check captcha
Login]


## How to Solve?
If we see a login form, the first thing that we need to test is SQL injection. So i inputted `' or true-- -` in the username but I can't click `Login` button because there is a captcha


[Image extracted text: <form action=" /login" method-"post" >
(div class="
mb-4
text-1g W-full">@</div>
(div class=
mb-4
text-1g W-full" @</div>
(div>
<{div>
The Vault
(div
class=
flex
flex-row
flex-nowrap justify-center
U-min'
<ldiv>
Tlex
(div
class="W-full">
<idiv>
Enter Login Details
(div
class=
mt-8 flex justify-center text-lg
text-black'
<button disabled id="login_button
class=
rounded-3xl
bg-blue
100
opacity-50 pX-18
text-white
shadow-xl backdrop-blur-md
transi
ion-colors duration-380
hover: bg-blue
480"> Login</button>
user
</div>
{form}
button#login
button rounded-3xlbg-blue-1OO.bg-opacity-
10.py-Z.text-white shadow-xlba
****
dlisabl
Cancel
Styles
Computed
Layout
Event Listeners
DOM Breakpoints
Properties
Accessibility
Solves remaining: 50
Filter
hov
cls
element-style {
2 8D
curation-303
e9248505
CsS
tnansition
dunarion
Console
What's New
Issues
Network conditions
Check captcha
Highlights from the Chrome 111 update
Automatic in place pretty print
The Sources pane
now
Login
automatically pretty-prints
minified source files in place
Enhanced UX in managing
new
PY - 2
50.px-'
flag,]


To bypass the captcha, as you can see in the inspect element tab. There is a `disabled` attribute on the button. Remove that attribute so now we can login without captcha check


[Image extracted text: <div class="mb-
flex flex-col items
center'
</div>
Flex
form action=" /login
method="post
<div
class=
mb-4 text-1g W-full" e</div>
<div class=
mb-4
text-1g W-full">
<{div>
<div>
<{div>
The Vault
<div
class=
flex flex-row flex-nowrap justify-center W-min"
<ldiv>
Tlex
<div
class="W-full">
<idiv>
Enter Login Details
<div
class=
mt-8
flex justify-center
text-lg
text-black" >
fley
(button
id=
login_button'
class="rounded-
3x1
bg-blue-100 bg-opacity
50 pX-10 py-2
text-White shadow-xl backdrop
blur-md
transition-colo
duration-308
hover:bg-
blue
480">Login</button>
or true-
</div>
4form}
button#login_button rounded-3xlbg-blue-
1O0.bg-opacity-
10.py-Z.text-white shadow-xlbac
dlisabl
Cancel
Styles
Computed
Layout
Event Listeners
DOM Breakpoints
Properties
Accessibility
Solves remaining: 50
Filter
:hov
cls
element-style
0
8D)
curation-388
flag.e9248505
CSS
tnansition-dunation=
Console
What's New
Issues
Network conditions
Check captcha
Highlights from the Chrome 111 update
Automatic in place pretty print
The Sources panel now
Login
automatically pretty-prints
minified source files in place;
Enhanced UX in managing
new
breakpoints
-50.pX-]



[Image extracted text: vikeCTF{OnIy_7h3_wOrZhy_m@y_p@55}]


```
vikeCTF{0n1y_7h3_w0r7hy_m@y_p@55}
```