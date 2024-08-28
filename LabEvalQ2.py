Line=str(input("Enter A String: "))
Line.lower()
Count=0
Str={}
for i in Line:
    if i in ['a','e','i','o','u']:
        Count+=1
        if i in Str:
            Str[i]=Str[i]+1
        else:
            Str[i]=1

print("Vowels:",Count)

for j in Str:
    print(j)
    



