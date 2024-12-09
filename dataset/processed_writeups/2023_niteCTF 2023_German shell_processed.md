# German shell
> Do you have an Albert Einstein in you? If not you better find one cuz you gonna need em else you gunna faint rottin

> /var/quantumLava/flag.txt

## About the Challenge
We were given a server to connect without any attachment, and in this server we can execute bash command but the output is a little bit weird


[Image extracted text: [oasn-s.2#
bash-3.2$
nc
35.244.43.8
1337
$
$ 1s
Ibin/sh:
1:
tl:
not
found
$
cat
Ibin/sh:
1:
vbc:
not
found
$
whoami
Ibin/sh:
1:
nqdqiw:
not
found]


## How to Solve?
After trying some random comments, I just realize there's a "pattern"


[Image extracted text: [bash-3 .2$
nc
35.244.43.8
1337
$
aaaaaaaaaaaa
Ibin/sh:
1:
lkjihgfedcba:
not
found
$ bbbbbbbbccccc
Ibin/sh:
1:
onmlkihgfedcb:
not
found]


As we can see here, the program will reverse the results of our input and also substract -1 to each character we input. For example here, i want to execute `cat` command:

```
1. Reverse cat -> tac
2. Minus -1 character for every character
t - 0 = t
a - 1 = z
c - 2 = a
3. To execute `cat`, we need to input `tza`
```

But this doesn't apply to special character because they always changed the character every second


[Image extracted text: bash-3 .2$
nc
35
244
43.8
1337
$ SSSSSS3SSSSSSSS3
Ibinlsh:
1:
not
found
$ SSSSSSS$
Ibinlsh:
1:
Permission
denied
$ SSSSSSSS
$ SSSSSSSS
Ibinlsh:
1:
5555:
not
found
$ $sssSSS$
Ibinlsh:
1:
%62/262/62/626%6:
not
found
$ SSSSSSSS
Ibinlsh:
1:
Syntax
error:
&&
unexpected
$ SSSSSSS$
Ibinlsh:
1:
Syntax
error:
&&
unexpected
$ SsSsSSSS
Ibinlsh:
1:
Permission
denied
$ SsssSSS$
Ibinlsh:
1:
Syntax
error:
end
of
file unexpected
(expecting
") " )
$ SsSsSSSS
Ibinlsh:
1:
Syntax
error:
)"
unexpected
$ SSSSSSS$
Ibinlsh:
1:
Xxxxxxxx
not
found
$]


And to read the flag, luckily the program didn't change character `?` every second so the final payload will looks like this

```
????????/???????????/???/ hr
```

Means I want to execute

```
sh /???/???????????/????????
```


[Image extracted text: [bash-3.2$
nc
35.244
43.8
1337
$
22222222/22222222222/222/
hr
Ibin/sh:
1:
Syntax
error:
I )
unexpected
$ ?2222222/22222222222/222/
hr
Ibin/sh:
1:
sh,*?22*22222222222*22222222 :
not
found
$ ?2222222/22222222222/222/
hr
Ibinlsh:
1:
sh-+222+22222222222+22222222 :
not
found
$
22222222/22222222222/222/
hr
Ibin/sh:
1:
sh.,222,22222222222? , ?2222222 :
not
found
$ ?2222222/22222222222/222/
hr
Ibinlsh:
1:
sh/-?22-22222222222-22222222 :
not
found
$
22222222/22222222222/222/
hr
Ibin/sh:
1:
she
222 .?2222222222 . ?2222222:
not
found
$ ?2222222/22222222222/222/
hr
Ivar
quantumLava
txt:
1: nite{tr7nSi7tion_uS1ng_tlm3_net_c001_@00dyx} :
not
found
flag.]


> we need to input this command multiple times because the program change `/` into a random character

```
nite{tr7n517t10n_u51ng_t1m3_n0t_c001_00000yx}
```