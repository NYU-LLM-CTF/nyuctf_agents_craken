# my-chemical-romance
> When I was... a young boy... I made a "My Chemical Romance" fanpage!

## About the Challenge
We were given a website about My Chemical Romance

## How to Solve?
First if we check the response header, there is an interesting header:
```
Source-Control-Management-Type: Mercurial-SCM
```
And i think, this is source code exposure in `.hg` directory (You can check the reference [here](https://github.com/daffainfo/AllAboutBugBounty/blob/master/Exposed%20Source%20Code.md))

We need to dump it using this [tool](https://github.com/arthaud/hg-dumper), but the tool is broken and i still can get the sensitive file like `.hg/branch` or `.hg/requires`. And after I dump some file, I am using the `hg` command in Kali. First, I check using the `hg log` command and the result will be like this.


[Image extracted text: changeset:
1:3ecb3a79e255
tag:
Jser
bliutech <bensonhliu@gmail_
com>
Jate:
Fri Feb 10 06:50:48 2023
0800
summary:
Decided
to keep
my favorite
song
secret
changeset:
0:2445227b04cd
Jser:
bliutech <bensonhliu@gmail_
com>
Jate:
Fri Feb 10
06:49:48 2023
0800
summary:
I love
'My Chemical Romance
tip]


And then i run `hg up 2445227b04cd`. `hg up` is short for `hg update` and it is used to switch to a different version of a repository. In this case i update the repository to version `2445227b04cd`

And then there is a file named `gerard_way2021.py` and if we open the flag we can get the flag


[Image extracted text: from flask import Flask,
send_from_directory, Response
app
Flask(_
name
# FLAG: lactf{denT_6rInk_m3rCurlal_frem_8_flaSk}
@app.route('/')
@app.route( ' /<path:path>
def index(path-' index.html' ):
resp
send_from_directory( ' static
path)
resp.headers[
Source-Control-Management-Type' ]
'Mercurial-SCM'
return resp
@app.errorhandler(404)
def page_not_found(e)
return send_from_directory(' static
404.html' )]

```
lactf{d0nT_6r1nk_m3rCur1al_fr0m_8_f1aSk}
```