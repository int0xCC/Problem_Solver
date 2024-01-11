import random

inp=input("TYPE heads or tails(Case sensitive): ")

tim=random.randint(1,2)

if tim==1:
    get="heads"
elif tim==2:
    get="tails"

if inp==get:
    print("Go Ahead! its",get)
else:
    print("Rethink your decision..its",get)
