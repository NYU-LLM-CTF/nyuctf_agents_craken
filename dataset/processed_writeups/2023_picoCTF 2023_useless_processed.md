# useless
> There's an interesting script in the user's home directory

## About the Challenge
We were given an access to SSH server and then there is a file called `useless` and if we check the content of the file


[Image extracted text: picoplayer@challenge:~$
15
useless
picoplayer@challenge:~$ cat
useless
#!/bin/bash
Basic mathematical operations
via
command-line arguments
if [ $# != 3 ]
then
echo
"Read the
code first"
else
if [[ "$1"
'add" 1]
then
sum-$( ( $2 + $3 ))
echo
"The
Sum is:
Ssum"
elif [[
"61"
sub" 1]
then
sub-$(( $2 - $3 ))
echo
"The Substract
is:
Ssub"
elif [[
"61"
"div" ]]
then
div-$(( $2 / $3 ))
echo
"The
quotient is: Sdiv"
elif [[ "$1"
"mul" 1]
then
mul-$(( $2 * $3 ))
echo
"The product is:
Smul"
else
echo
"Read the manual"]


## How to Solve?
If we check the source code of the `useless` file, in the `else` block there is a hint. To obtain the flag, we need to read the manual of the file. So im using this command

```shell
man useless
```

Here is the output


[Image extracted text: picoplayer@challenge:~$
man
useless
useless
useless,
This is
simple calculator script
SYNOPSIS
useless, [add
sub mul
div] numberl number2
DESCRIPTION
Use the useless,
macro
to make simple calulations like addition,subtraction, multiplication
and division.
Examples
Luseless add 1 2
This
will add
and
and
return
Juseless mul 2 3
This
will return
as
product of 2
and
Juseless div 6 3
This
will return
as
quotient of
and
Juseless sub 6 5
This
will return
as
remainder 0f substraction of 5
from
Authors
This script
was
designed
and
developed by Cylab Africa
picoCTF{us3l3ss_ch4ll3ng3_Gxploit3d_1888}]


```
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_1888}
```