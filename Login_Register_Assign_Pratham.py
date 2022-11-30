import re
import csv

Email_Regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
Pwd_Regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')


def ValidEmail(email):
    if re.fullmatch(Email_Regex, email):
        return True
    else:
        return False


def ValidPwd(pwd):
    if len(pwd) < 16 and len(pwd) > 5 and re.fullmatch(Pwd_Regex, pwd):
        return True
    else:
        return False


def register():
    print('\nPlz Register New User\n')
    email = input('Email id: ')
    if ValidEmail(email):
        password = input('Password: ')
        if ValidPwd(password):
            write_file(email, password)
            print('\nUser Registered')
        else:
            print('\nInvalid Password, Please Try Again')
    else:
        print('\nInvalid Username, Please Try Again')


def login():
    email = input('Email id: ')
    auth = False
    if ValidEmail(email):
        password = input('Password: ')
        if ValidPwd(password):
            if search_file(email, password):
                print('\nLogged In Successfully')
            else:
                print('\nUser Not Found')
                register()
        else:
            print('\nInvalid Password,Please try again')
            forgot_pwd()
    else:
        print('\nInvalid Username,Please try again')


def forgot_pwd():
    email = input('Email id or User name: ')
    if ValidEmail(email):
        if search_pwd(email):
            print('\nUser Found Log In Again!')
            login()
        else:
            print('\nUser Not Found!')
            register()
    else:
        print('\nInvalid Username, Please Try Again')


def search_file(email, pwd, mode='r',newline=''):
    with open('Access_file.csv', mode, newline=newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0] and pwd == row[1]:

             return True

        return False


def search_pwd(email, mode='r',newline=''):
    with open('Access_file.csv', mode,newline=newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0]:
                print('\nPassword for '+ email + ' is '+ row[1])

            return True
        return False


def write_file(email, pwd, mode='a', newline=''):
    with open('Access_file.csv', mode, newline=newline) as f:
        writer = csv.writer(f)
        writer.writerow([email, pwd])



def welcome():
    print("Hi There!!!")
    print("~For going further Login else if you are New then please Register~")
    W=input("Login|Registration|Forgot Pwd[Type L/R/F]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    elif W=="F":
        forgot_pwd()
    else:
        print("Error,please check")
        welcome()
welcome()

