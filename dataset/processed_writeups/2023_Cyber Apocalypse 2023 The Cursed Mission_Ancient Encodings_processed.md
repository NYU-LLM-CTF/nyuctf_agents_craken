# Ancient Encodings
> Your initialization sequence requires loading various programs to gain the necessary knowledge and skills for your journey. Your first task is to learn the ancient encodings used by the aliens in their communication.

## About the Challenge
We were given a zip file (You can download the file [here](crypto_ancient_encodings.zip)). If you unzip the file, there are 2 files called `output.txt` that contain an encoded flag and `source.py`. Here is the content of `source.py`

```python
from Crypto.Util.number import bytes_to_long
from base64 import b64encode

FLAG = b"HTB{??????????}"


def encode(message):
    return hex(bytes_to_long(b64encode(message)))


def main():
    encoded_flag = encode(FLAG)
    with open("output.txt", "w") as f:
        f.write(encoded_flag)


if __name__ == "__main__":
    main()
```

As we can see the script just encode the flag using `base64` encoding and `hex`

## How to Solve?
You can use [CyberChef](https://gchq.github.io/CyberChef/) to solve this chall. Input the encoded message and then use `From Hex` and `From Base64` operation. Open the website to get the flag

```
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=MHg1MzQ2NTI0MzY1N2E0Njc1NTgzMzZiNzc2NDU4NGE2NjYxNmE0MjMxNjM2ZDM0N2E2NTU2MzkzNTRkNDg1NjY2NjQzMjZiNzg2MjQ2Mzk3YTVhNTQ0ZTY2NjQ0NzY3Nzg0ZTU2Mzk2YzYyNmQ0ZDc3NWE0NDQ2NzU1YTMzNGU2NjVhNTg1OTdhNjM2ZTZjMzM2MTQ3NTY3OTRkMzMzMDNk
```


[Image extracted text: (n
JuTd
T4LCS
c9o
Cioon
TCTC:
Il (]
Cjod
JuppoC
Recipe
Input
+
O9
0x53465243657a467558336b7764584a6661634231636d3473655639354d48566664326b786246397a5a54426664476778
From Hex
4e56396c626d4d77534446755a334e665a58597a636e6033614756794d33303d
Delimiter
Auto
From Base64
Alphabet
A-Za-20-9+/=
Remove non-alphabet chars
Strict mode
162
Raw Bytes
Output
0 0 @ :
HTB{In_your_journ3y_you_will
se3 th15
encodlngs_ev3rywher3}]


```
HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}
```