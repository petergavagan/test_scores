f = open("scores.txt", "w")

while True:
    user = input("User name >   ")

    if user == "quit":
        print ("Quiting...")
        break

    score = input("Score for " + user + "> ")
    f.write(user + "," + score + "\n")

f.close()
