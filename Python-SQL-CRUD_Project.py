# Crud operation using My SQL Database in python#

from dbhelpercrud import Database

def main():
    DB=Database()
    while True:
        print()
        print("*********WELCOME*************")
        print()
        print("Press 1 to Insert new user ")
        print("Press 2 to Display all user ")
        print("Press 3 to Delete user ")
        print("Press 4 to Update user ")
        print("Press 5 to Exit program ")
        print()

        try:

            choice = int(input())
            if choice == 1:
                uid = int(input("Enter user id : "))
                username = input("Enter user name : ")
                userphone = input("Enter user phone : ")
                DB.insert_user(uid,username,userphone)

            elif choice == 2:
                DB.fetch_all()

            elif choice == 3:
                userid = int(input("Enter user to which you want to delete :"))
                DB.delete_user(userid)

            elif choice == 4:
                uid = int(input("Enter Id of user : "))
                username = input("Enter new name : ")
                userphone = input("Enter new phone : ")
                DB.update_user(uid,username,userphone)

            elif choice == 5:
                break

            else:
                print("Invalid input ! Try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")
            print()


if __name__ == "__main__":
    main()
