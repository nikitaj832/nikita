import re
password=input("enter your password:")
if len(password)<8:
    print("password must contain atleast 8 character")
elif not re.search("[A-Z]",password):
    print("password must atleast one uppercase letter,password is weak",password)
elif not re.search("[a-z]",password):
    print("password must atleast one lowercase letter,password is weak",password)
elif not re.search("[0-9]",password):
    print("password must atleast one number,password is weak",password)
elif not re.search("[@]",password):
    print("password must atleast one special letter,password is weak",password)
else:
    print("password is strong")