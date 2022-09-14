from random import choice
from fractions import Fraction
from functions import *
def get_multiplicative_inverse(a,p):
    p = int(p)
    a = int(a)
    euler_value = Eulers_totient(p)
    inverse_value = pow(a,euler_value-1)
    return inverse_value
    
class eliptic_curve:
    def __init__(self , a ,b ,q):
        self.a = int(a)
        self.b = int(b)
        self.q = int(q)
        self.elliptic_points = []
    def get_points(self):
        a = self.a
        b = self.b
        q = self.q
        if (pow((4*a),3) + pow((27*b),2)) != 0 :
            eliptic_points = []
            for x in range(0,q):
                for y in range(0,q):
                    
                    v = pow(y,2) % q 
                    g = ((pow(x,3)+ (a*x) + b)) % q
                    if v == g :
                        eliptic_points.append([x,y])
                    
                
                
                
        
        domain = list(range(0,len(eliptic_points)))
        
        self.elliptic_points = eliptic_points
        while True :
            j = choice(domain)
            temp_point = eliptic_points[j]
            n = self.get_order(temp_point)
            if n > 200:
                break
            
            
        return temp_point 
    def add_points(self,p,h):
        r = []
       
        x_p = p[0]
        y_p = p[1]
        x_h = h[0]
        y_h = h[1]
        numerator = y_p - y_h
        denominator = x_p - x_h
        lamda = (numerator * get_multiplicative_inverse(denominator , self.q)) % self.q
        r.append((pow(lamda,2) - x_p  -x_h) % self.q)
        r.append((lamda * (x_p - r[0]) - y_p)  % self.q) 
        return r
    def get_order(self, point):
        
        
        zero_point = self.add_points(point,[point[0],-point[1]])
        
        
         
        x = point[0]
        y = point[1]
        r = []
        b = 1
        
                
        
        
        while True:
            if r == zero_point:
                break
            else:
                    denominator = (2*y)
                    numerator = ((3*pow(x,2)) + self.a) % self.q
                    
                    lamda = (numerator * get_multiplicative_inverse(denominator,self.q)) % self.q
                    r.append((pow(lamda,2) - (2* x)) % self.q)
                    r.append((lamda*(x - r[0]) - y) % self.q)
                    r = self.add_points(point,r)
                                
                    
            b+=1 
        
        return b
    def multiply_point_by_n(self,point,n):
        zero_point = self.add_points(point,[point[0],-point[1]])
        n = int(n)
        
         
        x = point[0]
        y = point[1]
        r = []
        b = 1
        
                
        
        
        while b != n:
            if r == zero_point:
                break
            else:
                    denominator = (2*y)
                    numerator = ((3*pow(x,2)) + self.a) % self.q
                    
                    lamda = (numerator * get_multiplicative_inverse(denominator,self.q)) % self.q
                    r.append((pow(lamda,2) - (2* x)) % self.q)
                    r.append((lamda*(x - r[0]) - y) % self.q)
                    r = self.add_points(point,r)
                                
                    
            b+=1 
        
        return r



class KEY_GENERATION:
    def __init__(self,a,b,prime):
        self.elliptic_curve = eliptic_curve(a,b,prime)
        
        self.elliptic_points = self.elliptic_curve.elliptic_points
        self.g_point = self.elliptic_curve.get_points()
        self.order_n = self.elliptic_curve.get_order(self.g_point)
        self.calculate_user_keys()
        
        
        
    def User_key_generation(self,n ,point):
        n = int(n)
        domain = list(range(100,n))
        private_value = choice(domain)
        public_key = self.elliptic_curve.multiply_point_by_n(point,private_value)
        return [public_key,private_value]
    
    def calculate_user_keys(self):
        while True:
            
            self.user_a = self.User_key_generation(self.order_n,self.g_point)
            self.user_b = self.User_key_generation(self.order_n,self.g_point)
            secret_key = self.secret_key()
            if secret_key:
                break
        
    def secret_key(self):
        key_1 = self.elliptic_curve.multiply_point_by_n(self.user_a[0], self.user_b[1])
        
        key_2 = self.elliptic_curve.multiply_point_by_n(self.user_b[0], self.user_a[1])
        
        if key_1 == key_2:
            return True
        else:
            return False
        
    

