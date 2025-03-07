nations = ['Indonesia', 'Bahrain', 'Malaysia']

print('=== Basic For Loop ===')
for nation in nations:
    print(nation)

fruits = ['Banana', 'Apple', 'Grape']

print('=== Loop with Break ===')
for fruit in fruits:
    if fruit == 'Apple':
        break
    print(fruit)

roles = ['Backend', 'Frontend', 'QA', 'Mobile', 'Product', 'UX']

print('=== Loop with Continue ===')
for role in roles:
    if role == 'Product':
        continue
    print(role)

print('=== Loop with Enumerate ===')
for index, role in enumerate(roles, 1):
    print(index, role)

print('=== Loop with While ===')

condition = True

while condition:
    user_input = input('Masukkan secret: ')
    if user_input == 'admin':
        condition = False
        print('Akses Di terima')