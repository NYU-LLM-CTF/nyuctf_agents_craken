# ERaaS
> Emergency response? Afraid not

## About the Challenge
We were given a website without the source code, where the website only has one functionality: converting the epoch to date.


[Image extracted text: Epoch Reverter as a Service
123123123
submit
Mon
Nov
26
00:52:03
UTC
1973]


## How to Solve?
The website is vulnerable to OS Command Injection through the addition of `;` after the epoch, followed by the command you want to execute


[Image extracted text: 123123123; Is
submit
Mon
Nov
26
00:52:03
UTC
1973
pycache_
flag.txt
main.pY report.pY requirements
txt
run.sh
templates]



[Image extracted text: 123123123; cat flag.txt
submit
Mon
Nov
26
00:52:03
UTC
1973 nite{b3tt3r
no
thZn_b7d_cSp_rlbht_fh8w4d}
cSp_]


```
nite{b3tt3r_n0_c5p_th7n_b7d_c5p_r16ht_fh8w4d}
```