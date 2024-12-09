# Simple rev
> `-`

## About the Challenge
We were given a file (You can download the file [here](outfile)) and we need to do reverse engineering to get the flag

## How to Solve?
The easiest solution is by using `strings` command and then find the flag using `grep`. Here is the command that you can used

```shell
strings outfile | grep "grepCTF"
```

Here is the output


[Image extracted text: root@LAPTOP-FIL3RGSH:~# strings
outfile
grep
"grepCTF"
grepCTF {4p0g33_hlvemlnd_g3n3sls}
root@LAPTOP-F9L3RGSH:~#]


```
grepCTF{4p0g33_h1vem1nd_g3n3s1s}
```