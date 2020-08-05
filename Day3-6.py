d={}
print("歡迎進入系統")
while True:
    print("1.建立辭彙")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5.測驗")
    print("6.離開系統")
    
    x=int(input("請輸入數字"))
    if x==1:
        y=input("請輸入英文單字:")
        z=input("請輸入單字意思:")
        d[y]= z
        #break
    elif x==2:
        print(d)
        #break
    elif x==3:
        y=input("請輸入英文單字")
        if y in d:
            print(d[y])
    elif x==4:
        z=input("請輸入中文")
        for e,c in d.items():
            if c==z:
                print(e)
            
    else:
        break
        
