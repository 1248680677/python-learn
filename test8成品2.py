import random
t = random.randint (1,101)
s = 50
if t > s:
	print(t,'>',s,'fail')
if t < s:
	print(t,'<',s,'success')
if t == s:
        print(t,'=',s,'success')
