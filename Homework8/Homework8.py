# Task 38

phonebook = {}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def find_contact(query):
    results = []
    for name, phone_number in phonebook.items():
        if query.lower() in name.lower():
            results.append((name, phone_number))
    return results

def update_contact(query):
    results = find_contact(query)
    if not results:
        print("The contact was not found.")
        return
    
    print("The following contacts were found:")
    for i, result in enumerate(results):
        name, phone_number = result
        print(f"{i + 1}. Name: {name}, Phone number: {phone_number}")
    
    contact_index = int(input("Enter the contact number to change: ")) - 1
    if contact_index < 0 or contact_index >= len(results):
        print("Incorrect contact number.")
        return
    
    name, phone_number = results[contact_index]
    new_phone_number = input("Enter a new phone number: ")
    phonebook[name] = new_phone_number
    print("The contact has been successfully updated.")

def delete_contact(query):
    results = find_contact(query)
    if not results:
        print("Contact not found.")
        return
    
    print("The following contacts were found:")
    for i, result in enumerate(results):
        name, phone_number = result
        print(f"{i + 1}. Name: {name}, Phone number: {phone_number}")
    
    contact_index = int(input("Enter the contact number to delete: ")) - 1
    if contact_index < 0 or contact_index >= len(results):
        print("Incorrect contact number.")
        return
    
    name, phone_number = results[contact_index]
    del phonebook[name]
    print("Contact successfully deleted.")

add_contact("Max Cherry", "94123456789")
add_contact("Paul Lighter", "98987654321")

query = input("Enter your first or last name to search: ")
results = find_contact(query)
if results:
    print("The following contacts were found:")
    for i, result in enumerate(results):
        name, phone_number = result
        print(f"{i + 1}. Name: {name}, Phone number: {phone_number}")
else:
    print("No contacts found.")

update_query = input("Enter the first or last name to change: ")
update_contact(update_query)

delete_query = input("Enter the first or last name to delete: ")
delete_contact(delete_query)

print(phonebook)  