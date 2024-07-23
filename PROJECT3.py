       
       #CONTACT BOOK
       
contacts={}

def add_contact():
    phone=int(input("ENter the phone number:"))
    name=input("ENter the name:")
    if name in contacts:
        print("THis contact already exists.")
    else:
        contacts[name]=phone
        print("Contact added successfully.")

def delete_contact():
    name=input("ENter name:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
        
    else:
        print("THis contact doesn't exists.")
        
def update_contact():
    name=input("ENter name:")
    for contact in contacts:
        if contact==name:
            phone=input("ENter the new phone number:")
            contacts[name]=phone
            print("Contact updated successfully.")
            break
        else:
            print("THis contact doesn't exists.")
            
def search_contact():
    name=input("ENter name:")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("CONTACT FOUND.")
            print(contact,contacts[contact])
            break
        else:
            print("CONTACT NOT FOUND.")

def display_contact():
    if contacts =={}:
        print("THERE'S NO CONTACT")
    else:
        print("\t\tCONTACT LISTS:")
        for name,phone in contacts.items():
            print(name,phone)

while True:
    print("\nCONTACT BOOK MENU:")
    print("1. ADD CONTACT")
    print("2. DELETE CONTACT")
    print("3. UPDATE CONTACT")
    print("4. SEARCH CONTACT")
    print("5. DISPLAY CONTACT")
    print("6. EXIT")
    
    choice = int(input("ENter your choice between (1-6):"))
    
    if choice == 1:
        add_contact()
    
    elif choice ==2:
        delete_contact()
     
    elif choice ==3:
        update_contact()
        
    elif choice == 4:
        search_contact()
    
    elif choice == 5:
        display_contact()
    
    elif choice == 6:
        print("EXITING CONTACT BOOK.  GOODBYE !!")
        break
    
    else:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER !!")
    
print("------------------x------------------")   
    