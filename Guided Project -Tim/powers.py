
# given a and b, return a ** b, without using the inbuilt operator

# Understand
## one way: a single number being multiplied by itself, as many times the second number
## Valid and invalid inputs
### invalid: letters
### valid: any number whatsoever

### maybe no negative numbers for b? 2 ** -2 == 1/4
#### 1/( 2 ** 2 )
### for a negative number for b, put a 1 over the whole operation

### Square root with a power: raise to 1/2, 0.5
### i = sqrt(-1) == (-1)**0.5

## What if b == 0? What's 2^0? Anything to the power of 0 is 1

### Let's not handle decimal numbers for b

## Plan
### We have two numbers, one or both may be negative

### Iterative or recursive?

### 2^3
### a = 2, b = 1
### Iterative pseudocode
#### check if b == 0, if so return 1
#### have a counter == a
#### while loop: while b isn't 1
##### multiply the counter by a
##### decrement b to approach 1
#### return counter

## a = 2, b = 0
## counter = 16

def iter_power_v1(a, b):
#### check if b == 0, if so return 1
    if b == 0:
        return 1
#### have a counter == a
    product = a
#### while loop: while b isn't 1
    while b != 1:
##### multiply the counter by a
        product *= a
##### decrement b to approach 1
        b -= 1
#### return counter
    return product

## Review
### Handle positive values for a and b successfully
### And values of 0 for b!
### But not negative

## negative values for b --> 2^-2 --> 1/4
## decimal value for b

### Iterative pseudocode
#### check if b is an integer, otherwise return error message
#### check if b == 0, if so return 1
#### check if b < 0: if so, multiply by -1, set invert to True
#### have a counter == a
#### while loop: while b isn't 1
##### multiply the counter by a
##### decrement b to approach 1
#### return counter

### Iterative pseudocode
def iter_power(a, b):
#### check if b is an integer, otherwise return error message
    if type(b) is not int:
        return "Sorry we don't handle decimals"

#### check if b == 0, if so return 1
    if b == 0:
        return 1
#### check if b < 0: if so, multiply by -1, set invert to True
    invert = False
    if b < 0:
        b *= -1
        invert = True

#### have a counter == a
    product = a
#### while loop: while b isn't 1
    while b != 1:
##### multiply the counter by a
        product *= a
##### decrement b to approach 1
        b -= 1
#### return counter

    if invert:
        return 1 / product
    else:
        return product

print(iter_power(2, 3) == (2 ** 3))
print(iter_power(10, 2) == (10 ** 2))
print(iter_power(10, 0) == (10 ** 0))
print(iter_power(2, -2) == (2 ** -2))
print(iter_power(2, 1) == (2))
print(iter_power(100, 1) == 100)

