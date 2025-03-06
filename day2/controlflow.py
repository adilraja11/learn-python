## Create a Function --> Control Flow
def case(role, name):
    if name is not None:
        if role == 'admin':
            return f'Selamat Datang di Dashboard Admin, {name}'
        else:
            return f'Selamat Datang, {name}!'
    else:
        return 'Nama tidak ada'
        
result = case('admin', "Doni")

print(result)