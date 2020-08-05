s=[]
scr=[]
a=0
total=0
def x(total,n):
    j=total
    for k in scr:
        j=j+k
    a=j/n
    return a
p=input("請輸入人數")
p=int(p)
for i in range(p):
    n=input("請輸入名字")
    s.append(n)
    s=input("請輸入分數")
    s=int(s)
    scr.append(s)
for i in range(p):
    total=total+scr[p]
n=input("輸入人數")
n=int(n)
x(total,n)

