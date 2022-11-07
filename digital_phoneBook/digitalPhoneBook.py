class Phonebook:
    def __init__(self):
        self.loginID= "";
        self.password= "";
        
        self.contactID= 0;
        self.name= [];
        self.PhoneNumber= [];
        self.email= [];

        self.login();

    
    def login(self):
        if self.loginID !="" and self.password !="":
            print("enter id and password for login");
            id= input("Enter id : ");
            pas= input("Enter password:");
            
            if id==self.loginID and pas==self.password:
                self.menu();
            else:
                print("you enter wrong id or password");
                self.login();

        else:
            print("Register Here");
            self.loginID= input("create an uinique ID: ");
            self.password= input("create new Password : ");
            self.login();

    
    def menu(self):
        user_input= input('''
        1. Add contact
        2. Update Contact
        3. Delete contact
        4. show contact
        5. exit
        ''')

        if user_input== "1":
            self.Add_contact();

        elif user_input== "2":
            self.update_contact();

        elif user_input== "3":
            self.delete_contact();

        elif user_input== "4":
            self.show_contact();

        elif user_input== "5":
            self.exit();

        else:
            print("You may Enter wrong key, Try again")
            self.menu();


    
    def Add_contact(self):
        self.contactID= self.contactID+1;
        self.name.append(input("Add Name: "));
        self.PhoneNumber.append(input("Add Phone Number: "));
        self.email.append(input("Add email: "));

        print("1 contact Added Successfully");

        self.menu();
    
    def show_contact(self):
        for i in range(self.contactID):
            print(f"| CONTACT_ID: {i}  | NAME :{self.name[i]} | PHONE :{self.PhoneNumber[i]} | EMAIL :{self.email[i]}  |")

        self.menu()

    
    def update_contact(self):
         for i in range(self.contactID):
            print(f"| CONTACT_ID: {i}  | NAME :{self.name[i]} | PHONE :{self.PhoneNumber[i]} | EMAIL :{self.email[i]}  |");
        
         print();
         update_index= int(input("Enter CONTACT_ID: "));

         self.name[update_index]= input("Update Name: ");
         self.PhoneNumber[update_index]= input("Update Number: ");
         self.email[update_index]= input("Update E-mail: ");

         print("Contact Updated Successfully")

         self.menu();

    def delete_contact(self):
        for i in range(self.contactID):
            print(f"| CONTACT_ID: {i}  | NAME :{self.name[i]} | PHONE :{self.PhoneNumber[i]} | EMAIL :{self.email[i]}  |");
        
        print();
        delete_index= int(input("Enter CONTACT_ID: "));

        self.name.pop(delete_index);
        self.PhoneNumber.pop(delete_index);
        self.email.pop(delete_index);


        self.contactID= self.contactID-1;
        print("1 contact Deleted successfully");
        self.menu();

    def exit(self):
        print("Bye");


mohitsPhone= Phonebook()