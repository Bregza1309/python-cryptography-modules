from eliptic_curve import *
from bit_encryption_functions import *
from math import sqrt

class ECC_ENCRYPTION:
    def __init__(self,plaintext,receiver_public,sender_public,a,b,prime,g_point):
        self.a = a
        self.b = b
        self.prime = prime
        self.elliptic_curve = eliptic_curve(a,b,prime)
        self.elliptic_points = self.elliptic_curve.elliptic_points
        self.hex_plaintext = string_to_hex(plaintext)
        self.plain_bytes = []
        i = 0
        while i < len(self.hex_plaintext):
            self.plain_bytes.append(self.hex_plaintext[i:i+2])
            i += 2
        self.receiver_key = receiver_public
        self.sender_key = sender_public
        self.cipher_points = []
        self.g_point  = g_point
        self.order_point = self.elliptic_curve.get_order(self.g_point)
    def koblitz_approach(self):
        
        k = self.order_point
        
        
        for byte in self.plain_bytes:
            m = hex_to_dec(byte)
            j = 0
            while True:
                
                temp_x = (m*k) + j
                temp_y = (pow(temp_x,3) + (self.a * temp_x) + self.b) % self.prime
                quad_residue = temp_y % self.prime
                v = sqrt(quad_residue)
                
                if Is_whole_number(v):
                    
                    self.cipher_points.append([temp_x,int(v)])
                    break
                j+=1
        return self.cipher_points
    def encrypt(self):
        k = self.order_point
        plaintext_points = self.koblitz_approach()
        print(plaintext_points)
        cipher_points = []
        x = self.elliptic_curve.multiply_point_by_n(self.g_point,k)
        mult_p_b = self.elliptic_curve.multiply_point_by_n(self.receiver_key[0],k)
        for point in plaintext_points:
            
            y = self.elliptic_curve.add_points(point,mult_p_b)
            temp_cypher = [x,y]
            cipher_points.append(temp_cypher)
        print(cipher_points)
        return cipher_points
    def decrypt(self):
        plain_points = []
        n = self.receiver_key[1]
        cipher_points = self.encrypt()
        for point in cipher_points:
            x = point[0]
            y = point[1]
            mulT_n_b = self.elliptic_curve.multiply_point_by_n(x,n)
            temp_point = [mulT_n_b[0],-mulT_n_b[1]]
            print(temp_point)
            sub_value = self.elliptic_curve.add_points(y,temp_point)
            return sub_value 

my_session_keys = KEY_GENERATION(4,199,1399)
bregza_key = my_session_keys.user_a
lethu_key = my_session_keys.user_b
g_point = my_session_keys.g_point

encryption_test = ECC_ENCRYPTION('bregza',lethu_key,bregza_key,4,199,1399,g_point).decrypt()
print(encryption_test)
                
                
            
        
         