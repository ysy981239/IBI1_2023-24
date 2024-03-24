my_dict = {}
Activity = {'Sleeping': 8, 'Classes': 6, 'Studying': 3.5, 'TV': 2, 'Music': 1, 'Other': 3.5}
Activity.items()
import matplotlib.pyplot as plt
activity_labels = ["sleeping", "classes", "studying", "TV", "music", "other"]
time_day = [8, 6, 3.5, 2, 1, 3.5]
plt.figure()
plt.pie(time_day, labels = activity_labels, startangle = 24)
fig, ax = plt.subplots()
ax.pie(time_day, labels=activity_labels, autopct='%1.1f%%')
plt.show()
plt.clf()