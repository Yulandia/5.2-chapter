xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total =  0
product = 1

for i in xs:
    print(i)

for i in xs:
    print("The square of", i, "is", i**2)

for i in xs:
    total +=i

print(total)

for i in xs:
    product = product * i

print(product)