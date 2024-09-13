while True:
    try:
        agua = float(input("cantidad de agua: "))
        harina = float(input("cantidad de harina: "))
        sal = float(input("cantidad de sal: "))
        aceite = float(input("cantidad de aceite: "))
        break
    except ValueError:
        print("Introdujo un valor que no es un numero")
bol = agua + harina + sal
budare = bol + aceite
print(f"La arepa final es {budare}")
