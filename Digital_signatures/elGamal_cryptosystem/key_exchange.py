from random import choice
from functions import *
def get_primitive_root(prime):
    n = Eulers_totient(prime)
    roots = []
    for i in range(1,prime):
        test = []
        for j in range(1,int(prime)):
            temp = pow(i,j) % int(prime)
            test.append(temp)
        c = 0
        for b in range(1,int(prime)):
            c = test.count(b)
        if c == 1:
            roots.append(i)
    return choice(roots)

      
def Global_Public_Elements():
    
    prime_nums = []
    for i in range(255,1000):
        isPrime = True
        for b in range(2,i):
            
            if i % b == 0:
                isPrime = False
        if isPrime:
            if i % 4 == 3:

                prime_nums.append((i))             

    p = choice(prime_nums)
    a = get_primitive_root(p)
    return [p,a]
public_elements = Global_Public_Elements()

def key_generation(p,a):
    domain = list(range(1,p))
    private_value = choice(domain)
    public_value = pow(a,private_value) % p
    return [public_value,private_value]
user_a_public = key_generation(public_elements[0],public_elements[1])
user_b_public = key_generation(public_elements[0],public_elements[1])


def secret_key(y ,x ,p):
    key = pow(y,x) % p
    return key
