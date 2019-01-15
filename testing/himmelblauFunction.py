import numpy
import himmelblauGA as GA

#f(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
#minima 1: f(3.0, 2.0) = 0.0
#minima 2: f(-2.805118, 3.131312) = 0.0
#minima 3: f(-3.779310, -3.283186) = 0.0
#minima 4: f(3.584428, -1.848126) = 0.0

population_size = 4 #manager input
population = numpy.random.uniform(low=-6, high=6, size=population_size) #manager input

generations = 5 #manager input

print("Population: ", population)

for generation in range(generations):
    print("Generation: ", generation)

    

    


print("Result: ", (pow((pow(population[0][0], 2) + population[0][1] - 11), 2) + pow((population[0][0] + pow(population[0][1], 2) - 7), 2)))

    