# Vigenere XOR
> Leonard forgot to tell you the key he used to encrypt his message.

> Would you be able to recover the message he sent you ?

> Flag format: dvCTF{[REDACTED]} found in the message

## About the Challenge
We were given a file that contains encrypted message (You can download the file here)

## How to Solve?
At first, I thought this is a binary but when I read the title I decided to decrypt the message using XOR decoder by dcode.fr. Use automatic bruteforce and then check the message that has been decrypted using `435239505430` key


[Image extracted text: 485239504536
#TK3YNER_FR
;ED}
1_n]]
ugee
You did itl
The flag
435239505430
dvCTF {80R3D_K3Y_15_K3
Y_MY_FRIZND} .
We1
Cone
Rou
rio it7
_he pljg
485239504230
OVCTP{30R3R_@3Y_' STK3]


```
dvCTF{80R3D_K3Y_15_K3Y_MY_FR13ND}
```