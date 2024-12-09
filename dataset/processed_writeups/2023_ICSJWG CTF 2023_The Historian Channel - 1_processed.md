# The Historian Channel - 1
> Jubilife’s security operations center (SOC) team has noticed some alarms are missing from a historian dashboard on one of the internal ICS networks. This historian runs an Apache web server to host its database and allows users to query various settings, statuses, alarms, and warnings from devices on the network.

> In these challenges, you will work with Jubilife’s SOC team to review the historian’s Apache logs and determine whether there is evidence of adversarial activity, and figure out how the alarms were deleted from the database.

> Attached is the historian’s access.log file from the time period the SOC team would like you to review. Most users logged into the historian’s web server on their first attempt, if not their second or third, but one user repeatedly failed in an apparent brute force attempt before eventually logging in successfully.

> What time did the suspicious user successfully login?

> Flag format: timestamp of the successful login from the suspicious user, without the timezone. Example: if the timestamp was [04/May/2023:09:24:56 -0500], the flag would be 04/May/2023:09:24:56

## About the Challenge
We were given a log file to analyze (You can download the file [here](access.log)). And we need to find the timestamp of the succesful login from the suspicious user

## How to Solve?
If we check content of the log file, you will see some suspicious requests from `192.168.4.146`


[Image extracted text: 192.168.
146
[04/May/2023:13:01:26
0500] "GET
alarms.php/ ?deviceID-1227%3BSELECT%zoreplace(replace(replace(replace(rep
192.168 _
146
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-1227 .%28.%2C .
%22.&Submit-Submit HTTP/1.1
500 121
192.168
4.146
[04/May/2023:13:04:55
0500
"GET [alarms.php/ ?deviceID-1227WIJFRA%3C%27%22%3EvWSrWo&Submit-Submit HTTP/1.1
192.168
4.146
[04/May/2023:13:04:55
0500
"GET [alarms.php/ ?deviceID-1229%2OAND%2075692302047220AND?20228832823083288Sub
192.168
4.146
[04/May/2023:13:04:55
0500]
"GET /alarms.php/ ?deviceID-1%29%20AND%2033512303351%20AND%20%287909%3D7909&Sub
192.168
4.146
[04/May/2023:13:04:55
0500]
"GET [alarms.php/ ?deviceID-1%2OAND?206699%3D8178&Submit-Submit HTTP/1.1" 500
192.168
146
04/May/2023:13:04:55
-0500]
"GET  /alarms.php/ ?deviceID-1%20AND%20335123033518Submit-Submit HTTP/1.1" 500
192.168
146
[04/May/2023:13
04:55
0500
'GET  /alarms.php/ ?deviceID-1%2OAND%2032212309412--%2Oxbc&Submit-Submit HTTP/1
192.168
146
[04/May/2023:13
04:55
0500
'GET  /alarms.php/ ?deviceID-1%2OAND%2033512303351
-%20jmcx&Submit-Submit HTTP/1
192.168
146
[04/May/2023:13
04:55
0500
'GET  /alarms.php/ ?deviceID-1227229%2OAND%2067532302200%2OAND%20228227GhKm227%3
192.168
4.146
[04/May/2023:13:04
55
0500
"GET [alarms.php/ ?deviceID-122722922OAND%203351230335122OAND%20228%27eecB227%3
192.168
4.146
[04/May/2023:13
04:55
0500
"GET [alarms.php/ ?deviceID-1227%2OAND%2041562305452220AND?20227VBNn?27%30227VB
192.168
4.146
[04/May/2023:13
04:55
0500
"GET [alarms.php/ ?deviceID-1227%2OAND%203351230335122OAND%20227THRD?27%30227TH
192
168 _
4.146
04/May/2023:13
04:55
0500
"GET  /alarms.php/ ?deviceID-1227%2OAND?2066032302942220AND?20227NSbh?27%30%27NS
192.168 _
146
[04/May/2023:13:04:55
0500
"GET /alarms.php/ ?deviceID-%28SELECT%2O%28CASERZOWHEN?20%2832687309651229%20TH
192.168 _
146
[04/May/2023:13:04:55
0500
"GET  [alarms.php/ ?deviceID-%28SELECT%2O%28CASERZOWHEN%20%2811947301194229%20TH
192.168 _
146
[04/May/2023:13:04:55
0500
"GET  [alarms.php/ ?deviceID-1229%20AND%ZOEXTRACTVALUE?28823222CCONCAT%280x5c22C
192.168 _
146
[04/May/2023:13:04:55
0500
"GET /alarms.php/ ?deviceID-1%2OAND%ZOEXTRACTVALUE%28823222CCONCAT2280x5c%2COx7
192.168
4.146
[04/May/2023:13:04:55
0500
"GET [alarms.php/ ?deviceID-1%2OAND?ZOEXTRACTVALUE?28823222CCONCAT%280x5c%2COx7
192.168
146
04/May/2023:13:04:55
0500]
"GET
[alarms . php/ ?deviceID-122782922OAND%2OEXTRACTVALUE?28823222CCONCAT%280x5c]


So, im using this regex

```
192.168.4.146 - - .* "POST /login.php
```

To determine when a suspicious user accessed the login page, you need to consider that some of the requests made after submitting the `POST` method to `login.php` will result in the user being redirected back to the `login.php` page. This is due to the logic of the website, which redirects users back to the login page if they cannot provide correct credentials.


[Image extracted text: 82
192.168.4.146
04/May/ 2023:12:21:38
0500
~GET
1 Jubilitenistorian/ CsS/ 0g1n.
183
192.168
4.146
04/May/2023:12:21:38
0500
"GET
[jubilifehistorian/images/jub
84
192.168.4.146
04/May/2023:12:21:38
0500
"POST /login.php HTTP/1.1" 302
391
185
192.168
4.146
04/May/2023:12:21:38
0500
"GET
Ilogin.php HTTP/1.1"
200 603
86
1192.168
4.146
04/May/2023:12:21:55
0500
'POST /login.php HTTP/1.1"
302
375
187
192.168
4.146
04/May/2023:12:21:55
0500
"GET Tlogin.php HTTP/1.1" 200 644
188
192.168
4.146
04/May/2023:12:22:20
0500
'POST
/login.php HTTP/1.1" 302
333
189
192.168
4.146
[04/May/2023:12:22:20
0500
"GET
login.php HTTP/1.1" 200
700
90
192.168
4.146
04/May/2023:12:22:50
0500
'POST
'login.php HTTP/1.1" 302 374
91
192.168
4.146
[04/May/2023:12:22:50
0500
"GET
index.php HTTP/1.1" 200 2500
192
192.168
146
[04/May/2023:12:22:50
0500
"GET [jubilifehistorian/css/main.c
193
192.168.4.130
[04/May/2023
12:31.49
0500
"GET /login.php HTTP/1.1
200 615]


But in line 190, after sending the `POST` request to the login.php page, the user is redirected to `index.php`. Therefore, the attacker has successfully logged in to the website.

```
04/May/2023:12:22:50
```