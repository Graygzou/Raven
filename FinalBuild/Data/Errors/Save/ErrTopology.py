 # coding: utf-8
import matplotlib, sys
import matplotlib.pyplot as plt

plt.figure(1)

# 1 neuron
plt.subplot(221)
listeFile = ["TestsError1.txt", "TrainingsError1.txt"]
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
plt.title('1 neuron')
plt.grid(True)


# 2 neurons
plt.subplot(222)
listeFile = ["TestsError2.txt", "TrainingsError2.txt"]
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
plt.title('2 neurons')
plt.grid(True)


# 3 neurons
plt.subplot(223)
listeFile = ["TestsError3.txt", "TrainingsError3.txt"]
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
plt.title('3 neurons')
plt.grid(True)

# 4 neurons
plt.subplot(224)
listeFile = ["TestsError4.txt", "TrainingsError4.txt"]
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
plt.title('4 neurons')
plt.grid(True)

plt.grid(color='b',linestyle='-',linewidth=0.01)

# Second plot with training error only
plt.figure(2)
listeFile = ["TrainingsError1.txt", "TrainingsError2.txt",
             "TrainingsError3.txt", "TrainingsError4.txt"]
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

