students={
    "Male": ["Sam","Sanshu", "derrick", "jermaine" ],
    "Female" :["erica","neha","monica","henielene"]
    }


for key in students.keys():
    for name in students[key]:
        if "a" in name :
            print (name)
