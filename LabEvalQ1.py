Str=str(input("Enter A String: "))
N=int(input("Enter Number Of Char To Be In LowerCase: "))
str1=Str.split()


Num=len(Str)        
str2=Str[0:N].lower()
str3=Str[N:Num].upper()
str2=str2+str3


str2.replace(",",".")
str2.replace(".",",")
print(str2)

