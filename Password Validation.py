def pass_validate(password1): #Function to validate password
    invalid=0
    numbers=0
    upper=0
    for i in password1:
        if i.isdigit():
                numbers+=1
        if i.isupper():
                upper+=1
        if i==' ' or i=='\t' or i=='=' or i=='?':
                invalid+=1
    if numbers>=2 and upper>=2 and invalid==0 and len(password)>=8:
        return True
    else:
        return False

def read(): #Function to read the txt file
    with open('passwords.txt', 'r') as f:
        string_read=f.read()
    dictionary_read={}
    # print(string_read)
    if string_read!='':
        list1=string_read.split('\n')
        list2=[]
        #print(list1)
        for i in range (len(list1)):
            list2=list1[i].split(',')
            dictionary_read[list2[0]]=list2[1]
    return dictionary_read

def write(): # Function to write to file
    dictionary_string=''
    for x,y in dictionary_read.items():
        dictionary_string+=x
        dictionary_string+=','
        dictionary_string+=y
        dictionary_string+='\n'
    dictionary_string=dictionary_string.strip()
    with open('passwords.txt', 'r+') as f:
        f.write(dictionary_string)


dictionary_read=read() #Reading the file to populate dictionary



keepgoing=True #Setting starting condition for while loop
invalid_try=0


while keepgoing: #Entering main loop to ask for pripary output
    print(f'A total of {len(dictionary_read)} users(s) have signed up.')
    prompt=input(' To sign up enter ("1"), to change password enter ("2"), press "Q" or "q" to quit')
    if prompt=='q' or prompt=='Q':
        keepgoing=False
    
    if prompt=='1': #NEW USER 
        username=input("Enter username:")
        while username in dictionary_read: #promt if username already exist
            username=input("Username taken, please enter another username")
        
        password=input("Input Password:") #prompt to input password
        while pass_validate(password)!=True: #While loop to recycle input in case password  doesn't meet requirement
            password=input("Invalid password, please enter new password")
        dictionary_read[username]=password
        print("New user created")
        write()
        
    
    if prompt=='2': #CHANGE PASSWORD 
        
        username=input("Enter username:") #username input
        if username in dictionary_read:  #checking dictionary to see if username exist
            password=input("Input Password:")
            
            if dictionary_read[username]==password: 
                password=input("Enter New Password")
                while pass_validate(password)!=True: #While loop to collect password which meet the requirements
                    password=input("Invalid password, please enter new password")
                dictionary_read[username]=password
                print('Password Changed')
                write()
            else:
                invalid_try=1
                while invalid_try<3: #Prmpting for correct password up to 3 times then sending user to main wile loop 
                    password=input(f'Invalid password, try again. {3-invalid_try} try left: ')
                    if dictionary_read[username]==password:
                        password=input("Enter New Password")
                        while pass_validate(password)!=True:
                            password=input("Invalid password, please enter new password")
                        dictionary_read[username]=password
                        print('Password Changed')
                        write()
                        break
                    invalid_try+=1
        else:
            print("Username does not exist")
print('Program ended')





