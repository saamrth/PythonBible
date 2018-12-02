from random import choice


questions = ["why is the sky blue? :" , "where are all the dinasours? :" , "why is the sun orange? :" ]


question = choice(questions)

answer = input(question).lower().strip()

while answer!= "just because":
    answer= input("why ?").strip().lower()

print ("oh.. Okay")

    


    
