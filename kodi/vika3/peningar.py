peningur = int(input())

tiuk = peningur//10000
peningur = peningur % 10000

fimmk = peningur//5000
peningur = peningur % 5000

thusund = peningur//1000
peningur = peningur % 1000

print("10k seðlar", tiuk)
print("5k seðlar", fimmk)
print("1k seðlar", thusund)
print("Afgangs", peningur)