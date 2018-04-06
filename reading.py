f = open ("scores.txt", "r")

users = {}

for line in f:
    entry = line.strip().split(",")
    user = entry[0]
    score = entry[1]
    users[user] = score
    print(user + ": " + score)

	
f.close()

print(users)

    