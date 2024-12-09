# 3 Strikes and you're out!


[Image extracted text: TRA
strik]


## About the Challenge

We given some images looks like hint for the challenge, and also try to find the right publication of tenable

## How to Solve

First when we see the image, it's look like a cutted image and i found this 


[Image extracted text: [Image not found]]


It's a logo from `CMS Strikingly`, so let's dig deeper

And then i found this 


[Image extracted text: [Image not found]]


We try to visit the publication article and view source the article

We found something

```
<!-- be bg a_ bf bc a_ bf bc a_ bf b_ a_ bf bb a_ bb e` a_ ba ee a_ ba ee a_ bf bf a_ bf bf a_ bf bf a_ ba ed a_ bf bc a_ be bd a_ be ed a_ be b` a_ be ba a_ be eb a_ be bd a_ ba ed a_ be bb a_ be ee a_ be ec a_ ba ee a_ bf bb a_ be bd a_ be bb a_ bf bd a_ bf ba a_ be bh a_ bf bc a_ bf bh a_ ba ee a_ bf ba a_ be bd a_ bf bb a_ be bd a_ be b` a_ bf ba a_ be bb a_ be bg a_ ba ee a_ bf bc a_ bf ba a_ be b` a_ ba ec a_ bb ba a_ bb b_ a_ bb ba a_ bb bb a_ ba ec a_ bb ba a_ bb b_ -->
```

Then we try to decode it


[Image extracted text: [Image not found]]


We got a url, so let's visit it and get the view source


[Image extracted text: [Image not found]]


In the caption we need `231 CPUs` maybe it's more like `231 CVE` right?

So we googled it 


[Image extracted text: [Image not found]]


View source the article and we got something


[Image extracted text: [Image not found]]


And we decode it


[Image extracted text: [Image not found]]


```
flag{d3Cod3_d@_iNT3Rn3Tz}
```