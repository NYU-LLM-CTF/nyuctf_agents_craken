# Track a coin from your crypto O valley of plenty

> During the investigation in one of the cases, our forensics analysts were tasked with tracing the following transaction hash which occured on a trial network, and get the first address who sent money. Could you find that address?
> Transaction Hash:0xa150ff06619b927cc323f16984a679a24b07265f1c1a664f1c729177929cebae

## About the Challenge

We need to find the first wallet address who sent money using the transaction hash

## How to Solve

First we analyze the transaction hash it's look like a ethereum. But the ethereum has network testnet which is has different transaction hash.

I search some the testnet and i found this


[Image extracted text: [Image not found]]


After some attemps, i know the transaction hash is from `Sepolia` testnet, you can use this web to track the transaction hash [Sepolia Etherscan](https://sepolia.etherscan.io/)

And i found the transaction hash details


[Image extracted text: [Image not found]]


Then i do some scrolling and found the first wallet address who's have sent the money


[Image extracted text: [Image not found]]


```
ASCWG{0xEDaf4083F29753753d0Cd6c3C50ACEb08c87b5BD}
```