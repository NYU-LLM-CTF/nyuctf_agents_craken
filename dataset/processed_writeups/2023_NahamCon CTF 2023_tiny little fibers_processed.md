# tiny little fibers
> Oh wow, it's another of everyone's favorite. But we like to try and turn the ordinary into extraordinary!

## About the Challenge

We given the image file, and we need analyze to find flag

[images](images/tiny-little-fibers)

## How to Solve

To solve this, all you need is `stegsolve`

You can download here [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)

But before you open it to stegsolve, make sure already add the `.jpeg` extension

After that `Analyse` > `File Format`, just slowly scroll down and you got flag


[Image extracted text: 4bfa5893a27c5832 d231370316025816
72e113217115e2f8 cf3fffd9
Ascii:
fla .
2. {.2._
2.0.5..
3.4.0_
5.a.b.
e.a.8.
4b.f.
6.c.1_
1.9.3_
e.2.6 .-
3.f7 
2.5.9.
f}]


```
flag{22c534c5abea84bf6c1193e263f7259f}
```