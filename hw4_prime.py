
# coding: utf-8

# In[ ]:


num=int(input("Enter a number: "))  

if num>9:
    num_sqrt = int(num**0.5)
else:
    num_sqrt = num
for i in range(2, num_sqrt):
    if num % i ==0:
        print('not prime')
        break
    elif num==2:
        print('prime')
        break
    elif num==3:
        print('prime')
        break
    else:
        print('prime')
        break

