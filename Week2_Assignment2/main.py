miles = int(input('Enter number of miles: '))
yards = int(input('Enter number of yards: '))
feet = int(input('Enter number of feet: '))
inches = int(input('Enter number of inches: '))
divider = '--------------------'

totalInches = int((miles * 63360) + (yards * 36) + (feet * 12))
totalMeters = int(totalInches / 39.97)
totalKilometers = int(totalMeters)

print(divider)
print('Metric length:')
print('     ' + str(totalKilometers) + ' kilometers')
print('     ' + str(totalMeters) + ' meters')

