f_appand = open("file_append.txt", "a")
hello = "\nHello my name is"
f_appand.write(f"{hello} Al-Amin")
f_appand.close()
f_open = open("file_append.txt")
print(f_open.read())