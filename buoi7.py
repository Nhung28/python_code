# def abc ():
#   c=0
#   return c
# print(abc())
# x=abc()
# print(x) 
#mảng list lưu các phần tử cùng một ý nghĩa, dùng []
#dict lưu thông tin của cùng đối tượng, dùng {}
#hàm khi mình gọi một cái thì nó chạy ra những gì đã khai báo, thì gọi dấu ngoặc tròn: def
#
import string
import random
def generate_id():
    id=''
    for i in range(10):
        id+= random.choice(string.ascii_letters)
    return(id)
generate_id()


    

def new_account():
    Name= input("name")
    Address= input("address")
    Phone= input("phone")
    Password= input("password")
    Re_password= input("re_typepassword")
    Initial_Amount= int(input("Initial Amount"))
    User_id=generate_id()
    print(User_id)
    accounts.append({
        'Name': Name,
        'Address': Address,
        'Phone': Phone,
        'Password': Password,
        'Balance': Initial_Amount,
        'Id':User_id,
    })
    print(accounts)
    main_menu()

def log_in():
    found_account = None
    for i in range(3):
        Tendangnhap=input('Ten dang nhap')
        Matkhau=input('Mat Khau')
        for account in accounts:
            if Tendangnhap == account['Name'] and Matkhau == account['Password']:
                found_account=account
                break
        if found_account !=None:
            print(found_account)
            break
    if found_account==None: 
        print('Your account is blocked') 
    else:
        return found_account   
        
    

      
    
def changing_password(current_user):
    print(current_user)
    old_password= input ('Old Password')
    new_password= input ('New Password')
    re_new_password= input ('Rewrite New Password')
    if old_password == current_user['Password'] and new_password == re_new_password:
        for account in accounts:
            if account['Name']==current_user['Name'] :
                account['Password']=new_password
                print('Success')
                transaction(current_user)

    else: 
        print('Nhap lai')
    
def depositing(current_user):
    print('Your balance: ',current_user['Balance'])
    print('How much do you want to deposite?')
    Amount=int(input('Amount'))
    for account in accounts:
            if account['Name']==current_user['Name'] :
                account['Balance']=current_user['Balance']+Amount
                transaction(current_user)


def withdraw(current_user):
    print('Your balance: ', current_user['Balance'])
    print("How much do you want to withdraw?")
    Withdraw=int(input("Withdraw"))
    for account in accounts:
        if account['Name']==current_user['Name']:
            account['Balance']=current_user['Balance']-Withdraw
            print(accounts)
            transaction(current_user)



def transaction(current_user):
    print('1.changing password')
    print('2.depositing')
    print('3.withdrawal')
    print('4.printing the current account information')
    x=input('selection:')
    if x=='1':  
        changing_password(current_user)
    if x=='2':
        depositing(current_user)
    if x=='3':
        withdraw(current_user)
    if x=='4':
        print(current_user)

                      


    

        


accounts=[{
    'Name': 'Nhun',
    'Password': '012',
}
]
import random
def main_menu():
    print("1.New account")
    print("2.Log in")
    print("3.Exit")
    x=input('selection:')
    if x=='1':  
        new_account()
    if x=='2':
        found_user=log_in()
        if found_user != None:
            transaction(found_user)
        else:
            print("Nhap lai di")
    if x=='3':
        print('Paipai')

main_menu()




