def print_menu():
    print("1. Print Phone Numbers")
    print("2. Add a Phone Number")
    print("3. Remove a Phone Number")
    print("4. Lookup a Phone Number")
    print("5. Retrieve from File")
    print("6. Quit")
    print()

numbers = {}
menu_choice = "0"
print_menu()
while menu_choice != "6":
    menu_choice = str(input("Type in a number (1-6): "))
    if menu_choice == "1":
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()

    elif menu_choice == "2":
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
        
        f = open("PhoneBook.txt", "a")
        mystring = ""
        for x in numbers:
            mystring = x +" " + numbers[x] + "\n"
        f.write(mystring)
        f.close()
        print()

    elif menu_choice == "3":
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            with open("PhoneBook.txt", "r") as fp:
                lines = fp.readlines()

            with open("PhoneBook.txt", "w") as fp:
                for line in lines:
                    if line.strip("\n") != name + " " + numbers[name]:
                        fp.write(line)
            del numbers[name]
        else:
            print(name, "was not found")
            print()

    elif menu_choice == "4":
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The phone number is", numbers[name])
            print()
        else:
            print(name, "was not found")
            print()       
        
    elif menu_choice == "5":
        
        print("Retrieved from Phonebook File")
        f = open("PhoneBook.txt", "r")
        if(f.readable):
            arr={};
            for x in f:
                arr=x.split()
                name = arr[0]
                phone = arr[1]
                numbers[name] = phone   
        f.close()
        print()
    elif menu_choice != "6":
        print_menu()