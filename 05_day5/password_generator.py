import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=["'!","@","#","$","%","^","&","*","(",")","_","+"]

         

number_names=int(input("enter the number of letters you want:\n  "))
number_numbers=int(input("enter the number of NUMBERS you want:\n  "))
number_symbols=int(input("enter the number of SYMBOLS you want:\n  "))

total=number_names+number_numbers+number_symbols

# password=[]
# for char in range(0,number_names):
#    password+=random.choice(letter)

# for char in range(0,number_numbers):
#    password+=random.choice(numbers)

# for char in range(0,number_symbols):
#   password+=random.choice(symbols)

# # password = random.shuffle(password)
# # password = str(password)


# print(f"Your password is: {password}")


password=[]
for char in range(0,number_names):
    password.append(random.choice(letter))

for char in range(0,number_numbers):
    password.append(random.choice(numbers))


for char in range(0,number_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
pas = ''.join(password)
print(f"your password is:\n",{pas})
