x=input("enter the email address: ").strip()


user =x[:x.index("@")]



domain =x[x.index("@")+1:]

message=" Your username is {} and the domain name is {} "

output=message.format(user,domain)

print(output)






