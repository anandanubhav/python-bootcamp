age=int(input("what is you age?"))

if age>2 and age <8:
    print("You are eligible for child fare")
else:
    print("Sorry, cild fare not applicable to you!")
	

city = input("where do you live?")

if city == "mumbai" or city == "pune": 
    print("You live in Maharashtra")
else:
    print("You don't live in Maharashtra")


if (not((age >2 and age<8) or age>=65)):
    print("You pay 100 rupee for movie ticket")
	
	
#is vs ==
#is cheks memory address and == checks value