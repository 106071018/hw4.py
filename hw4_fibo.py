
# coding: utf-8

# In[ ]:


fibo_list=[1]
num = int(input('Please type an integer: '))
for i in range(1, num):
    if len(fibo_list)>=2:
        num = fibo_list[-1]+fibo_list[-2]
    else:
        num = 1
    fibo_list.append(num)
print(fibo_list[num])

