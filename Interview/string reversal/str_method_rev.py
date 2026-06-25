str1="Hello how are u"
x=str1.split()
revstr=[]
for i in range(len(x)-1,-1,-1):
    revstr.append(x[i])

y=" ".join(revstr)
print(y)