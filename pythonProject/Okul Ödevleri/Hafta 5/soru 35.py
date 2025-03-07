with open("ödev.txt","w",encoding= "utf-8") as file:
    file.write("""fatih çokan
210206039
ostim teknik
""")
with open("ödev.txt","r",encoding= "utf-8") as file:
    print(file.read())