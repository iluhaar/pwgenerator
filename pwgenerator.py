import random

chars = '+-/*@#$%^&?=<>qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

question = input('Do u want a password? (Yes No)'+'\n')
#number = int(input('Numbers of passwords:' + '\n'))
#length = int(input('Number of symbols in pw:' + '\n'))

if question == "Yes":
    number = int(input('Numbers of passwords:' + '\n'))
    for n in range(number):
        password = ''
        length = int(input('Number of symbols in pw:' + '\n'))
        for i in range(length):
            password += random.choice(chars)
    print(password)
elif question == "No":
    exit()

#question2 = input('More passwords? (Yes No)'+'\n')
#if question2 == "Yes":
#    number = int(input('Numbers of passwords:' + '\n'))
#   for n in range(number):
#       password = ''
#       length = int(input('Number of symbols in pw:' + '\n'))
#        for i in range(length):
#           password += random.choice(chars)
#   print(password)
#elif question == "No":
#   exit()    