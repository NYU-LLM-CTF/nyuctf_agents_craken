# Idoriot
> Some idiot made this web site that you can log in to. The idiot even made it in php. I dunno.

## About the Challenge
We were given a website that has 2 functionality, first we can register as a user in this website


[Image extracted text: Not secure
idoriotchal.imaginaryctforg/register php
Registration
The user database will be wiped every 30 minutes.
Username
Password
Register
Already have an account? Login]


And then, after registered an account, you can also login into the website


[Image extracted text: < >
C
Not secure
idoriot chal_imaginaryctf org/login php
Login
Username:
Password:
Login
Don't have an account? Register]


And then after login, there is a source code that you can see written in PHP


[Image extracted text: Not secure
idoriot chal.imaginaryctforg/indexphp
Welcome; User ID: 397208627
Source Code
<?php
session_
start();
Check if
user
logged
if
(lisset(s_SESSION[
user
id']))
header
Location:
login-php") ;
exit();
Check if
session i5
expired
if
(time
$_SESSION[
expires' ])
header(
Location:
logout.php") ;
exit();
Display
user
landing
page
echo
"Welcome
User
ID:
urlencode
$_SESSION[
user
id' 1);
Get the user
for
admin
Sdb
ner
PDO (
sqlite:memory:
Sadmin
Sdb->query
SELECT
FROM
users
WHERE
user
LIMIT
1' )->fetch();
Check if
the
user
admin
if
Sadmin[
user
id' ]
$_SESSION[
user_id' ])
Read
the
from flag
txt
Sflag
file_
contents
'flag-
txt' ) ;
echo
<hl>Flag< /hlx"
echo
<p>Sflags /p>
else
Display
the
source
code
for
this file
echo
<hl Source
Code< /hl>"
highlight
file
FILE_);
Lid
flag
get]


```php
<?php

session_start();

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Check if session is expired
if (time() > $_SESSION['expires']) {
    header("Location: logout.php");
    exit();
}

// Display user ID on landing page
echo "Welcome, User ID: " . urlencode($_SESSION['user_id']);

// Get the user for admin
$db = new PDO('sqlite:memory:');
$admin = $db->query('SELECT * FROM users WHERE user_id = 0 LIMIT 1')->fetch();

// Check if the user is admin
if ($admin['user_id'] === $_SESSION['user_id']) {
    // Read the flag from flag.txt
    $flag = file_get_contents('flag.txt');
    echo "<h1>Flag</h1>";
    echo "<p>$flag</p>";
} else {
    // Display the source code for this file
    echo "<h1>Source Code</h1>";
    highlight_file(__FILE__);
}

?>
```

To read the flag, we need to login as an admin where the `user_id` is `0`

## How to Solve?
I believe, I solved this chall using unintended way, as you can see in this code

```php
if ($admin['user_id'] === $_SESSION['user_id']) {
    // Read the flag from flag.txt
    $flag = file_get_contents('flag.txt');
    echo "<h1>Flag</h1>";
    echo "<p>$flag</p>";
}
```

The location of the flag is `flag.txt` not `/flag.txt`. So, you can read the flag directly by accessing http://idoriot.chal.imaginaryctf.org/flag.txt


[Image extracted text: 9
C
Not secure
idoriot chal_imaginaryctf.org
txt
ictf{ins3cure_
direct
object_reference_
from_hidden_post
param_i
guess}
/flag:t]


```
ictf{1ns3cure_direct_object_reference_from_hidden_post_param_i_guess}
```