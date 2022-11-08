from getGetCarsFromWeb import getCars

x = 2000

#run get cars function for all vauxhall corsas
while x < 2021:
    getCars("vauxhall", "corsa", str(x))
    x = x + 1