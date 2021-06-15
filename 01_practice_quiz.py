# Q1    Find Average
k = 80
e = 90
m = 98

average = (k+e+m)/3
print(complex(average))

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
if int(pin[7]) == 2 or 4:
    print("Female")
elif int(pin[7]) == 1 or 3:
    print("male")
