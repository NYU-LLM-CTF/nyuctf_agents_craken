# The Historian Channel - 2
> Jubilife’s SOC looked for other suspicious events around the time of the successful brute force login and noticed earlier activity from the suspicious user (IP address 192.168.4.146) in the web server logs. It looks like this user attempted to access information on the webserver without logging in, and it is possible that they succeeded in reading files they were not supposed to have access to due to a misconfiguration.

> What is the name of the file (full path) that the suspicious user accessed from the webserver?

> Flag format: full path of file. Example: if the file accessed was /folder/file.txt, the flag would be /folder/file.txt

## About the Challenge
We were given a log file to analyze (You can download the file [here](access.log)). And we need to find the full path of the file that the user accessed

## How to Solve?
If we check on the log file, there are some suspicious request that the suspicious user trying to find some configuration files such as `config.txt` or `config.ini`


[Image extracted text: 192.168
4.134
[04/May/2023:11:55:06
0500]
"GET [jubilifehistorian/css/update 
CSS
HTTP/1.1" 200 322 "http:/ Ljubilifehistorian/upC
192.168
4.146
[04/May/2023:12:05:09
0500
"GET [jubilifehistorian_config.ini HTTP/1.1"
404 490
"Mozilla/5.0 (Windows NT
10
192.168
146
[04/May/2023:12:05:14
0500]
"GET /jubilifehistorian_config txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
NT
10 .
192.168
146
[04/May/2023:12:05:29
0500]
"GET /config ini HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
NT
10.0; Win64; X64) Appl
192.168
4.146
[04/May/2023:12:05:41
0500]
"GET /config txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
NT 10.0; Win64; X64) Appl
192.168
4.146
04/May/2023/.12:05:49
0500
"GET /config/jubilifehistorian_config.ini HTTP/1.1"
404
490
"Mozilla/5.0 (Windows
192.168
4.146
[04/May/2023:12:06:03
0500
"GET /configljubilifehistorian_config txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
192.168.4.146
[04/May/2023:12:06:10
0500
"GET /config/config.ini HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
NT
10.0; Win64;
192.168
4.146
[04/May/2023:12:06:22
0500
"GET /config/config txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
NT
10.0; Win64;
192.168
4.146
[04/May/2023:12:06:29
0500
"GET [jubilifehistorian/jubilifehistorian_config ini HTTP/1.1"
404
490
"Mozilla/5
192.168
4.146
[04/May/2023:12:06:44
0500
"GET /jubilifehistorian/ jubilifehistorian_config.txt HTTP/1.1"
404
490
"Mozilla/5
192.168
4.146
[04/May/2023:12:06:58
0500
"GET [jubilifehistorian/config.ini HTTP/1.1" 200 1635
"Mozilla/5.0 (Windows
NT
10
192.168
4.146
[04/May/2023:12:07:03
0500
"GET [jubilifehistorian/config txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows NT
10_
192.168
4.146
[04/May/2023:12:07:09
0500
"GET [jubilifehistorian/config/jubilifehistorian_config txt HTTP/1.1"
404 490
'Moz
192.168
4.146
[04/May/2023:12:07:14
0500
"GET [jubilifehistorian/config/jubilifehistorian_config.ini HTTP/1.1"
404 490
Moz
192.168
4.146
[04/May/2023:12:07:22
0500
"GET [jubilifehistorian/config/config.ini HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
192.168
4.146
[04/May/2023:12:07:30
0500
"GET [jubilifehistorian/config/config.txt HTTP/1.1"
404 490
"Mozilla/5.0 (Windows
192.168
4.147
04 /Mav/2023.12:08.54
0500
"GET /login.php HTTP /1.15
200 697
"Mozilla/5.0 (Windows NT
10.0; Win64;
X64) Apple]


As you can see, some of the requests returned a `404 Error`. However, when the user accessed `/jubilifehistorian/config.ini`, it returned a `200 OK` status code.

```
/jubilifehistorian/config.ini
```