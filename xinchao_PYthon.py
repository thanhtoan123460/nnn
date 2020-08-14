'''x cau 2 = int(input("nhap so càn tính gia thua:"))
def fact(x):
    if(x==1):
        return 1
    return x * fact(x-1)
print(fact(x))'''

n = int(input("Nhap vao so nguyên"))
d= dict()
for i in range (1,n+1):
    d[i]=i*i
print(d)
'''temperature = int(input())

if temperature >=100:
    print("Stay at home and enjoy a good movie")
elif temperature >= 92:
    print("Stay at home")
elif temperature == 75:
    print("Go outside and enjoy the weather")
elif temperature <= 0:
    print("It's cool outside")
else:
    print("Let's go to school")'''
