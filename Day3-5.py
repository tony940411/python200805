while True:
    print("-----------------------------------------------------------")
    print("1.加法")
    print("2.減法")
    print("3.乘法")
    print("4.除法")
    print("5.離開")
    
    x=int(input("請輸入數字"))
    if x==1:
        add1=int(input("請輸入一個數字"))
        add2=int(input("請輸入一個數字"))
        print("答案是",add1+add2)
    if x==2:
        m1=int(input("請輸入一個數字"))
        m2=int(input("請輸入一個數字"))
        print("答案是",m1-m2)
    if x==3:
        t1=int(input("請輸入一個數字"))
        t2=int(input("請輸入一個數字"))
        print("答案是",t1*t2)        
    if x==4:
        s1=int(input("請輸入一個數字"))
        s2=int(input("請輸入一個數字"))
        print("答案是",s1/s2)
    if x==5:
        break    