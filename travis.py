known_users=["Bob", "Sam", "Emily", "Sanshu" , "Aadi" ,"Buddy", "Kritika","Sapna"]


print(len (known_users))


while True:
    print("Hi My Name is Travis!")
    name = input("What is your Name? :").strip().capitalize()

    if name in known_users:
        print("Hi! {}".format(name))
        remove= input("Do You want to be removed from the system?(y/n):").lower()

        if remove == ("y"):
            known_users.remove(name)
            print(known_users)
        elif remove ==("n"):
            print("sorry i didnt want you to leave anyways")
            
    else:
        print("I dont think i have met you {}".format(name))
        add_user= input("Do you wnated to be added to the system?(y/n):").strip().lower()

        if add_user ==("y"):
            print(known_users)
            known_users.append(name)
            print (known_users)
        
        
        elif add_user ==("n"):
            print("see you soon")
         
        
            
    
    
