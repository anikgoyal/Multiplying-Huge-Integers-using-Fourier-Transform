# Multiplying-Huge-Integers-using-Fourier-Transform:

# Problem Statement:
The problem is that traditional approaches to multiplication requires O(n^2) multiplication operations, where n is the number of digits.

To see why, assume for example that we want to multiply the numbers 123 and 456. The normal way to do this as follows:

![image](https://user-images.githubusercontent.com/57549021/111580797-28af5200-87de-11eb-8ccb-e2cfcd7a8454.png)

We see that for two integers of length 3, this multiplication requires 3 × 3 = 9 operations, hence its complexity is O(n^2). 

What about this one?
![image](https://user-images.githubusercontent.com/57549021/111580860-48467a80-87de-11eb-96b2-dfe3274769d3.png)

Executing an O(n^2) algorithm for huge n is very costly, so that is why it is preferred to use more efficient algorithms when multiplying huge integers.

One way to do this more efficiently in O(nlogn), is by using FFT
