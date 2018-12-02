films= {
    "Finding dory":[5,15],
    "Avengers":[13,45],
    "Harry Potter":[5,25],
    "Green mile":[13,2],
    "Jumanji":[13,13]
}

while True:
    choice = input("What movie do you wanna watch?:").strip().capitalize()

    if choice in films:

        age = int(input("How old are you?:").strip())
        if age>= films[choice][0]:

            if films[choice][1]>0:
                films[choice][1]=films[choice][1]-1
                print("enjoy the movie")
            else:
                print("sorry we are sold out")
        else:
            print("Sorry your too young for the movie")
            
        
    else:
        print("we dont have that film")
        
    
    
    
