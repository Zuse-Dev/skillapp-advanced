# import area
import sqlite3
from random import *


# setup
datebasename = r"E:\abonga\Python\project X\skillapp - advanced\skillapp.db"
db = sqlite3.connect(datebasename)
dbcr = db.cursor()
db.execute("create table if not exists users (user_id integer ,name string ,password string)")
db.execute("create table if not exists userskills (user_id integer, skill string, progress integer)")
newask2 = ""

def adduser(): # get with "1"
    username = input("Your name : ").strip().lower()
    password = input("Write your password : ").strip().lower()
    addskill = input("Your skill (write one only) : ").strip().lower()
    addprogressmsg = f"Please write you progress in '{addskill}' (number less than 100) : "
    try :
        addprogress = int(input(addprogressmsg).strip().lower())
    except :
        addprogress = "asd"
    # print(addprogress)

    while type(addprogress) != int:
        try :
            addprogress = int(input(addprogressmsg).strip().lower())
        except :
            pass
    
    if addprogress > 100 :
        while addprogress > 100 :
            try :
                addprogress = int(input(addprogressmsg).strip().lower())
            except :
                pass
    userid = (len(username) + len(password)) * randint(456,27465)
    paramsadd1 = (userid,username,password)
    paramsadd2 = (userid,addskill,addprogress)
    dbcr.execute(f"insert into users (user_id ,name ,password ) values(? , ? , ?)", paramsadd1)
    dbcr.execute(f"insert into userskills (user_id ,skill ,progress) values(?, ?, ?)", paramsadd2)
    db.commit()
    print("-_" * 49)
    print(f"Done, your name : '{username}' and your password : '{password}'\nwith skill in\n{addskill} -> {addprogress}%")
    print("-_" * 49)


def addskills(): # get with "2"
                # print(askuserid)
                addskill = input("Your skill (write one only) : ").strip().lower()
                addprogressmsg = f"Please write you progress in '{addskill}' (number less than 100) : "
                # try :
                #     addprogress = int(input(addprogressmsg))
                # except :
                #     addprogress = "asd"
                # print(addprogress)
                addprogress = ""
                while type(addprogress) != int:
                    try :
                        addprogress = int(input(addprogressmsg).strip().lower())
                    except :
                        pass

                if addprogress > 100 :
                    while addprogress > 100 :
                        try :
                            addprogress = int(input(addprogressmsg).strip().lower())
                        except :
                            pass
                # print(type(addprogress))
                # print(addprogress)
                if type(addprogress) == int and addprogress < 101:
                    paramaddskill = (i[0],addskill,addprogress)
                    db.execute("insert into userskills (user_id,skill,progress) values (?,?,?)", paramaddskill)
                    db.commit()
                    print("-_" * 49)
                    print(f"Done, you jast add '{addskill}' -> {addprogress}%")
                    print("-_" * 49)


