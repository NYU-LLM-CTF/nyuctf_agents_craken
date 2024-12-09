# Ready Gladiator 0
> Can you make a CoreWars warrior that always loses, no ties?

## About the Challenge
We were given a file called `imp.red` (You can download the file [here](imp.red)) and we need to find a way to make the `Warrior 1` lose


[Image extracted text: ;redcode
;nane
Ex
assert
mov 0,
end
Submit your
Warrior: (enter
'end"
when done)
Warriorl:
;redcode
;nane
Ex
assert
mov 0,
end
Rounds:
100
Warrior
1 wins:
Warrior
wins
Ties
100
again .
Your Warrior
(warrior 1)
must lose all
rounds,
no
ties
Imp
Imp
Try]


Also here is the content of `imp.red`

```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

The code will move the value `1` to register `0`

## How to Solve?
Actually i don't know anything about `CoreWars` code but to solve this I just changed the from value `1` to value `0` to obtain the flag

```
;redcode
;name Imp Ex
;assert 1
mov 0, 0
end
```

And luckily I got the flag


[Image extracted text: ;redcode
;nane
Ex
assert
mov 0,
end
Submit your
Warrior: (enter
'end"
when done)
Warriorl:
;redcode
name
Ex
assert
mov 0,
end
Rounds:
100
Warrior
1 wins:
Warrior
wins
100
Ties
You did itl
picoCTF{h3ro_to_z3r0_Amlrlgh7_fle207c4}
Imp
Imp]


```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}
```