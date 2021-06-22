# Q1    Find Average
k = 80
e = 90
m = 98

r= (k+e+m)/3
print(complex(r))

### Ver.2

korean = int(input("Please input Korean score : "))
english = int(input("Please input English score : "))
math = int(input("Please input Math score : "))

average = (korean+english+math)/3
print(average)

# Q2    Even Or Odd
n = int(input("Please input any Numbers : "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3    Format Change
id_num = "881120-1068234"
print(id_num)
birth = id_num[:6]
pid = id_num[7:]
print("Your Birthday is : " + birth)
print("Your ID Number is : " + pid)

# Q4    Male or Female

pin = (input("Please input ID Numbers(123456-1234567) : "))
print(pin)
print(pin[7])
if int(pin[7]) == 2:
    print("Female")
elif int(pin[7]) == 1:
    print("male")
elif int(pin[7]) == 1:
    print("male")
elif int(pin[7]) == 3:
    print("male")

# 05 Replace
a = "a:b:c:d"
print(a.replace(":", "#"))

#06 list function
list_a = [1, 3, 5, 4, 2]
list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)

# 07 Use join fuction
s = ['Life', 'is', 'too', 'short']
t = " ".join(s)
print(t)

# 08 tuple
tpl_1 = (1,2,3)
tpl_2 = (4,)
tpl = tpl_1 + tpl_2
print(tpl)

# 09 Dictionary
dic_a = dict()
print(dic_a)

# 10 Set
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

