import functions


print("Üdvözöljük!\n\nKérem válasszon az alábbi opciók közül:\nFoglalás: f, Lemondás: l, Listázás: t vagy kilépés: k")

while True:
    inp=input()
    if inp.lower()=="f":
        print("Adja meg a datumot")
        month=input("Hónap:")
        day=input("Nap")
        date=functions.input_to_date(month, day)
        print(date)
        name==input("Adja meg a nevét: ")
        hotel=input("Adja meg a hotel nevét: ")
        room=input("Adja meg a szobaszámot: ")
    elif inp.lower()=="l":
        name=input("Kérem a nevét!")
        functions.Delete_booked_date(name)
    elif inp.lower()=="t":
        hotel=input("Adja meg a hotel nevét: ")
        functions.list_out_occupied_rooms(hotel)
    elif inp.lower()=="k":
        break
    else:
        print("Ismeretlen utasítás")