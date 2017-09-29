# Homework 03

------

## The exercise 1.1

The velocity of a freely falling object near Earth's surface is described by the equation

![photo](https://github.com/kammmmmi/photos/blob/master/VNWNB%5DT%25N7H%7DNAJ%7B34K%24%5BE9.png)(1.8)

Where *v* is the verlocity and $g = 9.8m/s^2$ is the acceleration due to gravity.Write a proggram that employs the Euler method to compute the solution to(1.8）；that is,calcilate *v* as afunction of *t*.For simplicity,assume that the initial velocity is zero-that is,the object starts from rest-and calculate the solution for times *t*=0 to *t*=10s.Repeat the calculation for several different values of the time step,and compare the results with the exact solution to (1.8).It turns out that for this case the Euler method gives the exact result.Verify this with your nymerical resulet and prove it analytically.

### Numerical approach:
 
由题意得 

![123](https://github.com/kammmmmi/photos/blob/master/%25NEA%60ULA1GW%5BFWC0FN_R~5W.png)
 
对其泰勒展开
 
$$v(t+\Deltat)=v(t)=

