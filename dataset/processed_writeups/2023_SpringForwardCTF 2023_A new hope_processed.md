# A new hope
> So we found this on a thumbdrive. I know, I know, don't load random USBs, but look... Things are weird right now and I figured it might be something.

> All it has is this half of a program and a weird mashing of letters and numbers.

> Maybe it's nothing, but it might be something. Think you can check?

## About the Challenge
We were given 2 files `encrypt.py` and `log.txt`. Here is the content of the `encrypt.py` file
```
def encrypt(message, key):
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted.encode("utf-8").hex()

message = #//////ERROR ERROR ERROR
key = #/////// ERROR OERROR ERROR ERROR
encrypted = encrypt(message,key)
```
The script just encrypt the `xor`ing the message using the key. And here is the content of the `log.txt` file
```
SWYgeW91J3JlIHJlYWRpbmcgdGhpcywgeW91IGJldHRlciBiZSBtZS4KTW9zdCBsaWtlbHkgeW91IGZvcmdvdCwgdGhhdCB0aW1lIGlzIHRoZSBrZXkuCg==
mpq_wxkdim_qe_WTNQ
tvp euaapnbqpr vafhlk abtx ogwi aaif qr xxeg qe


072923373661312c3f2d66273661276537203f652429232b73352f283661312c3f2d6627362f22653124202a2124663c3c346a65322f22652a2e3365302028653b242a357334352d363366313b2835653a2f68653d28252628297529231e2b760c7124740c36062b2e6f661c3c3466282632326520282b353f3866233c2d2a2a2461322d36613624272966233c3366203d2d2f223b35232b3e2428317d616b1711
```
There is some encoded msg that encoded in different way and then there is an encrypted message

## How to Solve?
Decode the message first to know what is the key. Use `Base64 Decoder` and `Vigenere Cipher`, here is the decoded message
```
If you're reading this, you better be me.
Most likely you forgot, that time is the key.
the_secret_is_SAFE
and absolutely nobody will know what my plan is
```

We know the key is `SAFE` and we need to XOR the encrypted message with the key


[Image extracted text: length:
322
Recipe
Input
lines:
+
D9
07292337366131203f2d66273661276537203f652429232b73352f28366131203f2d6627362f22653124202a2124663c3c
From Hex
346a65322f22652a2e33653020286536242a357334352d36336631362835653a2f68653d28252628297529231e2b760c71
24740c36062b2e6f66103c3466282632326520282b35363866233c2d2a2a2461322d3661362427296623303366203d2d2f
Delimiter
Auto
223635232b3e2428317d616b1711
XOR
Key
SAFE
UTF8
Scheme
Standard
Null preserving
time:
2ms
Output
length=
161
0 0 @ I
5
lines
There Will be
day when time will bend before
you,
and you
can
help usher this in.
nicc{h3lp_m3_Ob1_W@n}. You
must simply follow the path for enlightenment.
-RB]


```
nicc{h3lp_m3_0b1_w@n}
```