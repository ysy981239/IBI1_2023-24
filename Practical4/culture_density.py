holiday = 0
density = 5
# cell line doubles
while density <= 90:
    density *= 2
    # if culture density is over 90%, the holiday can't going on.
    if density > 90: 
        break
    holiday += 1
print ("I can stay away from the lab for" , holiday , "days.")