def changeuserdate(): # get with "3"
                newask = ""
                while type(newask) != int:
                    try :
                        newask = int(input("What do you want to change? [1,2,3,4]\n1- 'name'\n2- 'password'\n3- 'delete skill'\n4- 'delete account' . ").strip())
                    except :
                        pass
                while newask > 4:
                    try :
                        newask = int(input("What do you want to change? [1,2,3,4]\n1- 'name'\n2- 'password'\n3- 'delete skill'\n4- 'delete account' . ").strip())
                    except :
                        pass
                if newask == 1:
                    print("-_" * 49)
                    newusername = input("new name : ").strip().lower()
                    print("-_" * 49)
                    print(f"Your new name is '{newusername}'")
                    print("-_" * 49)
                    paramsnewname = (newusername,askpassword)
                    dbcr.execute(f"update users set name = ? where password = ?", paramsnewname)
                    db.commit()
                elif newask == 2:
                    print("-_" * 49)
                    newpassword = input("new password : ").strip().lower()
                    print("-_" * 49)
                    print(f"Your new password is '{newpassword}'")
                    print("-_" * 49)
                    paramsnewpassword = (askname,newpassword)
                    dbcr.execute(f"update users set password = ? where name = ?", paramsnewpassword)
                    db.commit()
                elif newask == 3:
                    dbcr.execute("select skill from userskills")
                    selectskill = dbcr.fetchall() # skill
                    dbcr.execute("select user_id,skill from userskills")
                    selectskilldatewithid = dbcr.fetchall() # id , skills
                    # print(selectskilldatewithid)
                    # print(i[0])
                    print("-_" * 49)
                    print("What did you want to delete ?")
                    num = 0
                    userskilllist = []
                    for f in selectskilldatewithid :
                        if i[0] in f :
                            num += 1
                            userskilllist.append(f[1])
                            print(f"{num}- {f[1]}")
                    # print(selectskilldatewithid)
                    # print(userskilllist)
                    askskill = input("Write the skill that you want to delete . ").strip().lower()
                    # print(askskill)
                    if askskill in userskilllist :
                        user_id = i[0]
                        paramsdeleteskill = (user_id,askskill)
                        # print(paramsdeleteskill)
                        dbcr.execute("delete from userskills where user_id = ? and skill = ? ", paramsdeleteskill)
                        print("-_" * 49)
                        print(f"'{askskill}' had been deleted !")
                        print("-_" * 49)
                        db.commit()
                    else :
                        print("You write wrong skill, Try again .")
                        print("-_" * 49)
                elif newask == 4 :
                    newask2 = ""
                    while newask2 != "ok" :
                        print("-_" * 49)
                        newask2 = input("Are you sure you want to delete account [y/n] ? ").strip().lower()
                        # print(newask2)
                        if newask2 == "y" :
                            numberindex = 0
                            dbcr.execute("select user_id, skill from userskills")
                            deleteskill = dbcr.fetchall() # id ,skills
                            dbcr.execute("select user_id, progress from userskills")
                            deleteprogress = dbcr.fetchall() # id ,progress
                            print("-_" * 49)
                            print("Account had been deleted ! ")
                            print("-_" * 49)
                            deleteuser = (i[0],askname ,askpassword)
                            dbcr.execute("delete from users where user_id = ? and name = ? and password = ?", deleteuser)
                            skilllist = []
                            progresslist = []
                            for skill in deleteskill :
                                if i[0] in skill :
                                    skilllist.append(skill[1])
                            
                            for progress in deleteprogress :
                                if i[0] in progress:
                                    progresslist.append(progress[1])
                                    
                            for lol in range(1,len(skilllist) + 1):
                                deleteskill = (i[0],skilllist[numberindex],progresslist[numberindex])
                                dbcr.execute("delete from userskills where user_id = ? and skill = ? and progress = ?", deleteskill)
                                numberindex += 1
                            newask2 = "ok"
                            db.commit()
                        elif newask2 == "n" :
                            print("-_" * 49)
                            print("Account is not deleted ! ")
                            print("-_" * 49)
                            newask2 = "ok"

def showskill(): # get with "4"
        dbcr.execute("select user_id,skill from userskills")
        showskill = dbcr.fetchall() # id , progress
        dbcr.execute("select user_id,progress from userskills")
        showprogresswithid = dbcr.fetchall() # id , skills
        # print(i[0])
        num = 0
        userskilllist = []
        userprogresslist = []
        for priskill in showskill:
            if i[0] in priskill:
                userskilllist.append(priskill[1])
        for priprogress in showprogresswithid:
            if i[0] in priprogress:
                userprogresslist.append(priprogress[1])
        # print(userprogresslist)
        # print(userskilllist)
        for lol in range(1,len(userskilllist) + 1) :
            print(f"{lol}- '{userskilllist[num]}' -> {userprogresslist[num]}%")
            num += 1
        print("-_" * 49)
        # print(showskill)
        # print(userskilllist)

def exit(): # get with "5"
    print("-_" * 49)
    print("The terminal has been close .")
    print("-_" * 49)
    db.close()


while True :
    sqlite3.connect(datebasename)
    answer1 =input("Choose want you want\n1- 'log in'\n2- 'make account'\n3- 'Esc' (write numbers) . ").strip().lower()
    if answer1 == "1" :
        print("-_" * 49)
        askname = input("Username : ").strip().lower()
        askpassword = input("Password : ").strip().lower()
        print("-_" * 49)
        dbcr.execute("select name,password from users")
        allusersdate = dbcr.fetchall() # name , password
        dbcr.execute("select user_id from users")
        userid = dbcr.fetchall() # user_id
        # print(allusersdate)
        dbcr.execute("select user_id,name,password from users")
        allusersdatewithid = dbcr.fetchall() # user_id,name,password
        allask = (askname,askpassword)
        answer = "0"
        if allask in allusersdate :
            for i in userid : # i is the user_id
                allask2 = (i[0],askname,askpassword)
                if allask2 in allusersdatewithid :
                    while answer != "4":
                        
                        answer = input("Choose what you want\n1- 'add skills'\n2- 'change your date'\n3- 'show skills'\n4- 'log out' (write numbers) . ").strip().lower()
                        print("-_" * 49)
                        if answer == "1":
                            addskills()
                        elif answer == "2":
                            changeuserdate()
                            break
                        elif answer == "3":
                            showskill()
                        elif answer == "4" :
                            print(f"You had been log out from '{askname}'")
                            print("-_" * 49)
                        else :
                             print("Write number between [1,2,3,4]")
        else : 
            print("Name or password is wrong .")
            # print(f"your name is '{username}'\nand you have skills in\n'{userskill}' -> '{progress}%'")
        # print("-_" * 49)



    elif answer1 == "2" :
        adduser()
        
    elif answer1 == "3" :
        exit()
        break
    
    else :
        print("Please write numbers [1,2,3] !")
