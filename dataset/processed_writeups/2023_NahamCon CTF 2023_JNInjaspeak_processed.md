# JNInjaspeak
> We are all very familiar with Leetspeak, can you crack the code on how JNInjaspeak works?

## About the Challenge

Given .apk files, and we must analyzed it to find flag

[file.apk](files/jninjaspeak.apk)

## How to Solve

To solve this, all you need is `strings` command

The following command is like this `strings file.apk | grep "flag"`


[Image extracted text: sinon@LAPTOP-2VOH1439
[mnt/d/a/bounty/ctf/NAHAMCON2023$ strings jninjaspeak.apk
grep
"flag'
flag{1f539e4a706e6181dae9db3fad6a78f1}covariant
return
thunk
to
flag{1f539e4a706e6181dae9db3fad6a78f1}
flag{1f53ge4a706e6181dae9db3fad6a78f1}
flag{1f539e4a706e6181dae9db3fad6a78f1}
sinon@LAPTOP - 2VOH1439
[mnt/d/a
bounty/ctf/NAHAMCON2023$]


```
flag{1f539e4a706e6181dae9db3fad6a78f1}
```