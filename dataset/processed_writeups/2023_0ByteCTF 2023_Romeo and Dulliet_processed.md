# Romeo and Dulliet
> Romeo dan dulliet merupakan sepasang kekasih, Mereka berdua memutuskan untuk tetap bersama meskipun segala rintangan, dan dengan bantuan Friar Laurence, seorang pendeta yang berharap bahwa pernikahan mereka bisa memperdamaikan keluarga-keluarga tersebut, mereka merencanakan pernikahan rahasia. Sayangnya, situasi semakin memburuk ketika Tybalt, sepupu dulliet, menantang Romeo untuk duel karena ia merasa terhina oleh kedatangan Romeo ke pesta mereka. tugas kalian carilah kelebihan dan kekurangan dari sepasang kekasih ini.

## About the Challenge
Given a ZIP file containing two server logs from a website named `Dulliet.txt` and `Romeo.txt`. Each log file has a large file size of around 66 megabytes. Upon initial inspection, it appears that the two files are similar in content.


[Image extracted text: Dullietbxt
Romeobt
1 4
Pomeo bxt
83.195.18.195
[01/Jun/2023:00:01:00
+0788] "GET /dashboard/transac
83.195.18.195
[01/ Jun/ 2023:88:01:88 +0700] "GET
Adashboandettans
80.172.186. 28
[01/Jun/2023.00:02:06 +0788]
"POST /dashboard/add HI
80.172.186.28
[01/ Jun/2823:88:02:86 +0700] "POST /dashboard/add
89.209.181.44
[01/Jun/2023:00:03:09 +8780] "POST /dashboard/login
89.209.181.44
[01 / Jun/2823:88:03:09 +0700] "POST /dashboard/logir
155.21.25.104
[01/Jun/2023:00:04:00 +0700] "GET /contact HTTP/1
155.21.25.104
[01/ Jun/2023:80:04:00 +0700] "GET /contact HTTP/1
108.189.11.31
[01/Jun/2023:00:04:35 +0788] "GET /assets/css/bootsti
108.189.11.31
[01/Jun/2023:08:04:35 +0700] "GET /assets/css/boots
146.22.134.29
[01/ Jun/2023:00:05.41 +07801 "GET
HTTP/1.1" 40
146.22.134.29
[01/ Jun/2023.80:05.41
+0700] "GET /logs HITP/1.1"
Hlogs]


## How to Solve?
If these two log files are further analyzed, it becomes apparent that there are some differences between them. Firstly, the number of lines in the `Dulliet.txt` log file is 438,923 lines.


[Image extracted text: 4900921
140
LL154
23
LsoiAubi 2025.25.90 15
+0r00]
Fusi
1uasmdoarurtrai
438922
89.209.181.44
[30/Aug/2023:23:58:52 +0700] "POST /dashboard/log'
438923
178.37.153.34
[30/Aug/2023:23:59:53 +0700] "GET /support HTTP/1
438924]


Meanwhile, the `Romeo.txt` log file contains a total of 438,979 lines.


[Image extracted text: 4903
40L4194.
130iAubi 202s.2.30.1
TOToo]
odi
Tudsudoauictam
438978
89.209.181.44
[30/Aug/2023:23:58:52 +0700] "POST /dashboard/logi
438979
178.37.153.34
[30/Aug/2023:23:59:53 +0700] "GET /support HTTP/1
438980]


When I attempted to find suspicious requests in both logs, I discovered several lines where each line contained only one character. For example, as shown in the image below:


[Image extracted text: 1545
229.239.15.87
[01/Jun/2023:22.41.42 +0
1546
217.112.15.97
[01/Jun/2023:22:42:37
+0
1547
59.45.194.238
[01/Jun/2023:22:43:50
+02
1548
1549
91.120.11.246
[01/Jun/2023:22:45.47 +03
1550
59.45.194.238
[01/Jun/2023:22:46:37 +03
1551
155.21.25.104
[01/Jun/2023:22:47:20 +03
1552
194.25.80.209
[01/Jun/2023:22:48.:11 +03
1553
146.22.134.29
[01/Jun/2023:22:49:21 +03
1554
248.84.162.17
[01/Jun/2023:22:50:01 +03]


In the `Romeo.txt` file, at line 1548, there's a `{` character, which is typically a format used in CTF flags. Following this, I tried to create a Python script to search for a similar lines that contain only 1 character.

```python
with open('Dulliet.txt', 'r') as log_file:
    for line in log_file:
        line = line.strip()
        if len(line) == 1:
            print(line)
```

Then, run the above code on both the `Dulliet.txt` and `Romeo.txt` files. Here are the results:


[Image extracted text: daffainfo@dapOs:~/Romco
and_Dullietf python3 test.py
M
3]



[Image extracted text: daffainfo dapOS:~/Romeo_and_Dulliet$ python}
test-py
{
^
m
;
}]


At first glance, both lists of characters seem to resemble a flag, although they appear to be somewhat jumbled. In this case, I tried manually flipping and combining both sets of characters, which eventually formed a flag.

```
0byteCTF{s3M4n9At_3mPAt_l1m4_1337}
```