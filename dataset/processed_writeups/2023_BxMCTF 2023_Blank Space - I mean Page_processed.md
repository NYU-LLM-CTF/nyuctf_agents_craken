# Blank Space - I mean Page
> Have fun finding the flag…regardless if you're capable of solving CAPTCHAs or not.

> https://bxmweb1.jonathanw.dev/

## About the Challenge
We were given a very simple website


[Image extracted text: 7
view-
source https:/ /bxmweb1 jonathanwdev
Line
wrap
< !DOCTYPE
html?
<html>
<head>
<title Welcome
the website</title>
</head>
<body>
</body>
<html>]


## How to Solve?
As usual, im gonna check some interesting endpoints first such as `robots.txt` or `sitemap.xml`. And this website have a `robots.txt` file


[Image extracted text: 2 
bxmweb1 jonathanwdev/robotstxt
User-agent:
Disallow:
[very-secretly-hidden]


Now, we need to access `/very-secretly-hidden` endpoint to obtain the flag


[Image extracted text: 6 
bxmweb1jonathanwdev/very-secretly-hidden/
ctf{sdh57349857243fkhkwAklkAH}]


```
ctf{sdh57349857243fkhkwAklkAH}
```