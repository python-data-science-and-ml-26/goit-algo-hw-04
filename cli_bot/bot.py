

def parse_input(user_input):
    cmd, *args = user_input.split()

    if not cmd:
        return "", []
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args

        if name in contacts:
            return "Error: Contact with this name already exists."
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please provide both name and phone number."

def change_contact(args, contacts):
    try:
        name, phone = args

        if name not in contacts:
            return "Error: Contact not found."
        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Error: Please provide both name and phone number."

def find_contact(args, contacts):
    try:
        name = args[0]

        if name not in contacts:
            return "Error: Contact not found."
        return f"{name}: {contacts[name]}"
    except IndexError:
        return "Error: Please provide a name."

def list_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

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
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

