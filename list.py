#"groceries = ["ice cream", "pizza", "love", "happiness", "chocolate"]


from random import *

haiku1 = ["I like little dogs\n","I fell down the stairs\n",
"The hills are alive\n","Coding is so fun\n","Kids are sometimes loud\n",
"I have eaten frog\n","Memes can run my life\n","I forget the date\n"]

haiku2 = ["Sometimes they act like angels\n","Landed on and cut my knee\n",
"The sound of music is so pure\n","So far I have learned python...\n",
"Tastes like really good chicken\n",
"So many dank ones exist\n","Big dogs are wonderful too\n",
"Sometimes write my 'n''s like 'u''s,\n"]

haiku3 = ["Just luck of the draw\n","Give me a bandaid\n","H-T-M-L sucks\n",
"Do I sound snobish?\n","Still a little weird\n",
"Love the internet\n","Animals are great\n","Maybe I'll learn soon\n"]


#haiku = [haiku1, haiku2, haiku3])


def generate():
    replay = input("Haiku? (yes or no)")
    if replay == "yes":
        x = randint(0, len(haiku1)-1)
        y = randint(0, len(haiku2)-1)
        c = randint(0, len(haiku3)-1)
        print (haiku1[x], haiku2[y], haiku3[c])
        generate()

    else:
        exitonclick()

x = 0
while x == 0:
    generate()
