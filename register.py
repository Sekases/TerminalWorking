from json import load, dump

def have_acc():
    flag = input('Do you have a account?("yes" or "no"): ')
    while not flag.lower() == 'yes' and not flag.lower() == 'no':
        flag = input('Get answer "yes" or "no": ')
    if flag == 'yes':
        return True
    else:
        return False

def open_kos(put = 'usres_info_db.json', mode='r') -> dict:
    with open(put, mode, encoding='utf-8') as file:
        try:
            db = load(file)
        except:
            db = {}
    return db

def create_name():
    name = input('Create a self name(6 - 20 chars): ')
    while len(name) < 5 or len(name) > 21:
        name = input('Self name must be a 6 - 20 chars!: ')
    return name

def verif_name(name, db):
    if len(db) > 0:
        while True:
            try:
                flag = db[name]
                print('Name is not uniq!')
                name = create_name()
            except:
                return name

def create_a_password():
    passw = input('Create a password(Must have 10 - 20 chars, and 2 of it must be a digit): ')
    while len(passw) < 9 or len(passw) > 20:
        passw = input('Must have 10 - 20 chars')
    count_digit_passw = 2
    while count_digit_passw < 1:
        count_digit_passw = 0
        for dig in passw:
            if dig.isdigit():
                count_digit_passw += 1
        if count_digit_passw < 1:
            passw 
    return passw
        
if __name__ == '__main__':
    have_acc = have_acc()
    db = open_kos()
    if not have_acc:
        name = create_name()
        name = verif_name(name, db)
        print(name)
    else:
        pass
