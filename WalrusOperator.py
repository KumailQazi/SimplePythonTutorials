# New Features in Python 3.8
# Warlrus Operator helps you assign a value to the operator and at the same time return the value. Lets see how!!

user = {'form' : {'username' : 'Jack', 'password' : 'conf'}}
db = []

def create_user(user):
    # password = user['form'].get('password')
    # if len(password) > 6:
    if len(password := user['form'].get('password')) > 6:
        db.append(password)
        return 'Added user!'
    else:
        return 'Password is too short!'

print(create_user(user))
print(db)
