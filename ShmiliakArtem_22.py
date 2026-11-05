a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

num = int(input())
if (1000 <= abs(num) <= 9999) and (num % 7 == 0 or num % 17 == 0):
    print("Число красиве")
else:
    print("Число не красиве")
