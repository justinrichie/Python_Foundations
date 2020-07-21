class Dog: 
    species = "mammal"
    
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
# We can instantiate our Dog class like this
philo = Dog("Philo",5)
mikey = Dog("Mikey",6)

# We can access the instance attributes with dot notation.
print(philo.name)
print(philo.age)

print("{} is {} and {} is {}.".format(philo.name, philo.age,mikey.name,mikey.age))
