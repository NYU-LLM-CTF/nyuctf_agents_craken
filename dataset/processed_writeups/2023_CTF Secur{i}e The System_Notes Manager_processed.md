# Notes Manager

> You are a penetration tester hired by a small company who got their website hacked recently. They said the hacker somehow got administrative privilege to the website, but there were no logs indicated that an our main admin account was used in other IP Address else than our administrator IP Address. Can you help this company to find the vulnerabilities so that they can patch it ASAP?

## About the Challenge
We were given a website without the source code, and there are some functionality such as:
* Register
* Login
* Setting acount
* Create our note
* See our note
* Lock our note


[Image extracted text: NotesManager
Login to start your session:
Username
Password
Login
Register a new account]


## How to Solve?
To obtain the flag, we need to first change our role from `user` to `admin` in the settings menu. (When I solved this challenge, the author accidentally added a `role` parameter to the account settings form)


[Image extracted text: Request Data
MIME Type: application/x-V
name: test
gender: female
role: admin]


After obtaining the `admin` role, we need to check the locked note that contains the flag.


[Image extracted text: Notes
Show
10
entries
Search:
Title
Secured
Action
FLAG
Don't open this:
TODO
Showing 1 to 3 of 3 entries
Previous
1
Next]


We can bypass it by accessing the note directly (There is a note UUID in the body).


[Image extracted text: <tr>
<td class-"align-middle">FLAG</td>
<td class-"text-center align-middle">
<i
class-"fa-solid fa-lock"><li>
<ltd>
<td class-"text-center align-middle">
<a href="#" class-"btn btn-sm btn-outline-primary"
<1
class-"fa-solid fa-eye"
onclick-"viewSecuredNote( 'a6faca0d-7e51-4b02-834f-c7b11370056f ')"><li>
<la>
<ltd>]



[Image extracted text: 178.128.113.198:1337/notes/a6facaOd-7e51-4602-834f-c7b11370056f
Create Note
Content:
Notes
STS23BlAckbox_Ch4Il_FOr_Anoth3r_D4y}]


```
STS23{Bl4ckb0x_Ch4ll_F0r_An0th3r_D4y}
```