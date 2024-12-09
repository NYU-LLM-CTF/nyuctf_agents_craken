# college-tour
> Welcome to UCLA! To explore the #1 public college, we have prepared a scavenger hunt for you to walk all around the beautiful campus.

## About the Challenge
We were given a website and we need to find 6 parts of the flag. Here is the preview of the website


[Image extracted text: tour of UCLA
Click me for Light Model
After finally setting foot on UCLA's campus, youre excited to explore it: However, the new student advisors have
hidden six clues in the format lactf{number_text} all across UCLA To complete the scavenger hunt, you must
merge all the parts into one in order. For example, if you find the clues lactf{I_IOsT} lactf{2
JIN_b} (note the
repeated underscore); and lactf{3_03LT3r}, the answer is lactf{IOsT_IN_bO3LT3r} Have fun exploring!]


## How to Solve?
We need to check the source code first and I found 3 flag parts in the homepage
```
lactf{1_j03_4}
lactf{2_nd_j0}
lactf{4_n3_bR}
```


[Image extracted text: <button
id-"dark
mode
button
onclick=
dark_mode( )" Click
me
<p>
After finally setting
foot
UCLA
campus_
you
excitec
<4 -
lactf{l_j03_4}--
src=
royce_jpg"
alt="lactf{2_nd_j0}"
height="40Opx
<iframe
src=
lactf{4_n3_bR}_pdf"
width="100%'
height="500px'
<img]


And then there is css and js file. In the css file I found 1 flag parts
```
lactf{3_S3phI}
```


[Image extracted text: secret
font
family:
"lactf{3_S3phI}]


And in the js file, I found 2 flag parts
```
lactf{5_U1n_s}
lactf{6_AY_hi}
```


[Image extracted text: else
document
getElementById (
dark_mode_
button
).textContent
"Click
for lactf{6_AY_hi}
Mode!
window.addEventlistener("load"
(event)
=>
document
cookie
cookie-lactf{5_Uln_s}
});]


After that we need to combine each part to know the final flag

```
lactf{j03_4nd_j0S3phIn3_bRU1n_sAY_hi}
```