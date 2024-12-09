# secure router
> My friend bought this router. I want to hack into it so bad.

> The firmware for the router is online. There's gotta be bugs in it...

## About the Challenge
We were given a website and also a squashfs filesystem


[Image extracted text: Username:
Password:
Submit]



[Image extracted text: root@ubuntu-s-Ivcpu-Zgb-sgpl-01:~/_secure_router.bin.extracted/squashfs-root#
1s
~la
total
84
drwxr-Xr-X
21
root
root
4096
Nov
25
2016
drwxr-Xr-X
root
root
4096
Dec
15
09:16
drwxr-Xr-X
root
root
4096
Dec
15 09:16 bin
drwxr-Xr-X
2
root
root
4096
Nov
25
2016
boot
drwxr-Xr-X
root
root
4096
Dec
15
09:16
dev
drwxr-Xr-X
85
root
root
4096
Dec
15
09:16
etc
drwxr-Xr-X
3
root
root
4096
Nov
25
2016
home
drwxr-Xr-X
16
root
root
4096
Dec
15
09:16
lib
drwx_
root
root
4096
Nov
25
2016
lost+found
drwxr-Xr-X
2
root
root
4096
Nov
25
2016 media
drwxr-Xr-X
2
root
root
4096
Nov
25
2016
mnt
drwxr-Xr-X
3
root
root
4096
Nov
25
2016
opt
drwxr-Xr-X
2
root
root
4096
Jan
2015
proc
drwx____
2
root
root
4096
Feb
3
2017
root
drwxr-Xr-X
5
root
root
4096
Nov
25
2016
run
drwxr-Xr-X
root
root
4096
Dec
15
09:16
sbin
drwxr-Xr-X
2
root
root
4096
Nov
25
2016
srv
drwxr-Xr-X
2
root
root
4096
Apr
12
2015
SyS
drwxrwxrwt
root
root
4096
Feb
3
2017
tmpl
drwxr-Xr-X
10
root
root
4096
Nov
25
2016
usr
drwxr-Xr-X
12
root
root
4096
Dec
15
09:16
var]


## How to Solve?
There are 5 perl code in `var/www/` directory


[Image extracted text: root@ubuntu-s-Ivcpu-2gb-sgpl-01:~/_secure_router.bin.extracted/squashfs-root/var
WWW#
1s
~la
total
28
drwxr-Xr-X
root
root
4096
Feb
3
2017
drwxr-Xr-X
12
root
root
4096
Dec
15
09:16
~rwXr-Xr-X
daffa
daffa
1971
Feb
3
2017 MCU_check_serial.pl
~rwXr-Xr-X
daffa
daffa
1924
Feb
2017
MCU_recover_credentials.pl
~rwXr-Xr-X
daffa
daffa
917
Feb
2017
serial_forgot_password.pl
~rwXr-Xr-X
daffa
daffa
469
Feb
2017
index.pl
~rwXr-Xr-X
daffa
daffa
1758
Feb
2017 login.pl
MCU _]


To obtain the flag, we need to acquire the credentials first and then log in. To retrieve the credentials, we can use `MCU_recover_credentials.pl` and `MCU_serial_forgot_password.pl`. Here is the content of `MCU_recover_credentials.pl`: 

```perl
...
$timestamp = strftime("%j%m%H%M%Y", localtime);

open(FH,"username.txt") or &dienice("Can't open username.txt: $!");
$username = <FH>;
close(FH);

open(FH,"password.txt") or &dienice("Can't open password.txt: $!");
$password = <FH>;
close(FH);

print "Content-type:text/html\r\n\r\n";

if ($FORM{id} ne $timestamp){
    print "<html>";
    print "<head>";
    print "<title>Secure Router</title>";
    print "</head>";
    print "<body>";
    print "<center><p>Sorry, your timestamp nonce has expired</p></center>";
    print "</body>";
    print "</html>";
    exit 0;
}

print "<html>";
print "<head>";
print "<title>Secure Router</title>";
print "</head>";
print "<body>";
print "<p>Password recovered</p>";
print "<p>$username</p>";
print "<p>$password</p>";
print "</body>";
print "</html>";
```

We need to provide the correct nonce / timestamp to recover the credential. And to get the correct nonce, we can use `MCU_serial_forgot_password.pl` because the code leaked the nonce


[Image extracted text: <head>
</head>
<form method-"POST"
action-"MCU_check_serial pl?id-3531204242023">
$0
<p>Router
Serial
Number:</p>
<input
type_"text" name-"serial">
<brz
<brz
<input type-"submit">
<[form>
</body>
</html>
zbodyz]


Copy the `nonce` and paste it into the `id` parameter of the `MCU_recover_credentials.pl`file.


[Image extracted text: https:IIthecybercoopctf-secure-router chals io/MCU_recover_credentials pl?id-3531204242023
Password recovered
admin
ridingexpresstrains]


Use the credentials to log in to the website.


[Image extracted text: https:IIthecybercoopctf-secure-router chals iollogin pl
Authenticated
flag{based_on_a_true_router_cve_story}]


```
flag{based_on_a_true_router_cve_story}
```