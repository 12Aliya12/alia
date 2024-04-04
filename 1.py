slovo = [a.lower() for a in input().split("-")]
chet = (len(slovo))
for i in slovo:
    i.split()
    for s in i:
        if s in "wasd":
            chet -= 1
            break
print(chet)

