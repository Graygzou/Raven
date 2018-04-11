 # coding: utf-8
import matplotlib, sys
import matplotlib.pyplot as plt

# Second plot with training error only
plt.figure(1)
listeFile = ["Regular_TestsError.txt", "Regular_TrainingsError.txt"]
for fileString in listeFile:
    file = open(fileString, "r")
    y = []
    x=[]
    cnt = 1
    for line in file:
        y.append(float(line))
        x.append(cnt)
        cnt+=1
    plt.plot(x,y, label = "Error("+ fileString +")")
    file.close()

plt.legend()
plt.xlabel('Nombre d iterations')
plt.ylabel('Erreur moyenne')
plt.title('Courbes des erreurs finales')
plt.grid(color='b',linestyle='-',linewidth=0.01)
plt.show()

