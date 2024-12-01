# CS50 Week 0 Problem
# Einstein
# https://cs50.harvard.edu/python/2022/psets/0/einstein/

# How much energy is in the mass given
c = 300000000
mass = float(input("Enter mass in kg: "))
energy = mass * c * c
print(f"Energy is {energy} or {int(energy):,} Joules")

# How much water can this boil
joulesToBoilALiterOfWater = 334400
litersBoiled = energy/joulesToBoilALiterOfWater
print(f"This is enough energy to boil {int(litersBoiled):,} liters of water")

# How much water is that actually
litersPerOlympicPool = 2500000
numPools = litersBoiled/litersPerOlympicPool
print(f"This is the equivalent of {int(numPools):,} Olympic sized swimming pools")