# Charles Parker - CPSC2100 - Chapter 2 Programming Assignment - Stock Portfolio
# Take input from user about their amount of money invested in different stock tickers and
# add the totals up and print out the percentage of total in each stock and their total invested

# The following prompts take user input as a float to store how much they have in each ticker
SPY = float(input('Enter amount invested in SPY: $'))
QQQ = float(input('Enter amount invested in QQQ: $'))
EEM = float(input('Enter amount invested in EEM: $'))
VXX = float(input('Enter amount invested in VXX: $'))
# The following vars are to make printing the final output easier
space = '       '
divider = '--------------------'
print()

# totalInvested takes the 4 inputs and adds them together to get the total dollar amount invested
totalInvested = float(SPY + QQQ + EEM + VXX)
# The percent vars calculate the percentage of the total that each ticker takes up
percentSPY = SPY / totalInvested
percentQQQ = QQQ / totalInvested
percentEEM = EEM / totalInvested
percentVXX = VXX / totalInvested

# The round() method rounds the floats to 2 decimal places to make it look cleaner since we are dealing with money
round(percentSPY, 2)
round(percentQQQ, 2)
round(percentEEM, 2)
round(percentVXX, 2)
round(totalInvested, 2)

# These are my print statements to print out the final calculation
print('ETF' + space + 'PERCENTAGE')
print(divider)
print('SPY' + space + str(percentSPY) + '%')
print('QQQ' + space + str(percentQQQ) + '%')
print('EEM' + space + str(percentEEM) + '%')
print('VXX' + space + str(percentVXX) + '%')
print('TOTAL AMOUNT INVESTED: $' + str(totalInvested))

