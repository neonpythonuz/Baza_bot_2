from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import base
menular = base.select_all_menu()
print(menular)

index = 0
keys = []
j = 0

for region in menular:
    if j % 2 == 0 and j != 0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f"{region[1]}",)])
    else:
        keys[index].append(KeyboardButton(text=f"{region[1]}",))
    j += 1

keys.append([KeyboardButton(text='Ortga')])
menu_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)




