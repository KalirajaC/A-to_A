s=input("Enter string :")
count=0
fa=0
la=0
for i in range(len(s)):
    if s[i]=='a':
        count+=1
        if count==1:
            fa=i
        elif count==2:
            la=i
    if 'a' not in s:
        print("there is no double a in the given string")
        break
        
for i in range(fa+1,la):
    print(s[i],end=' ')
        
           