loop=0
counter=0
set_user="reyhaneh"
set_password="12345"


while loop<3:
    loop+=1
    user=input("enter your user")
    password=input("enter your password")

    if (user==set_user) and (password==set_password):
        print('wellcome')
        'break'
    else:
        counter += 1
        if (counter < 3):
            print('try again!')
            'continue'
        elif(counter == 3):
            print('your account has been locked')


	
