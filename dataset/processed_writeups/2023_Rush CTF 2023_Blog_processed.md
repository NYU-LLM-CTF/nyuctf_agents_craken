# Blog
> Hey what do you think about my blog?

## About the Challenge
We were given a plain website that contains a blog


[Image extracted text: Xtra
Bleg Home
Single Post
About Xtra
Contact Us
Xtra
is a
multi-purpose HTML template from Template_Mo website. Left side is a sticky menu bar: Right side content will scroll up and down:
Search
~Image
New
Simple
useful HTML layout
There is a clickable image with beautiful hover effect and active title link for each post item Left side is a sticky menu bar: Right side is a blog content that will scroll up and down:
Travel
Events June 24.2020
36 comments by Admin Nat
Hmage
New
Multi-pupose_bleg_template
Xtra
is a
multi-purpose HTML CSS template from TemplateMo website.
list, single post; about; contact pages are included. Left sidebar fixed width and content area is a fluid full-width
Blog
Blog
and
Bleg
Blog]


## How to Solve?
If we check one of the post, the endpoint will looks like this


[Image extracted text: Not secure
challs ctfcafe 5555/post php?page-post1.html
Xtra Blog
Bleg Home
Single Post
About Xtra
Contact Us
Xtra Blog is a multi-purpose HTML template from Template_Mo website. Left side is a sticky menu bar: Right side content will scroll
Search
Single Post of Hello World 123
June 16,2020 posted by Admin Nat
Hello World 123
Duis pretium efficitur QUnc. Mauris vehicula nibh nisi. Curabitur gravida neque dignissim; aliquet nulla sed, condimentum nulla. Pellel
aliquam ex vel lectus ornare tristique. Nunc et eros
enim feugiat tincidunt et vitae dui:
Creative . Design
Business
Design: TemplateMo
Copyright 2020 Xtra
Company Co. Ltd.
quis
Blog]


```
http://challs.ctf.cafe:5555/post.php?page=post1.html
```

So I tried to to change the `post1.html` value to another file, for example `/etc/passwd`.


[Image extracted text: Xtra
Blog Home
Single Post
About Xtra
Contact Us
Xtra Blog is a multi-purpose HTML template from Template_Wo website. Left side is a sticky menu bar: Right side content will scroll up and down:
Search_
Warning: include(  posts//etc passwd): failed to
stream: No such file o directory in Ivar/wwwlhtm]post:php o line 82
Warning: include(): Failed opening ' posts//etc passwd' for inclusion (include
{USI
/locaVlib php') in /varhwwwlhtm]post:php on line 82
Design: TemplateMo
Copyright 2020 Xtra Blog Company Co. Ltd.
Blog
open
path='_]


Unfortunately, we can't check the `passwd` file because we still inside the `posts` directory. We can use `../` or dot dot slash to go to `/` directory and then read the `passwd` file


[Image extracted text: 2 >
C
Not secure
challs ctfcafe 5555/post php?page=_
Jetc/passwd
Xtra Blog
Bleg Home
Single Post
About Xtra
Contact Us
Xtra Blog is a multi-purpose HTML template from Template_Wo website. Left side is a sticky menu bar: Right side content will scroll up and down.
Search
root:x:O:O root: root:/bin bash daemon:x:l:l:daemon: usr/sbin: usr/sbin/nologin bin:x:2:2:bin:/bin: uSE/sbin/nologin sys:x:3.3.sys:/dev: usr/sbin/nologin sync:x:4.65534:sync: bin:/bin/sync
games:x:S:60:games: uSr games: usr/sbin/nologin man:x:6:12:man: var/cache man: usr/sbin/nologin Ipx:7:7:lp: var/spool/lpd: usr/sbin/nologin mail:x:8:8:mail: var/mail: usr/sbin nologin
news:x:9:9 news: var/spoolnews: usr/sbin
Ynologin uucp:x:10:1O:uucp: var/spooluucp: usr/sbin/nologin proxyx:13:13:proxy:/bin: uS/sbin nologin WWW-data:x:33:33:WWW-data: var WWW: usr/sbin nologin
backupx:34.34:backup: var backups: usr/sbin/nologin list:x:38.38: Mailing List Manager: varllist: usc sbin nologin irc:39.39:ircd: var/run ircd: usr/sbin/nologin gnats:x:41:4]:Gnats Bug-Reporting System
(admin): var lib/gnats: usr/sbin/nologin nobody:x:65534.65534:nobody:/nonexistent: usr/sbin/nologin
apt:x:100.65534:/nonexistent: bin false RUSH{LFI_1S_SO_BZ_FOR_M3}
Design: TemplateMo
Copyright 2020 Xtra
Company Co Ltd.
Blog]


```
RUSH{LF1_1S_SO_3Z_F0R_M3}
```