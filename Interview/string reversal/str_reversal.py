txt= "Hello How Are You"
pointer=len(txt)
revtxt=""
for i in range(len(txt)-1,-1,-1):
    if txt[i]==" ":
        for x in range(i+1,pointer):
            revtxt+=txt[x]

        revtxt+=" "
        pointer=i 

revtxt+=txt[:pointer]

print(revtxt)
