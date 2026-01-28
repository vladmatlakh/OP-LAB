class People:
    __population = 8_000_000_000

    def __init__(self,population_ua,population_usa):
        self.population_ua = population_ua
        self.population_usa = population_usa


    def populations (self):
        return self.__population


class Person(People):
    def __init__ (self, population_ua,population_usa):
        super().__init__(population_ua,population_usa)

    def nation_populations(self, a):
        if a == 'ua':
            return self.population_ua
        else: return self.population_usa
        
        
people = People(44_000_000, 356_000_000)
person = Person(44_000_000, 356_000_000)
print("UA nation population: ",person.nation_populations('ua'))
print("USA nation population: ",person.nation_populations('usa'))
print("All people population: ",people.populations())
