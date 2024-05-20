# spatial_SIR.py
import numpy as np
import matplotlib.pyplot as plt

def initialize_population(size):
    return np.zeros((size, size))


def infect_neighbors(population, beta):
    new_population = np.copy(population)
    infected_positions = np.where(population == 1)
    for x, y in zip(infected_positions[0], infected_positions[1]):
       
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), 
                     (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
        for nx, ny in neighbors:
            if 0 <= nx < population.shape[0] and 0 <= ny < population.shape[1]:
                if new_population[nx, ny] == 0:  
                    rand = np.random.random()
                    if rand < beta:  
                        new_population[nx, ny] = 1
    return new_population

def recover(population, gamma):
    new_population = np.copy(population)
    infected_positions = np.where(population == 1)
    for x, y in zip(infected_positions[0], infected_positions[1]):
        if np.random.random() < gamma:  
            new_population[x, y] = 2
    return new_population

population = initialize_population(100)

outbreak_position = (np.random.choice(100), np.random.choice(100))
population[outbreak_position] = 1

beta = 0.3  
gamma = 0.05  

time_steps = 100

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial Outbreak State')
plt.show()

for t in range(time_steps):
    population = infect_neighbors(population, beta)
    population = recover(population, gamma)
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time step {t+1}')
    plt.show()

