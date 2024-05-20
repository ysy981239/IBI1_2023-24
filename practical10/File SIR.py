import numpy as np
import matplotlib . pyplot as plt
s=[]
s.append(9999)
i=[]
i.append(1)
r=[]
r.append(0)
b = 0.3
g = 0.05
N = 10000
T = [t for t in range(0, 1000)]
for t in range(0, len(T)-1):
    s.append(s[t]-b*i[t]*s[t]/N)
    i.append(i[t]+i[t]*b*s[t]/N-g*i[t])
    r.append(r[t]+g*i[t])
fig, ax = plt.subplots(figsize=(6,4))
ax.plot(s, c='b', lw=2, label='susceptible')
ax.plot(i, c='r', lw=2, label='infected')
ax.plot(r, c='g', lw=2, label='recovered')
ax.set_xlabel('TIME',fontsize=20)
ax.set_ylabel('number of people',fontsize=20)
ax.grid(1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.show()
plt.clf()
