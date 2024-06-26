# create class
# update Dictionary=>self.books_dict.update({str(Id):{"books_title":line.replace("\n","")}})
# update key =>self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            # "lender_name":"" ,"Issue_data":"","Status":"Available" }})
            # Id = Id + 1
# Books dictionary            
           

import datetime
import os
os.getcwd()

class LMS:
    """This class is used to keep record of books library.
    It has total four module: "Display Books","Issue Books","Add Books","Return Books" """
    def __init__(self, list_of_books, library_name):   # constructor
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}    # titale,lender name,issue data,status of that book
        Id = 101      # concept of file handling
        with open(self.list_of_books) as bk:     # notepad file how to read
            content = bk.readlines()
        for line in content:
            # print(line)
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            'lender_name':"" ,'Issue_data':"",'Status':"Available" }})
            Id = Id + 1
    
    # display_books        
    def display_books(self):
        print("-----------------------------List of Books------------------------")        
        print("Books ID" , "\t","Title")  
        print("------------------------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"- [",value.get("Status"),"]")
    
    # Issue_books
    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_data = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            
            elif self.books_dict[books_id]["Status"] == "Available": 
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_data
                self.books_dict[books_id]["Status"]="Already Issued"
                print("Books Issued successfully !!! \n")
        else:
            print("Book ID not found !!!") 
            return self.Issue_books()
        
    def add_books(self):
        new_books = input("Enter books title:")   
        if new_books == "":
            return self.add_books()  
        elif len(new_books) > 25 :
            print("Books title length is too lonh !!! Title length should be 20 chars")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title': new_books,'lender_name': "",
                'Issue_date':"",'Status':"Available"}})
                print(f"This books '{new_books}' has been successfully !!!")
    
    def return_books(self):
        books_id = input("Enter book ID:") 
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your bokk ID.")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully updated !!! \n")
        else:
            print("Book ID is not found")
            
try:
    myLMS =  LMS("List_of_books.txt","python's library")  
    press_key_list = {"D":"Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}     
    key_press = False
    while not (key_press == "q"):
        print(f"\n------------------------welcome To {myLMS.library_name} Library Management System----------------------------\n")
        for key,value in press_key_list.items():
            print("Press" , key,"To",value)
        key_press = input("Press_key: ").lower()
        if key_press == "i":
            print("\n Current Selection : Issue Books")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\n Current Selection : Add Books \n")     
            myLMS.add_books()
        elif key_press == "d":
            print("\n Current Selection :Display Books\n")
            myLMS.display_books()    
        elif key_press == "r":
            print("\n Current Selection : Return Books\n")
            myLMS.return_books() 
        elif key_press == "q" :
            break
        else:
            continue    
except Exception as e:
    print("something went wrong.Please check your input !!!")
                     
              
                    
                    
                   
                   
# l = LMS("List_of_books.txt","python's Library")
# print(l.display_books())            
# # print(LMS("List_of_books.txt","python's Library")) 
