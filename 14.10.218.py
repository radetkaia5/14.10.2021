s1="A B C D E F G H I J K L M N O P Q R S T X Y Z "
s2=''
for i in s1:
    if ord(i) in range(65,90):
        i=chr(ord(i)+1)
        s2+=i
    if i==' ':
        i='_'
        s2+=i 
for i in s2:
    if i=='Z':
        i='A'
        s2+=i
print(s2)