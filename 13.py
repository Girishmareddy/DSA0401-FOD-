f = open("C:\\Users\\giris_pu2cvr5\\OneDrive\\Desktop\\sample.txt", "r")
data=f.read()
sp=data.split()
w={}
for i in sp:
    if i in w:
        w[i]+=1
    else:
        w[i]=1
print(w)
for i , j in w.items():
    print(f"{i}:{j}")
