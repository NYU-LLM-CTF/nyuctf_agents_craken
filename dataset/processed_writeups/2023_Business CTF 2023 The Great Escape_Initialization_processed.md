# Initialization
> During a cyber security audit of your government's infrastructure, you discover log entries showing traffic directed towards an IP address within the enemy territory of "Oumara". This alarming revelation triggers suspicion of a mole within Lusons' government. Determined to unveil the truth, you analyze the encryption scheme with the goal of breaking it and decrypting the suspicious communication. Your objective is to extract vital information and gather intelligence, ultimately protecting your nation from potential threats.

## About the Challenge
We got a zip files (You can download the file [here](crypto_initialization.zip)) that contains 3 more files (1 python script and 2 txt file). Here is the content of `source.py`

```python
#!/usr/bin/env python3

import os
from Crypto.Util import Counter
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

class AdvancedEncryption:
    def __init__(self, block_size):
        self.KEYS = self.generate_encryption_keys()
        self.CTRs = [Counter.new(block_size) for i in range(len(MSG))] # nonce reuse : avoided!

    def generate_encryption_keys(self):
        keys = [[b'\x00']*16] * len(MSG)
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                keys[i][j] = os.urandom(1)
        return keys
    
    def encrypt(self, i, msg):
        key = b''.join(self.KEYS[i])
        ctr = self.CTRs[i]
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        return cipher.encrypt(pad(msg.encode(), 16))

def main():
    AE = AdvancedEncryption(128)
    with open('output.txt', 'w') as f:
        for i in range(len(MSG)):
            ct = AE.encrypt(i, MSG[i])
            f.write(ct.hex()+'\n')

if __name__ == '__main__':
    with open('messages.txt') as f:
        MSG = eval(f.read())
    main()
```

It looks like this python code will encrypt the msg inside `messages.txt` using AES-CTR and then save the encrypted msg in `output.txt`

## How to Solve?
At first i tried to run the program and see the behaviour. Before i ran the program, i added `print (self.KEYS)`. And here was the result


[Image extracted text: [[b' Ixgc
b ' Ixbc
b'n'
b'W'
b'0 '
b'
b' Ix82 '
b ' Ixf1'
b' Ixoc '
b'W'
b ' Ixf9'
b' Ixea
b' |x93 '
b' Ix97'
b ' Ixe9 '
b' It'],
[b' Ixgc'
b' Ix
bc
b'n'
b'W'
b'0 '
b
b' |x82 '
b' Ixf1'
b ' Ixoc
b'W'
b' Ixf9'
b' Ixea
b' [x93
b' |x97 '
b' Ixe9'
b' It']
[b' Ixgc '
b' Ixbc
b'n'
b'W'
b'0 '
b'
b' Ix82
b ' Ixf1'
b' Ixoc
b'W'
b ' Ixf9
b' Ixea
b' |x93 '
b' Ix97'
b ' Ixe9 '
b' It'],
[b' Ixgc '
b' Ixbc
b'n'
b'W'
b'0' ,
b' :' ,
Ix82 '
b' Ixf1'
b ' IxOc '
b'W'
b' Ixf9
b' Ixea
b' [x93
b' |x97'
b' Ixe9'
b' It'1]
5815ddd8f0811c234f08af933296f7125b144ba38f77b191ae704f98899bae9f5233b2af0eblb983c4f17elc9dbcc277345565525407ab9afd09cfb32d722620
421294c4be8d4f605d09e2956087e11617125df1c67cb99dae645eg8899bae9f4737b4b45cbbac8589bd1d3ae9dfa515
4429f6d0efd7503c0358fdc92dd9bd4f084217bcd926e8cle32211d3dfcbff801964ece41lede7d2dbac2403d0e69c2c2b471e287a65cael9729c7bb257a2e28
5f18d7d9b59c4f6a5201ad847f87f619581308ea9539b290bf6f579c9491a49f5132a7b30e93bc9b85fd78598bf9e67d774869560002ab81b974bdd4451041548c486ba8fu6ff1c9
c7ddfb253caecaac]


As you can see the program encrypt the key is reused for all the encryption. And because of the nonce was reused, we use this notation

```
flag = (ciphertext1 ⊕ ciphertext2) ⊕ known_plaintext
```

And i used this [reference](https://github.com/Y-CTF/writeups/tree/main/CryptoCTF2021/Wolf) to solve this chall

```python
known_plaintext = 'This is some public information that can be read out loud.'
encrypted_text = bytes.fromhex('76ca21043b5e471169ec20a55297165807ab5b30e588c9c54168b2136fc97d147892b5e39e9b1f1fd39e9f66e7dbbb9d8dffa31b597b53a648676a8d4081a20b')
encrypted_flag = bytes.fromhex('6af60a0c6e5944432af77ea30682076509ae0873e785c79e026b8c1435c566463d8eadc8cecc0c459ecf8e75e7cdfbd88cedd861771932dd224762854889aa03')

# Convert known_plaintext to bytes
known_plaintext_bytes = known_plaintext.encode()

# Perform XOR operations
result = bytes(x ^ y ^ z for x, y, z in zip(known_plaintext_bytes, encrypted_text, encrypted_flag))

# Print the result as a hexadecimal string
result_hex = result.hex()
print(result_hex)
```

After we got the result, decode the hex to obtain the flag


[Image extracted text: Recipe
0
Input
D9
4854427b756e7072307433637465645f626230636b636834316e5f73336375723174795f703472346d33743372732121217d0ede8e0e0
From Hex
eOeOede
Delimiter
Auto
116
Raw Bytes
Output
0
M]
:;
HTB{unprOt3cted_
blockch41n_s3curlty
p4r4m3t3rs!! !}so s0 s0 50 50 s0 so sol]


```
HTB{unpr0t3cted_bl0ckch41n_s3cur1ty_p4r4m3t3rs!!!}
```