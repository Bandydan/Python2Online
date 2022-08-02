dfojsdfljvnds;lkvn
sd;lknsd;lkv;ldfmv
sd;lkbndslk;bn;lds
#Банкомат выдает сумму максимально возможными купюрами

# banknotes = [1000, 500, 200, 100, 50, 20, 10]
banknotes = map(int, input("Please provide banknotes list divided by spaces: ").split())
amount = int(input("Please provide the amount of grn you want to get: "))

if amount % 10:
	print("Error: wrong amount entered!")
	exit()

for nominal in banknotes:
	print(nominal)
	if amount // nominal:
		print(' -> ' + str(amount // nominal))
		amount %= nominal
	if not amount:
		exit()
