# Simple Web
> It consists of only eight commands, each represented by a single character, and uses a tape-based memory model with a pointer. However, it is considered difficult to write programs in, as it provides very little abstraction over the machine model and requires one to break problems down into very simple steps.

## About the Challenge
We are given a zip code that contain HTML file inside of it


[Image extracted text: Task-www.zip (evaluation copy)
File
Commands
Tools
Favorites
Options
Help
(: 31
Add
Extract To
Test
View
Delete
Find
Wizard
Task-wwwzip
ZIP archive; unpacked size 347 bytes
Name
Task-WWW-indexhtml]


## How to Solve?
If we open the HTML file and check the source code, you will found `brainfuck` language


[Image extracted text: Line
wrap
<html>
<head>
<meta
equiv=
refresh
WWW-Authenticate=
~-[----->+<]>---.-[--->+<]s+++.---[->+++<]>.+++
sop=
WWW-Authenticate
</head>
<body>
<hl>Redirecting
in
seconds _
<fhl>
/body>
<fhtml>
http]


And if you decode it, you will get the flag

```
cyberthon
```