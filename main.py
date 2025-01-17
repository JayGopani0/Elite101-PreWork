print("Hello! Welcome to the solar system Chatbot!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'Hello {name}, you have witnessed {age} rotations of the Earth around the sun!')
print("How can I be of assitance?")
print("")
while True:
    print("Choose from these options: ")
    print("1. Placeholder option 1")
    print("2. Placeholder option 2")
    print("3. Placeholder option 3")
    print("4. Exit the Chatbot")
    choice = int(input("Enter a number to move through the different choices: "))
    if choice == 4:
        print("Thank you for speaking with Chatbot!")
        break

