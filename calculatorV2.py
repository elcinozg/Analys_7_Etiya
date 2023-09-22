while True: 
    num1 = float(input("1. Sayiyi giriniz: "))
    num2 = float(input("2. Sayiyi giriniz: "))
    choose = input("Yapmak istediginiz islemi seciniz : \n 1- Toplama \n 2- Cikartma \n 3- Carpma \n 4- Bolme \n 5- Mod alma \n Cikis yapmak icin Q veya q'ya basin! \n  ")

    def Sum(num1,num2):
        return num1 + num2
    
    def Subs(num1,num2):
        return num1 - num2
    
    def Multi(num1,num2):
        return num1 * num2
    
    def Div(num1,num2):
        return num1 / num2
    
    def Mod(num1,num2):
        return num1 % num2
    
    if choose == '1':
        print(Sum(num1,num2))
    elif choose == '2':
        print(Subs(num1,num2))
    elif choose == '3':
        print(Multi(num1,num2))
    elif choose == '4':
        print(Div(num1,num2))
    elif choose == 5:
        print(Mod(num1,num2))
    elif choose == "Q" or choose == "q":
        break    
    else:
        print("Hatali giris yaptiniz.")



    

    
    

