tala = int(input())
tala2 = int(input())

if tala % 2 == 0:
    print("Slétt tala")
else:
    print("Oddatala")

if tala > tala2:
    print("fyrri talan er stæri")
elif tala < tala2:
    print("Seinni talan er stæri")
else:
    print("Þær eru jafn stórar")

if "a" in "abc":
    print("a er partur af streinginum")