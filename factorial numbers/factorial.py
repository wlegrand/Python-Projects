number = input("which number: ")
number = int(number)
fact = number

for n in range(1, number+1):
    fact = fact * n
print("faxtorial ", fact)
