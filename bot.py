""" Prototype of bot-assistant for maintaining phone book """

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    try:
        old_phone = contacts[name] 
        contacts[name] = phone
        return "Contact updated."
    except KeyError:
        return f"Person with name {name} not found. Unable to update phone."   

def show_phone(args, contacts):
    name = args[0]
    try:
        phone = contacts[name]
        return phone
    except KeyError:
        return f"Person with name {name} not found."
    
def show_all(contacts):
    if len(contacts) == 0:
        return "Phone book is empty."    
    else:
        return f"Contact list with users :\n{contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))    
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()