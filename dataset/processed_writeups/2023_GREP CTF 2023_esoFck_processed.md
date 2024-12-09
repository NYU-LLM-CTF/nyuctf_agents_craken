# esoF*ck
> I've heard about brainf#ck but what the f#ck js this?

## About the Challenge
We were given a file (You can download the file [here](msg.txt)) and we need to decode it to obtain the flag

## How to Solve?
First, we need to remove `f#ck` keyword from the msg, and then here is the result


[Image extracted text: GREP CTF 2023
esoFck
txt
[J[([J+[J)[+[1J+(![+[J)[ !+[J++[1J+(![J+[D)[+!+[JJ+(W[J+[J)[+[JII[([I[([J+[J)[+[1J+(![J+[J)[ !+[J++[1J+(![J+[J)[++[1+(W[]
+[J)[+[JIJ+[J) [ !+[J++[J++[1J+(![J+[J[(![J+[J)[+[1J+(![+[J)[ !+[J++[1J+(![J+[D)[+!+[]J+(W[J+[J)[+[JI1)[++[J+[+[J]+([J[[]]
+[J)[++[JJ+(![J+[J)[ !+[J+!+[J++[1J+(W[J+[I)[+[1J+(![Z+[J)[++[JJ+([J[[]]+[J)[+[ZJ+([J[(![+[J)[+[1J+(![J+[J) [ !+[J++[1J+(![]
+[J)[++[1J+(W[#+[J)[+[JIJ+[J)[ W+[J+!+[J+!+[1J+(W![J+[J)[+[1J+(W[J+[J[(![J+[J)[+[1J+(![J+[J)[!+[J++[1J+(![J+[J) [++[1J+(W[]
+[I)[+[IHI)[+!+[J+[+[J]J+(W[]+[J)[+!+[JI([J[(![J+[J)[+[IJ+(![J+[J)[!+[J+!+[1J+(![J+[J) [+!+[1J+(W[Z+[J)[+[III[([I[([J+[J)[+[J]
+([H+[I) [ !+[J+!+[J]+(![J+[1)[+!+[JJ+(W[]+[I)[+[JI#+[J)[!+[J+!+[J+!+[JJ+(W[Z+[J[([J+[J)[+[JZ+('[J+[I)[!+[J+!+[IJ+(![J+[I) [+!
+[1J+(V[J+[J) [+[JII) [++[J+[+[IJ+([JI[]J+[J)[+!+[JJ+(![J+[J)[ !+[J+!+[J++[JJ+(
[J+[J)[+[1J+(W[J+[J)[+!+[JJ+([J[[I]+[J)[+[J]
+([I[([#+[D)[+[1Z+( [#+[I)[!+[J+!+[1J+(![]+[1) [++[IJ+(V[J+[J)[+[II#+[1)[J+[J+!+[J+!+[J+([h+[1)[+[I]+(W![]+[I[('[]+[I) [+[1]
+([J+[I)[ !+[J++[1J+(![J+[J)[++[1J+(W[J+[I)[+[JJ]) [++[J+[+[J]]+(V[J+[J)[++[JJJ(([J+[J)[++[1J+(W[J+[J)[ !+[J++[J+W+[]]
+(V[J+[J)[+[IJ+([I[[I]+[J)[+[1J+(![J+[J)[++[ZJ+([J[[]Z+[J)[+!+[JJ+([+[J)[(![J+[J)[+[1J+(V[J+[J[([J+[D)[+[1J+(![J+[J)[ !+[J+!
+[1J+(![J+[J)[++[1J+(![J+[J)[+[JJ1) [++[J+[+[J]]+([J[[I+[J)[++[1J+(![J+[J)[+[ZJ+([J[(![J+[J)[+[1J+( ![J+[J)[ !+[J++[JJ+(![]
+[J)[++[1J+(W[#+[J)[+[JIJ+[J)[ W+[J+!+[J+!+[1J+(W[J+[J[(![J+[J)[+[J+(![J+[J)[ !+[J+W+[1J+( ![J+[J)[+!+[1J+(W[J+[J)[+[JJ1)[++[]
+[+[JJJ+(![J+[J)[!+[J+!+[1J+(W[J+[J[C[J+[D)[+[1J+(![J+[J) [ !+[J++[1J+(![J+[J)[+!+[1J+(![J+[J) [+[JJ1) [++[J+[+[JIJ+(W[J+[I)[+!
+[JJJO[++[J+[ !+[J++[JlJ+((![J+[J)[+[1J+[++[1J+[ !+[J++[J++[J+!+[J+[ !+[J+!+[J++[J++[J++[J++[J+!+[1J+(W[J+[J)[+W+[JJ+( !
msg t]


And then find JSFuck decoder (In this case, im using [dcode.fr](https://www.dcode.fr/jsfuck-language)) and here is the output


[Image extracted text: intormatics
Programming Language
JSFuck Language [JI([+[J)
Sum
JSFUcK DECODER
Search for a tool
JSF
(SOURCE) CODE WRITTEN IN JSFUCK
JSF
SEARCH
TOOL
ON DCODE BY KEYWORDS:
H-Ej5
Whz
g. type 'boolean'
[i-[])
Hov
BROWSE THE FULL DCODE TOOLS LIST
JSFuc
Results
Ehhf
Hov
grepCTF{3sot3rlc_14ngu4g3s_ftw}
MODEO
DISPLAY AS JAVASCRIPT (CONVERSION TO NATIVE / UNOBFUSCATED)
interp
JSFuc
ExECUTE THE CODE (4 AT YOUR OWN RISK)
Whe
DECODE
Hov
50% discount
See also: Brainfuck
Sim-
JSFUcK DECODER]


```
grepCTF{3sot3r1c_l4ngu4g3s_ftw}
```