# warmup
> My first flask app, I hope you like it

## About the Challenge
We were given a website without the source code


[Image extracted text: 6 >
Not secure
ctfbOIlerscom:5115/aWSkZXguaHRtbA==
Hello World?]


## How to Solve?
If we check the source, code there is another endpoint called `debug.html`


[Image extracted text: <hlxHello
World!< /hl>
</body>
<script>
console.log("")
<[script>
<! -=
html
<fhtml>
debug]


And if we decode `aW5kZXguaHRtbA==` we will get `index.html`. Now change it from `index.html` to `debug.html` and encode it with `base64`


[Image extracted text: < 
C
Not secure
ctfbO1lers com:5115/ZGVidWcuaHRtbA==
rendering for flask app:py
testing -]


Now we got another file called `app.py`. Now, try to access app.py endpoint (Dont forget to encode the name again)


[Image extracted text: 7
C
Not secure
view-source:ctfbOIlerscom 5115/YXBwLnBS
Line
wrap
from base64
import
b64decode
import
flask
app
flask.Flask(_
name_
@app
route(
[<name>
def
index2
name
name
b64decode(name
if
(validate(name)
return "This
file
is blocked
try:
file
open (name_
r' ) .read()
except:
return
"File Not
Found"
return
file
@app.route( ' /')
def index()
return
flask.redirect(
aWSkZXguaHRtbA==
def
validate(data):
if
data
b 'flag.txt
return
True
return
False
name_
main__
app.run( )]


As you can see the flag was located in `flag.txt` endpoint. But we can't access it directly because there is a function called `validate` to detect if our input is `flag.txt` or not

```python
def validate(data):
    if data == b'flag.txt':
        return True
    return False
```

To bypass that, we need to add `./` on the endpoint. For example from `flag.txt` to `./flag.txt`. And then repeat then encode the endpoint again with `base64` and you will get the flag


[Image extracted text: Not secure
ctfbO1lerscom 5115/Li9mbGFnLnRAdA==
bctf{h4d_
fun
wlth_my_I4st_mnlnut3_WArmuP????!}]


```
bctf{h4d_fun_w1th_my_l4st_m1nut3_w4rmuP????!}
```