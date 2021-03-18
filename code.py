global base

#reuired base

base=10
print("base : ",base)

#max no. of digits in a polynomial
limit=300

#total number of points where testing needs to be done
required_point=20
#------------code----------

from cmath import exp
from math import pi
from pdb import set_trace as breakpoint
import time
import matplotlib.pyplot as plt

#to get the polynomial condition 2n<=2^n
def isPowerOfTwo(n):
    return n>0 and (n&(n-1))==0

# FFT using Cooley-Tukey, a divide and conquer algorithm running in O(n log(n)) time implemented reqursively, 
# NOTE that Cooley-Tukey requires n to be a power of two
def FFT(A):
    n = len(A)
    if n==1:
        return A

    assert(isPowerOfTwo(n))

    even = FFT(A[::2])
    odd  = FFT(A[1::2])

    # Numerically stable way of "twiddling"
    return [even[k] + exp(-2*pi*k/n*1j)*odd[k] for k in range(n//2)] +\
           [even[k] - exp(-2*pi*k/n*1j)*odd[k] for k in range(n//2)]

# Inverse FFT
def iFFT(A):
    n = len(A)
    A = FFT([a.conjugate() for a in A])
    return [a.conjugate()/n for a in A]

# Circular convolution in O(nlog(n)) time
def circ_conv(A,B):
    assert(len(A)==len(B))
    n = len(A)
    A = FFT(A)
    B = FFT(B)
    C = [0]*(n)
    for i in range(n):
        C[i]=A[i]*B[i]
    return iFFT(C)

# Polynomial multiplication in O((n+m)log(n+m)) time
def conv(A,B):
    n = len(A)
    m = len(B)
    N = 1
    while N<n+m-1:
        N*=2
    A = A + [0]*(N-n)
    #print(A)
    B = B + [0]*(N-m)
    #print(B)
    C = circ_conv(A,B)
    return C[:n+m-1]

import random
#random.seed(2478721839)
def generate(n,b):
  s=[random.randint(0, b-1) for i in range(n)]
  #print(s)
  for i in range(len(s)):
    if s[i] ==0:
      s[i]=1
  return s
  #print(int(''.join(str(i) for i in s)))

def normal_multiply(a,b):
  b1=1
  sum=0
  for i in range(len(a)):
    a_element=a[i]*b1
    b2=1
    for j in range(len(b)):
      b_element=b[j]*b2
      sum=sum+a_element*b_element
      b2=b2*base
    b1=b1*base
  return sum

l1=[]
l2=[]
l3=[]

# limit=400
# required_point=5
for length in range(1,limit,int(limit/required_point)):
  l1.append(length)
  # Multiply (1+2x+3x^2) and (2+3x+4x^2+5x^3)
  A = generate(length,base)
  B = generate(length,base)
  t = time.time()
  z=conv(A,B)


  n=len(z)-1
  sum=0
  for i in range(len(z)):
      z[i]=round(z[i].real)  #rounding is done make the real part of each element of FFT as closest integer.
      sum=sum+z[i]*pow(base,n)
      n=n-1
  fast_mul=int(sum)
  t = time.time()-t
  l2.append(t)

  a=(int(''.join(str(i) for i in A)))
  b=(int(''.join(str(i) for i in B)))
  #mul=int(a*b)
  A=A[::-1]
  B=B[::-1]
  t = time.time()
  mul=normal_multiply(A,B)
  t = time.time()-t
  l3.append(t)
  # if fast_mul==mul:
  #   #print(f"{a} * {b} = {fast_mul} , {mul} ,same, time:{t}")
  #   print("same")
  # else:
  #   print(f"{a} * {b} = {fast_mul} , {mul} ,not_same")

#import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
# x axis values 
x = l1
  
# plotting the points  
plt.plot(x, l2,label='FFT multiplication')
plt.plot(x, l3,label='normal multiplication') 

# naming the x axis 
plt.xlabel('length') 
# naming the y axis 
plt.ylabel('time') 
  
# giving a title to my graph 
plt.title('comparison graph with base '+str(base)) 
  
# function to show the plot 
#plt.axis([0, limit, 0, 0.0001+max(max(l2),max(l3))])
plt.legend()
plt.savefig('comparison graph with base '+str(base)+'.jpg')
plt.show()