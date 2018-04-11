 # coding: utf-8
import matplotlib, sys
import matplotlib.pyplot as plt

plt.figure(1)

# 1 neuron
plt.subplot(221)
listeFile = ["Eta0.01_TestsError.txt", "Eta0.01_TrainingsError.txt"]
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
plt.title('eta = 0.01')
plt.grid(True)


# 2 neurons
plt.subplot(222)
listeFile = ["Eta0.05_TestsError.txt", "Eta0.05_TrainingsError.txt"]
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
plt.title('eta = 0.05')
plt.grid(True)


# 3 neurons
plt.subplot(223)
listeFile = ["Eta0.09_TestsError.txt", "Eta0.09_TrainingsError.txt"]
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
plt.title('eta = 0.09')
plt.grid(True)

# 4 neurons
plt.subplot(224)
listeFile = ["Eta0.13_TestsError.txt", "Eta0.13_TrainingsError.txt"]
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
plt.title('eta = 0.13')
plt.grid(True)

plt.grid(color='b',linestyle='-',linewidth=0.01)

# Second plot with training error only
plt.figure(2)
listeFile = ["Eta0.01_TrainingsError.txt", "Eta0.05_TrainingsError.txt",
             "Eta0.09_TrainingsError.txt", "Eta0.13_TrainingsError.txt"]
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
plt.title('Courbes des erreurs du reseau')
plt.grid(color='b',linestyle='-',linewidth=0.01)
plt.show()

