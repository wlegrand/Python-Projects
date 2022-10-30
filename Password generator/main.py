import random


characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@ç§&¢%/()=?`^<>\;:-_'

number = input('Amount of passwords: ')
number = int(number)

length = input("Input your password lenght: ")
length = int(length)


print("here are your password: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)
