import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="pubg"
)

print(mydb)

mycursor = mydb.cursor()

sa = "insert into saurabh(username,password,age)values(%s,%s,%s)"
sa1 = "delete from saurabh where username=%s"
sa2 = "delete from saurabh where password=%s"
sa3 = "delete from saurabh where age=%s"
sa4 = "update saurabh set password=%s where username=%s"
sa5 = "update saurabh set username=%s where username=%s"
sa6 = "update saurabh set age=%s where username=%s"


val = input("user name")
ps = input("password")

if(val=="chandu" and ps=="124589"):
    while(1):
        print("1.insert")
        print("2.delete")
        print("3.update")
        print("4.display")
        ch = input("enter your choice")
        if(ch=="1"):
            un = input("enter the username")
            pw = input("enter the password")
            ag= input("enter the age")
            value=(un,pw,ag)
            mycursor.execute(sa,value)
            mydb.commit()
            print("insertion done")
        if(ch=="2"):
            print("1.delete by  username")
            print("2.delete by password")
            print("3.delete by age")
            de = input("enter your choice")
            if (de == "1"):
                js = input("username u want to delete")
                val=(js,)
                mycursor.execute(sa1,val)
                mydb.commit()
                print("deleted succesfully")
            if (de == "2"):
                js1 = input("password u want to delete")
                val = (js1,)
                mycursor.execute(sa2, val)
                mydb.commit()
                print("deleted succesfully")
            if (de == "3"):
                js2 = input("age u want to delete")
                val = (js2,)
                mycursor.execute(sa3, val)
                mydb.commit()
                print("deleted succesfully")

        if(ch=="3"):

            print("1.update username")
            print("2.update password")
            print("3.update age")
            cd = input("enter your choice")
            if(cd=="1"):
                sg6 = input("username u want to update")
                sg7 = input("new username")
                val = (sg7, sg6)
                mycursor.execute(sa5, val)
                mydb.commit()
                print("updated succesfully")
            if(cd=="2"):
                sg = input("username u want to update")
                sg2 = input("new password")
                val=(sg2,sg)
                mycursor.execute(sa4, val)
                mydb.commit()
                print("updated succesfully")
            if (cd == "3"):
                sg11 = input("username u want to update")
                sg10 = input("new age")
                val = (sg10, sg11)
                mycursor.execute(sa6, val)
                mydb.commit()
                print("updated succesfully")


        if(ch=="4"):
            mycursor.execute("SELECT * FROM saurabh")

            myresult = mycursor.fetchall()
            print("Database PUBG ")
            for x in myresult:
                print(x);

 output:--
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f0e7e1c1dd8>
user namechandu
password124589
1.insert
2.delete
3.update
4.display
enter your choice1
enter the usernamegade
enter the password123
enter the age56
insertion done
1.insert
2.delete
3.update
4.display
enter your choice2
1.delete by  username
2.delete by password
3.delete by age
enter your choice3
age u want to delete25
deleted succesfully
1.insert
2.delete
3.update
4.display
enter your choice4
Database PUBG 
('kunal', '1245', 12)
('kjhds', '4654', 45)
('chandu', '4566', 23)
('saurabh', '85', 14)
('khb', '8654', 12)
('akash', '7895', 21)
('gade', '123', 56)
1.insert
2.delete
3.update
4.display
enter your choice3
1.update username
2.update password
3.update age
enter your choice3
username u want to updatekhb
new age20
updated succesfully
1.insert
2.delete
3.update
4.display
enter your choice4
Database PUBG 
('kunal', '1245', 12)
('kjhds', '4654', 45)
('chandu', '4566', 23)
('saurabh', '85', 14)
('khb', '8654', 20)
('akash', '7895', 21)
('gade', '123', 56)
1.insert
2.delete
3.update
4.display
enter your choice
