# Apps
> I made a small app when I was 9 years old first learning to code.

## About the Challenge
We were given a file (You can download the file [here](CTF.aia)) and we need to do reverse engineering in order to get the flag

## How to Solve?
Im using this [website](https://filext.com/file-extension/AIA) to analyze the file. And we got this structure


[Image extracted text: src/
appinventor/
ai_23saahilt/
CTF/
Screen1
Screen1.scm
youngandroidproject/
project-properties
bky]


Read the `Screen1.bky` file to obtain the flag


[Image extracted text: d="t%xoRZuLP+tP53RSYgSW" > <mutation component_type=
TextBox"
set_
_generic=
false" instance_name=
TextBox1
x(/mutation><field
name
ame=
PROP">Text< /field><value
name="VALUE
xblock
type="text
id=
ame=
TEXT
bucket {Mit_
4PP
1NV3NTOR_bf0285c53}
[field></block></va
/block>< /statement)</block></statement></block><yacodeblocks
ya -
Iyacodeblocks><_
Xml>]


```
bucket{M1T_4PP_1NV3NT0R_bf0285c53}
```