'''
Modify the Country class to include a third instance attribute called capital as a string. Store your new class in a script and test it out by adding the following code at the bottom of the script:
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
The output of your script should be:

Japan population is 140000000 and capital is Tokyo.
'''

class Country:
    
    def __init__(self, name: str, population: int, capital=None):
        self.name = name
        self.population = population
        self.capital = capital
# Add increase_population method to country class. 
# This method should take an argument and increase population of the country on this number.
    def increace_population(self, amount):
        self.population += amount

    '''
Create add method to add two countries together. 
This method should create another country object with the name 
of the two countries combined and population of the two countries added together.

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'

    '''
    def __add__(self, other_country):
        new_name = f"{self.name} {other_country.name}"
        new_population = self.population + other_country.population
        return Country(new_name, new_population)
    

japan = Country('Japan', 140_000_000, 'Tokyo')
japan.increace_population(5_000_000)
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(f"{bosnia_herzegovina.name} {bosnia_herzegovina.population}")

