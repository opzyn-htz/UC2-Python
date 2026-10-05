userConnect = input("User Connected? \n >>>").lower()

userConnect.strip()
while True:
    match userConnect:
        case "yes":
            print("Mango")
            break
        
        case "no":
            print("Mango 2")
            break

        case "" | None:
            print("Kaboom")
            break