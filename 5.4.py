thomas_busby = {"height": "5ft11in", "weight": "193", "fav_color": "orange", "fav_author": "Stephen King"}
         
guess = input("What is Thomas's height, weight, fav_color, or fav_author?")

if guess in thomas_busby:
    result = thomas_busby[guess]
    print("Good going!")
else:
    print("Try again.")
