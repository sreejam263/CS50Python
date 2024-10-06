def slow_down(): #defining the functtion
    user_input = input("Please enter your text: ") #Prompting user for input
    print(user_input.strip().replace(' ','...')) #Removing whitespaces from either end using .strip() and replacing ' ' with '...' using .replace()

slow_down() #calling the function

