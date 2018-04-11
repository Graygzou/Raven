 # coding: utf-8
import matplotlib, sys
import matplotlib.pyplot as plt

plt.figure(1)

# 1 neuron
plt.subplot(221)
listeFile = ["Alpha0.00_TestsError.txt", "Alpha0.00_TrainingsError.txt"]
for fileString in listeFile:
    file = open(fileString, "r")
    y = []
    x=[]
    cnt = 1
    for line in file:
        y.append(float(line))
        x.append(cnt)
        cnt+=1
    plt.plot(x, y, label = "Error("+ fileString +")")
plt.title('alpha = 0.00')
plt.grid(True)


# 2 neurons
plt.subplot(222)
listeFile = ["Alpha0.25_TestsError.txt", "Alpha0.25_TrainingsError.txt"]
for fileString in listeFile:
    file = open(fileString, "r")
    y = []
    x=[]
    cnt = 1
    for line in file:
        y.append(float(line))
        x.append(cnt)
        cnt+=1
    plt.plot(x, y, label = "Error("+ fileString +")")
plt.title('alpha = 0.25')
plt.grid(True)


# 3 neurons
plt.subplot(223)
listeFile = ["Alpha0.50_TestsError.txt", "Alpha0.50_TrainingsError.txt"]
for fileString in listeFile:
    file = open(fileString, "r")
    y = []
    x=[]
    cnt = 1
    for line in file:
        y.append(float(line))
        x.append(cnt)
        cnt+=1
    plt.plot(x, y, label = "Error("+ fileString +")")
plt.title('alpha = 0.5')
plt.grid(True)

# 4 neurons
plt.subplot(224)
listeFile = ["Alpha0.75_TestsError.txt", "Alpha0.75_TrainingsError.txt"]
for fileString in listeFile:
    file = open(fileString, "r")
    y = []
    x=[]
    cnt = 1
    for line in file:
        y.append(float(line))
        x.append(cnt)
        cnt+=1
    plt.plot(x, y, label = "Error("+ fileString +")")
plt.title('apha = 0.75')
plt.grid(True)

plt.grid(color='b',linestyle='-',linewidth=0.01)

# Second plot with training error only
plt.figure(2)
listeFile = ["Alpha0.00_TrainingsError.txt", "Alpha0.25_TrainingsError.txt",
             "Alpha0.50_TrainingsError.txt", "Alpha0.75_TrainingsError.txt"]
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
plt.title('Courbes des erreurs en fonction de alpha')
plt.grid(color='b',linestyle='-',linewidth=0.01)
plt.show()

