# Attaaaaack5
> Q5. What is the another process that is related to this process and it's strange ?

> example : crew{spotify.exe}

## About the Challenge
We got `raw` image and we need to find the child process

## How to Solve?
To solve this, we need to find the child process using `pstree` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 pstree
```


[Image extracted text: 0x84368798: cmd
exe
2928
2876
20
2023-02-20
19:03:40
UtC+0uuO
0x84398998: runddl32
exe
300
2876
10
2314
2023-02-20
19:03:40 UTC+O0OO
0x84390030:notepad
exe
2556
300
58 2023-02-20
19:03:41
UTC+O0OO
0x8550b030
csrss
exe
416
396
268 2023-02-20 19:01:20 UTC+0]


Or you can use `pslist` plugin and then look for the process whose parent pid is 300

```
crew{notepad.exe}
```