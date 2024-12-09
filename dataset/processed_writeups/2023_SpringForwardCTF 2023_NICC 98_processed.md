# NICC 98
> Here’s an archive of the original NICC website from when we used to be hosted by Geocities! (Cut us some slack, it was 1998.)

> https://nicc-nicc-98.chals.io/nicc98.html

## About the Challenge
We were given a website about NJIT Information and Cybersecurity Club


[Image extracted text: Welcome to
NICC
NICC 
~NICC
NICC
NICC 
NICC
NICC
NICC
NICC 
NICC 
NICC
NICC 
NICC 
NICC
NICC 
N
NICC
NICC
NICC
NICC
NICC
NICC
NICC
VICC 
NICC
NICC
NICC
NICC
NICC
~NICC
N
NICC
NICC
NICC
NICCI
NICC
NICC 
NICC
NICC
NICC
NICC
NICC
NICCI
NICC
NICC 
NICC
NICC
~NICCI
N
MJIT Information
and Cyber security club
NICC is NJIT'$ official Information & Cybersecurity Club As a student run organization; We aim to give students practical experience in the information security and cybersecurity
N
industries while building engagement and excitement through hands-Ou activities, community building, and networking events
Become_a member!
NICC 
NICC 
~NICC 
NICCI
NICC 
NICCI
NICC 
Joinour IRCchannellCC
NICC 
NICCI
NICC 
NICCI
NICC 
~NICC
N
Next General Body Meeting: 3/11/1998
NICC
NICC
NICC
NICC
NICC
NICC
NICC
You are visitor
number _ICC
NICC
NICC
NICC
NICC 
NICC
~NICC
N
0/2/1/5/2/9]


## How to Solve?
If we check on the source code there is a custom javascript file named `nicc98.js`. The content of the file is

```javascript
console.log("bmljY3tmbGlwX3RoM19zY3JpcHR9");
window.alert("Welcome to the web page of the NJIT Information and Cybersecurity Club!");
console.log("Alert successful.")
```

Decode the `bmljY3tmbGlwX3RoM19zY3JpcHR9` msg using `Base64 decoder` and you will get the flag

```
nicc{flip_th3_script}
```