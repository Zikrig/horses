from re import fullmatch

def check_name(name):
    print(name)
    if(len(name) > 100):
        return False
    if(fullmatch(r'[а-яА-ЯёЁa-zA-Z\s\-]+',name)):
        print(f'Имя {name} меня вполне устраивает')
        return True
    return False

check_name('АлF$')