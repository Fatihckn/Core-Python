def pisagor():
    liste = list()
    for x in range(1,101):
        for y in range(1,101):

            c = (x ** 2 + y ** 2) ** 0.5

            if (c == int(c)):
                liste.append((x,y,int(c)))
    return liste
for i in pisagor():
    print(i)
