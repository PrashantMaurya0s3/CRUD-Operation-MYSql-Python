# Crud operation using My SQL Database in python#


import mysql.connector as connector

class Database:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='**********',  # use your own Mysql password
                                     database='pythontest') # Build your own Database in mysql and name here
        query = 'create table if not exists user(userID int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    # Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userID,userName,phone) " \
                "values({},'{}','{}')".format(userid, username, phone)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print()
        print("******User saved to DB*******")

    # Fetch All
    def fetch_all(self):
        query = "Select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User ID : ", row[0])
            print("User Name : ", row[1])
            print("Phone : ", row[2])
            print()


    # delete user
    def delete_user(self, userID):
        query = "delete from user where userID= {}".format(userID)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print()
        print("********Deleted*********")

    # update user
    def update_user(self, userID, newName, newPhone):
        query = "update user set userName='{}',phone='{}' where userId={}".format(newName, newPhone, userID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print()
        print("*********Updated*********")

