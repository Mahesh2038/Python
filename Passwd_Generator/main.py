import random

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
             "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
             "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "$", "%", "^", "&", "*", "(", ")", "+", "~"]

#Get the password length from the user.
num_of_alphabets = int(input("How many letters do you want in your password?\n"))
num_of_numbers = int(input("How many numbers do you want in your password?\n"))
num_of_symbols = int(input("How many symbols do you want in your password?\n"))
password = ""
 
for letter in range(num_of_alphabets):
    password += random.choice(alphabets)

for nums in range(num_of_numbers):
    password += random.choice(numbers)

for symb in range(num_of_symbols):
    password += random.choice(symbols)

#print(password)  
passwd = ''.join(random.sample(password, len(password)))
print(passwd)