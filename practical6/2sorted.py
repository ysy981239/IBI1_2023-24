A=['Edinburgh','Glasgow','Stirling','London']
B=[0.56,0.62,0.04,9.7]
z = zip(B, A)
z = sorted(z, reverse=True)
B, A = zip(*z)
for i,j in zip(B, A):
    print(j, '\t',i)

C=['Haining','Hangzhou','Shanghai','Beijing']
D=[0.58,8.4,29.9,22.2]
z = zip(D, C)
z = sorted(z, reverse=True)
D, C = zip(*z)
for i,j in zip(D, C):
    print(j, '\t',i)