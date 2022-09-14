from key_generation import * 
from SHA_512 import SHA512 ;

#get global variable p and a
t_global = Global_Public_Elements();

#generate user keys
t_public = user_key_generation(t_global);

def get_k(q):
    """Calculates k for Elgamal digital signature"""
    k = choice(list(range(1,q)))
    if(gcd(k ,q-1) != 1):
        return get_k(k);
    
    return k
# signing a message
def _d_sign_(public_key , message):
    """Signs a message using public_key and sha512"""
    #derive public elements
    q = public_key[0]
    print("q = "+ str(q))
    a = public_key[1]
    Ya = public_key[2]
    Xa = public_key[3]
    
    #calculate hash for message
    m_hash = SHA512(message).hash()
    
    #divide hash into bytes and store them in blocks
    blocks = blockulator(m_hash,2)
    
    #randomly choose k
    k = get_k(q);
    
    #compute s1
    s1 = pow(a,k) % q
    
    #compute k inverse
    euler_value = Eulers_totient(q)
    k_inverse = get_inverse(q,k)
    print(k_inverse)
    #loop through the blocks and join into s2
    s2 = ""
    for block in blocks:
        m = hex_to_dec(block)
        print(f"m = "+ str(m))
        temp = (k_inverse) * (m-(Xa * s1)) % (q)
        print(temp)
        s2 += binary_to_hex(dec_to_binary(temp))
    return [s1,s2]
        
            
     
    
    
print(_d_sign_(t_public,plaintext));
