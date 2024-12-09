# Trapped Source
> Intergalactic Ministry of Spies tested Pandora's movement and intelligence abilities. She found herself locked in a room with no apparent means of escape. Her task was to unlock the door and make her way out. Can you help her in opening the door?

## About the Challenge
We were given a website which contains a calculator. We have to be able to guess the pin number to get the flag


[Image extracted text: LOCKED
Clear
Enter]


## How to Solve?
To get the correct pin, check the source code and you will see on line 18 it has the correct pin number


[Image extracted text: dy>
(script>
window.CONFIG
window.CONFIG | 
buildNumber:
v201908167
debug
false,
modelName
Valencia
correctPin:
"8291"
<[script>
<div
class=
lockbox
{div
class=
lockStatus
>LOCKED< /div>
<div
class=
lockMid
<span
id=
btn9
classz"button
onclick="unlock(9)">9</span>
Gan
ids"btn8
classs"button
onclick=
unlock( &
84 | Shan>]


Enter `8291` in the calculator and you will get the flag


[Image extracted text: HTB {VI3w_Sourc3
C4n_b3_us3tul!
Clear
Enter]


```
HTB{V13w_50urc3_c4n_b3_u53ful!!!}
```