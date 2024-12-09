# Tengu In Colosseum
> Now, dear seeker of knowledge, do you yearn for guidance amidst this tangled labyrinth of evidence? Pray, let us illuminate the path before you, clarifying the enigmatic queries that shroud these digital artifacts.

## About the Challenge
We were given an image forensic challenge (on an Android). Additionally, we have received 10 questions that we need to answer correctly in order to obtain the flag.

## How to Solve?
In this case, im using `FTK Imager` to access some of the artifact, and also [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) to parse SQLite artefact

For the first question, we can obtain the information by using `/data/com.Slack/databases/org_T03EA50JASY` and then open the artefact using SQLite viewer.


[Image extracted text: messages (20 rows)
SELECT
FROM
messages
LIMIT
0,30
Execute
id
local_id
channel_id
client_msg_id
msg_send_state
ephemeral_msg_type
calls_room_id
thread
e9614d10-1cdc-4cf6-bfdb-b.
1651760692.920739
DOEXHZBYF2
null
null
null
f1c28e9f-385f-41b7-9742-C.
1651759634.281579
DO3EXHZBYF2
a305e58e-31ea-4f03-b162-
null
null
d22bOc1f-a0e0-45a8-8f19-0
1651758731.157879
DO3EA592P6G
null
null
null
c1a84931-cf61-464a-bcc7-2.
1651760693.015669
CO3ELD9B36V
null
null
null
4f2304e5-c132-4747-8d57-
1651758756.010499
CO3ELD9B36V
1e4f2f50-6a16-43e4-9264-2
null
null
3586dfbc-d0c7-441f-87bc-9.
1651758730.672819
CO3ELD9B36V
8bd7cc98-1f5a-4972-b4ab-f
null
null
e355bc0a-0600-418f-3654-
1651758598.180309
CO3ELD9B36V
null
null
null
72471388-0e7d-4322-b787-
1651799094.170179
CO3ELD9B36V
b4814eb4-52c8-46db-b964-_
null
null
46849e7d-6130-46bf-9441 -
1651799230.162739
CO3ELD9B36V
40db7045-bccd-4dd1-abbf-
null
null
10
754e8d11-b9bd-4d6c-b3f1-.
1651799254.033219
CO3ELD9B36V
bae3c2ee-4Odb-46ca-9d87_
null
null
40397cca-082c-42b9-8361-
1651799288.141579
CO3ELD9B36V
6e4122bc-f977-4e69-a7b1-
null
null
12
aObc1f45-cdc2-44ad-8b6a-
1651799311.614879
CO3ELD9B36V
aab076d8-6592-46cf-a8e2-.
null
null
13
6d4aebdo-872b-4252-9f2f-4
1651799330.000469
CO3ELD9B36V
d681328d-Scbb-49ff-9554-8,
null
null]


And then find `message_json` column, and read the whole conversation. You can find the group name by checking the data that has id `5` (b34stclub) and also the name of who invited Takumi to join this slack channel is `rosse` (Check data that has id `8`)


[Image extracted text: 1
Who
invited
Takumi
to
join
the
illegal
Human
Trafficking community?
What
the
name
of
the group/community?
And
what
the
name
of
the
first
app used
to
begin
the
chat
conversation?
(AlL
of
the
answers
are
lowercase)
Format
name_
communityname
appsname
Ex: john_theragingbullseyel337_michat
Note
The first application
was
used
to
INVITE
Takumi
to join the illegal
Human
Trafficking community 
rosse_b3ustclub_slack
Correct!
57:]


You can find Takumi email by using `/data/com.Slack/databases/T03EA50JASY` artefact and then find `users` table


[Image extracted text: users
8 TOWS )
SELECT
FROM
users
LIMIT
0,30
profile_display_name
profile_real_name_
normal:
profile_display_
name
nor .-
profile_email
takumi ozawa
takumi ozawa
takumi ozawa
takumiOzaw4@gmail.com
Slackbot
Slackbot
Slackbot
null]


And you can find the name of the boss by using `/data/com.Slack/databases/org_T03EA50JASY` artefact and then find `messages` table and find `message_json` data that has id `3`


