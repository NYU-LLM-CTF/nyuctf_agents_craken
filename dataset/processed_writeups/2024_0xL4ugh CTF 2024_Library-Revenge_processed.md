# Library-Revenge
> Built a book library, however my friend says that i made a really nasty mistake!

## About the Challenge
We got a server to connect and a source code (You can download the source code [here](Library-revenge-misc.zip))

This program has many functions. For example, we can add a member, search for a book, etc


[Image extracted text: Library
Management
System
1
Add Member
2
Add
Book
3
Display
Books
Search
Book
5
Check
Out
Book
6 _
Return
Book
7_
Save
Book
8
Check File
Presence
0
Exit]


## How to Solve?
This program is vulnerable to format string vulnerability where we can access other attributes (You can check more about the vulnerability [here](https://podalirius.net/en/articles/python-format-string-vulnerabilities/))

```python
        elif choice == "7":
            choice = console.input("\n[bold blue]Book Manager:[/bold blue]\n1. Save Existing\n2. Create new book\n[bold blue]Enter your choice (1-2): [/bold blue]")
            if choice == "1":
                title = console.input("[bold blue]Enter Book title to save: [/bold blue]").strip()
                file = SaveFile(library.display_books(title=title))
                save_book(file.file, content="Hello World")
            else:
                save_file = SaveFile()
                title = console.input("[bold blue]Enter book title: [/bold blue]").strip()
                author = console.input("[bold blue]Enter book author: [/bold blue]")
                isbn = console.input("[bold blue]Enter book ISBN: [/bold blue]")
                num_copies = int(console.input("[bold blue]Enter number of copies: [/bold blue]"))
                title = title.format(file=save_file)
                book = Book(title,author, isbn)
                isbn_to_book[isbn] = book
                library.add_book(book, num_copies)
                save_book(title)
```

So, if we input `{file.__init__.__globals__}` in the book title, we can read the value of the `FLAG` variable.


[Image extracted text: Book Manager:
1
Save
Existing
2
Create
new
book
Enter
your
choice
(1-2) :
Enter
book
title:
{file.
init__'__globals__}
Enter
book
author:
Enter
book
ISBN:
Enter
number
of
copies:
Error:
[Errno
2]
No
such
file
or
directory:
"{'__name
main__"
~_doc__
None
~package
None ,
loader
frozen_importlib_external.SourceFileLoader
object
at
0x7f5b076227d0>
spec_
None
annotations_
{} ,
builtins
<module
builtins'
(built-in)>
file_
Thome/challenger/challenge. py
cached
None ,
Console
<class
rich.console.Console
> ,
re
<module
re
from
lusr/lib/python3
1l/re/_
init___
py
> ,
shlex
<module
shlex
from
lusr/lib/python3.11/shlex.pY
>
05
<module
05
(frozen) > ,
FLAG '
OxL4ugh {TrUSt
M3_LiF3_I5
H4rD3r
Wizheuz
4_W1f3!}'
console'
<console
width-80
None>
Member
<class
main
Member
> ,
Book
<class
main__ _
Book
> ,
BookCopy
<class
main__
BookCopy
> ,
SaveFile
<class
Fnn
CaCi7-
E i

Fnn
3
3Le
In]


```
0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r_Wi7h0u7_4_W1f3!}
```