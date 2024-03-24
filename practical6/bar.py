import matplotlib
import matplotlib.pyplot as plt 

city = ['Edinburgh', 'Glasgow', 'Stirling', 'London']
population = [0.56,0.62,0.04,9.7]
plt.bar(city,population,color=['b', 'g', 'y', 'r'])
plt.xlabel("city")
plt.ylabel("population")
plt.bar(city, population)
plt.show()
plt.clf()

city = ['Haining','Hangzhou','Shanghai','Beijing']
population = [0.58,8.4,29.9,22.2]
plt.bar(city,population,color=['b', 'g', 'y', 'r'])
plt.xlabel("city")
plt.ylabel("population")
plt.bar(city, population)
plt.show()
plt.clf()