[Image extracted text: 'message
'subtype
'bot_message
alert_type
"UNKNOWN"
'hidden" : false,"ts
"1651758731.157879"
bot id"
B01"
"mrkdwn
true, "ephemeral_msg_type"
0 ,
user" : "USLACKBO
bot
upload-
false,
files
[J,"is_
starred
false,
is
read"
false,
pinned_
to
[J,"text
@UO3EASTMHK7>
just
sent <https: / /b34stclub. slack. com/archives/C03ELD9B36V/ p16517
st
message>
to
channel you're
in.
tada:
Help keep the
conversation going
attachments
[{"id":"1"
fallback"
[May Sth,
2022
6 :52
santokuabubasa:
wave:
Hi
ryone
ts
1651758730
author
name
Santoku Abubasa
author link
'https:
/b34stclub. slack
com/team/U03E4STMHK7
author
icon
https
/avatars_
slack
vpe
AN]]



[Image extracted text: 2
What
Takumi
email?
And
what
the
boss
name
likely?
If the
boss
full
name
consists
of
two
words ,
you need
to join
them
(Mikazu Tamara
~>
mikazutamara)
All
the
answers
are
in
lowercase
Format
emaildtld_bossname
Ex:
badut@mail.Xyz_mikazutamara
>>: takumiozawu@gmail.com_santokuabubasa
Correct!]


And you can find how many channels are there by using `/data/com.Slack/databases/org_T03EA50JASY` artefact and then find `conversation` table, as you can see there are 6 data in the table. And then find the column called `type`, if the data `type` is PUBLIC, that means that is a slack channel. So, essentially there are only 3 channels in the slack server


[Image extracted text: conversation
6 rOWS)
SELECT
FROM
id
conversation_id
CO3DT6UZYSD
CO3EZQ4GSSF
CO3ELD9B36V]


And if you want to find the last created channel, you can sort the `conversation` table based on `latest` column


[Image extracted text: 3
How many channels
are
there
in the first app?
Also ,
What
the
name
of
the
last
created
channel?
(exclude
any prefix(es)
of
the
channel's
name
like
ignore
the
#'
and
all LOWERCASE)
Format
TotalChannels_Name
Ex:
2_this-is-home
>>:
3_selling-muggles-for-fun-profit-not-stack
Correct!]


The second app is discord, because if you check the `messages` table again, you will see they plan to moved to discord


[Image extracted text: What
s the
second application
that
was
used
to communicate?
Format
appsname
(all LOWERCASE)
Ex:
wechat
>3:
discord
Correct!]


We can obtain the creation date of the discord server by using `/data/com.discord/files/STORE_GUILDS_V34` artefact and then use `string` to check the content of the artefact


[Image extracted text: java.util.ArrayLis
do.t
clolbe21gbf2172fd3f30a970543fb3
2022-05-05T13
44
59
886000+00
com.discord.api guild.GuildMaxVideoChannelUsersSLimite
b3ustcLu
en-U
deprecate
do.t_]


The creation date of the server is `05/05/2022_13:44:59`


[Image extracted text: 5 _
When
was
the group/server
in
the second
application created?
Format
DD/MM/YYYY_
HH
MM:SS
(In
UTC Format)
Ex:
02/01/2019_10
28:30
05/05/2022_13:44:59
Correct!
57:]


To find who created the registration system, we can check `/data/com.discord/files/STORE_MESSAGES_CACHE_V38`


[Image extracted text: Ye
Look Gopher will
create
registration system for
us
to
validate
behind
the shadow
ye]


His name is `Gopher`


[Image extracted text: 6 _
Who
creates
registration system for
the
illegal
Human
Trafficking
Community?
Format
name
(lowercase)
Ex:
>3:
gopher
Correct!
yuda]


To find the URL, you can use the same artefact, than just find the correct link


[Image extracted text: s4nto-ku
http://e2d4-2001-448a-2082-27c2-99ee-296d-aa07-9aa2.ngrok
takuzaw]


As you can see the the discord name called `s4nt0-kun` give me the link to takumi


[Image extracted text: 7 _
What's
the
URL
for
the registration
form
website
that
was
created
by
the
one
who
creates
the registration system?
Format
URL
ex:
Ijustlikethis.com
>3:
http://e2d4-2001-448a-2082-27c2-99ee-296d-aa07-9aa2.ngrok
io
Correct!
http:]


We can see user's trusted domain cache key by accessing `/data/com.discord/shared_prefs/com.discord_preferences.xml` artefact


[Image extracted text: astring name
Loo_
CACNE
RE
USER
LOOIN
7takum
<set name="USER_TRUSTED_
DOMAINS_
CACHE
KEY
<string>e2d4-2001-448a-2082-27c2-99ee-296d-aa0-
<string>2360-125-166-45-13.ngrok.io< /string_
<string> pastebin com< /string
Iset>]


As you can see, the total of `string` element are 3


[Image extracted text: 8
How many
user
trusted
domain cache key(s) in the second application?
Format:
totaloftheusertrusteddomaincachekey
Ex:
23
>>:
Correct!]


And then for this part, in the discord messages we got a PHP file

```php
<?php
    function generateRandomString($length = 2) {
        $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[mt_rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }
    if(isset($_POST['submit'])){
        if($_POST['username'] != ""){
            $username = $_POST['username'];
        }
        if($_POST['password'] != ""){
            $password = $_POST['password'];
        }
        if($_POST['sc'] != ""){
            $sc = $_POST['sc'];
        }
        $enc = openssl_encrypt($password, "rc4", $sc . generateRandomString());
        setcookie('username',$username,time() + (86400 * 30), "/");
        setcookie('guid_usr',$enc, time() + (86400 * 30), "/");
        header("Location: ./success.php");
    }
```

And we need to find the password, luckily one of the team member solved this question by bruteforcing a little bit of character


[Image extracted text: 9
Takumi
downloaded
an
illegal
APK
that
was
given
by
the Boss _
The
Boss
said that
apk
was
zipped
and protected with
his password that
was
used
before
in
the registration
form
website
Our
DFIR acquintance
said
that
the
source
code
of
that
form
was
revealed
in
the
second
application
and
the
secret
code
refers
to
the
SC
parameter
What
the password
of
the
zipped
APK file?
Format
password
Ex:
!aml33t
>>:
th!s_lz_a_V3ry_Unc3nZureD_p4SSwOrd
Correct!]


And for this part, you can find the pastebin link in the history, and if you open the pastebin directly, the data has been removed


[Image extracted text: pastebin com/8rHPOabR
PASTEBIN
API
TOOLS
FAQ
paste
Search 
10y
Not Found (#404)
This page is no longer available: It has either expired,
been removed by its creator; or removed by one of the Pastebin staff:
(0011]


However, you can still see the data using `Wayback Archive`


[Image extracted text: 10 _
The boss gave
Takumi
website
link
containing
text-based
information regarding
cash-flow spending
of
the community
and
the potential
ne
xt
volunteers
who
are
willing to
be
sold_
Luckily
he already
read the
content
and
ARCHIVED
it
How
many
volunteers
that
come
from
United
States (US)
Format
TotalVolunteersFromUs
Ex:
105
>>:
Correct!]


voilà, you obtain the flag


[Image extracted text: Here
your flag:
flag{you_defeated_th3_tengu_droid}]


```
flag{y0u_defeated_th3_ten9u_droid}
```