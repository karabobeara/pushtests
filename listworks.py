
#lost_time = ["youtube", "homework", "sleep", "procrastination", "phone"]

#lost_time.append("school")
#lost_time.extend("uhhhh")

#print (lost_time)

#for action in lost_time:
#    for letter in action:
#        if letter == "n":
#            print(action)




random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71,
84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45,
85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43,
99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]

#by fives

#for number in random_numbers:
    #if number % 5 == 0:
        #print(number)




#print(random_numbers)

#for number in random_numbers:
    #for digit in number:
        #if digit == 0:
            #print(number)
        #else:
            #for digit[1] in number:
                #if digit[1] == 5:
                    #print(number)


#by 3's and 5's
#z = 0
#for number in random_numbers:
#    if number % 5 == 0:
#        x = number
#        z = z + x
#    else:
#        if number % 3 == 0:
#            y = number
#            z = z + y

#print(z)





#prime

#c = 0
#for number in random_numbers:
#    if number % 2 == 0:
#        b = 0
#    elif number % 3 == 0:
#        b = 0
#    elif number % 5 == 0:
#    elif number % 7 == 0:
#        b = 0
#    else:
#        z = number
#        c = c + z





#prime2



c = 0
for number in random_numbers:
    prime = True
#go through all numbers from 2- number - 1
    for i in range(2, (number-1)):
        if number % i == 0:
            prime = False
    if prime == True:
        print(number)
        z = number
        c = c + z


print(c)
