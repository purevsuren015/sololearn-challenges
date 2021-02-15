siblings, popsicles = map(int, input().split())
print("give away" if popsicles % siblings == 0 else "eat them yourself")
