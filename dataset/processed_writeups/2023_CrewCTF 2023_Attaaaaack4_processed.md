# Attaaaaack4
> Q4. What is the name and PID of the suspicious process ?

> example : crew{abcd.exe_111}

## About the Challenge
We got `raw` image and we need to find the suspicious process and also the pid

## How to Solve?
To solve this, we need to find the suspicious process using `pslist` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 pslist
```


[Image extracted text: 0x84368798
cmd
exe
2928
2876
20
2023-02-20
19:03:40
UtC+OOOO
0x84365c90 conhost
exe
1952
416
49
2023-02-20
19:03:40 UTC+OOOO
0x84384d20
conhost
exe
2924
416
2
49
2023-02-20
19:03:40 UTC+OOOO
0x84398998 runddl32.exe
300
2876
10
2314
1
2023-02-20
19:03:40 UTC+OOOO
0x84390030
notepad.exe
2556
300
58
2023-02-20
19:03:41 UTC+OOOO
Ox8udf2458 audiodg
exe
1556
752
6
129
2023-02-20
19:10:50 UTC+OOOO
Ox8uflcaf8 DumpIt.exe
2724
1596
38
2023-02-20 19:10:52 UTC+OOOO]


You will notice there is a suspicious proccess called `runddl.exe`. Why suspicious? because the program has a typo, not `rundll.exe` but `runddl.exe`

```
crew{runddl.exe_2556}
```