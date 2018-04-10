
# coding: utf-8

# In[ ]:


a = int(input('Please type a number : '))
b = int(input('Please type a number : '))
def compute_gcd(a,b): 
    if a>b:
        r=a%b
        if r==0:
            return b
        else:
            a=r
            return(compute_gcd(a,b))
        
    elif a<b:
        r=b%a
        if r==0:
            return a
        else:
            b=r
            return(compute_gcd(a,b))
print(compute_gcd(a,b))

