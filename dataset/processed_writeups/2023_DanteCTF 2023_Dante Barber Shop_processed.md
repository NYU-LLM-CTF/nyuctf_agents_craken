# Dante Barber Shop
> Welcome to our renowned barber shop! Your task, should you choose to accept it, is to uncover hidden information and retrieve the sensitive data that the owners may have left around.

## About the Challenge
We were given a website about barber, there are 6 images in the homepage


[Image extracted text: Login
Welcome to Dante Barber Shop
Dante Barber Shop, located in Florence , takes inspiration from the renowned Italian
Dante Alighieri. Our
skilled barbers provide exceptional grooming services, combining traditional techniques with modern styles. Step
into our shop and experience the art of barbering in a warm and inviting atmosphere
We pride ourselves on
delivering personalized haircuts and beard trims to enhance your unique style
Our attention to detail and
commitment to customer satisfaction make us the go-to barbershop in the city: Don't forget to browse through the
pictures below to
a glimpse of our impeccable craftsmanship.
poet
get]


And also there is an admin panel functionality


[Image extracted text: Welcome to Dante
Barber Shop
Username:
Password:
Log in]


## How to Solve?
At first, I tried to bypass the login by using SQL and NoSQL injection payloads, but the attempt failed. Then, I checked the homepage and noticed something peculiar about the filenames of each image.


[Image extracted text: Our
attention
to
detail
commitment
customer
satisfaction
make
the
Don
forget
browse
through
the pictures
below
glimpse
of
our
impec
<[p>
<div
class=
image-grid">
src=
ingLbarber2_jpg"
alt=
Barber Shop
<img src="img[barber3_jpg
alt=
Barber
Shop
<img
src-"imgLbarberA-jpg
alt=
Barber Shop
src=
img[barber5_jpg
alt=
Barber
Shop"
<img src-"imgLbarber6_jpg
alt=
Barber Shop
src=
img[barberl_jpg
alt=
Barber
Shop
5
<div>
<div>
</body>
<fhtml>
and
get
<img
<img
<img]


Because `barber1.jpg` was missing, I tried to access the image by visiting `https://barbershop.challs.dantectf.it/img/barber1.jpg`, and luckily, we obtained a user credential.


[Image extracted text: < >
C
barbershopchalls dantectfit img/barber1
Backup User
barber
dant3barbershOp_cLIVeSidag
ljpg]


Use that credential to login to the website, and inside the admin panel, there is a search functinality and also a table containing customer list


[Image extracted text: Welcome; barberl
No flag for youl But you can check the list of customers!
Enter a keyword
Search
Customers:
Name
Surname
Phone
Alessandro
Rossi
+39 333 1234567
Beatrice
Bianchi
+39 335 2345678
Carlo
Ricci
+39 338 3456789
Davide
Marini
+39 340 4567890
Elena
Ferrari
+39 342 5678901
Federico
Romano
+39 344 6789012
Giulia
Gallo
+39 346 7890123
Hugo
Conti
+39 348 8901234
Isabella
De Luca
+39 350 9012345
Jacopo
Bruno
+39 352 0123456
Ludovica
Russo
+39 354 1234567
Matteo
Santoro
+39 356 2345678]


This functionality was vulnerable to SQLite injection, and in this case I will extract the admin credential using this payload

```
' union select 1,(SELECT username from users),(SELECT password from users),4-- -
```


[Image extracted text: Welcome; barberl
No
for youl But you can check the list of customers!
Enter a keyword
Search
Search result:
Name
Surname
Phone
Alessandro
Rossi
+39 333 1234567
admin
nSOrowLIstERiMbrUsHConesueyeadEr
Beatrice
Bianchi
+39 335 2345678
Carlo
Ricci
+39 338 3456789
flag]


Use that admin credential to login to admin panel again to obtain the flag


[Image extracted text: Welcome; admin!
DANTE{dant3_Is_inj3cting_everybOdy_aaxxaa}
Enter a keyword
Search
Customers:
Name
Surname
Phone
Alessandro
Rossi
+39 333 1234567
Beatrice
Bianchi
+39 335 2345678
Carlo
Ricci
+39 338 3456789
Davide
Marini
+39 340 4567890
Elena
Ferrari
+39 342 5678901
Federico
Romano
+39 344 6789012
Giulia
Gallo
+39 346 7890123]


```
DANTE{dant3_1s_inj3cting_everyb0dy_aaxxaa}
```