# name of student: 
# number of student:
# purpose of program: To help give change with the correct amount of coins of certain types.
# structure of program: The program calculates the change to be given and iteratively determines the number of coins of each type to be returned.

coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1] # Coin values in cents (including 1, 2, and 5-euro coins)

toPay = int(float(input('Amount to pay: ')) * 100) 
paid = int(float(input('Paid amount: ')) * 100) 
change = paid - toPay 

coinsReturned = {} 

while change > 0 and len(coinValues) > 0:
    coinValue = coinValues.pop(0) 
    nrCoins = change // coinValue 

    if nrCoins > 0: 
        print('Return maximal ', nrCoins, ' coins of ', coinValue, ' cents!') 
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? ')) 
        change -= nrCoinsReturned * coinValue 

        if coinValue in coinsReturned:
            coinsReturned[coinValue] += nrCoinsReturned 
        else:
            coinsReturned[coinValue] = nrCoinsReturned 

if change > 0: 
    print('Change not returned: ', str(change) + ' cents') # Inform the user of the remaining change
else:
    print('Done') 

print('Summary of returned coins:')
for coin, count in coinsReturned.items():
    print(f'{count} coins of {coin} cents')
