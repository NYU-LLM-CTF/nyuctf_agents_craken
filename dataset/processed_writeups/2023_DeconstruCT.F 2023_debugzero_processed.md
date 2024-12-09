# debugzero
> Someone on the dev team fat fingered their keyboard, and deployed the wrong app to production. Try and find what went wrong. The flag is in a file called "flag.txt"

## About the Challenge
We got a very simple website (And also there is no source code for this chall)


[Image extracted text: ch27524130614.cheng_
run
This website is currently under
development]


## How to Solve?
First, let's analyze the homepage.


[Image extracted text: Line
wrap
< #DOCTYPE
htmly
<html lang=
en"
<head>
<meta
charset="UTF - 8
<meta
http-equiv="X-UA-Compatible'
content="IE=edge'
<meta
name=
viewport
content=
width-device-width,
initial-scale=l.0'
<title Todo
List</title>
CSS
only
<link
href=
httpsi Lkcdn_jsdelivr_net Inpm/bootstrap@5_2_0-betalldistless[bootstrap_min_css"
rel=
stylesheet
integrity=
sha384-8evHe/X+RZYkIZDRvuzKMRqM+OrBnVFBL6DOitfPriatjfHxaWutUpFmBpAvmVor
crossorigin="anonymous
<! --
JavaScript
Bundle
with Popper
(script
src=
httpsi LLcdn_jsdelivr
[npnLbootstrap@5
0-betalLdistLjsLbootstrap_bundle_min_js"
integrity=
sha384-pprn3073KE6tlbbjs2QrFaJGz5_
SUsLqktiwsUTFSSJfv3qYSDhgCecCxMWSZnD2
crossorigin=
anonymous
x[script>
<link rel="stylesheet
href=
staticLstyles_Css
</head>
<body>
<div
class=
container
<hl This website
1s
currently under
<i>development< /i></hl>
<div>
</body>
<! --
John,
please
don
run the
app in
how
many
times
do
have
to tell
you this!
<fhtml>
<k~-
4net
debug
mode,]


There is a HTML comment, that caught my interest

```html
<!-- John, please don't run the app in debug mode, how many times do I have to tell you this! -->
```

This website was running in debug mode, but we still didn't know about the technology behind it. Then, I decided to try some of the common endpoints, such as `/robots.txt`, `sitemap.xml`, `/console`, `/admin`, etc. And voilà, there was an endpoint called `/console`


[Image extracted text: 6 >
C
ch27524130614.cheng run/console
Interactive Console
In this console you can
namespace wa
created by the debugger
Console Locked
[console ready]
The console is locked and needs to be unlocked by
entering the PIN. You can find the PIN printed out on
the standard output of your shell that runs the
server_
ACNOTeOCe
PIN
Confirm Pin]


But we need to know the PIN code first to use the Werkzeug console. Now, let's get back to the homepage again. You will see there is a CSS file.


[Image extracted text: < >
C
ch27524130614.cheng-run/static/styles:
CSS
Nothing
interesting
here
except
this
number
934123]


934123? Is that a PIN code? As it turned out to be true, that number is the PIN code! Now, we need to open `flag.txt` to obtain the flag. In this case im gonna use `open()`


[Image extracted text: Interactive Console
In this console you can execute Python expressions in the context of the
[console ready]
>> open( "flag txt").read()
dsc{p1zz4_15_
4w350m3 } In
>> >]


```
dsc{p1zz4_15_4w350m3}
```