qs = ["What is your name?" "What is your fav. color?", "What is your quest"]

n = 0
while True:
    print("Type q tp quit")
    a = input(qs[s])
    if a == "q":
        break
    n = (n + 1) % 3
