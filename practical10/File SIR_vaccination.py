# SIR_vaccination.py
import numpy as np
import matplotlib.pyplot as plt

N = 10000  
beta = 0.3  
gamma = 0.05  
I0 = 1  
def sir_vaccination_model(N, beta, gamma, I0, vaccination_rate):
    S, I, R = N * (1 - vaccination_rate), I0, 0
    trajectories = {'S': [], 'I': [], 'R': []}

    for _ in range(1000):
        S -= beta * S * I / N
        I += beta * S * I / N - gamma * I
        R += gamma * I
        trajectories['S'].append(S)
        trajectories['I'].append(I)
        trajectories['R'].append(R)

    return trajectories

vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  
colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

for rate, color in zip(vaccination_rates, colors):
    results = sir_vaccination_model(N, beta, gamma, I0, rate)
    plt.plot(results['I'], label=f'{100*rate}% Vaccination', color=color)

plt.xlabel('Time')
plt.ylabel('Number Infected')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.show()