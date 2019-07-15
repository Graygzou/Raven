# Raven [![Website](https://img.shields.io/website/https/graygzou.github.io/Raven-IA.svg)](https://graygzou.github.io/Raven-IA/)
Top down 2D game, similar to a Quake-style deathmatch. It is originaly made by Mat Bucklandin his book, ["Programming Game AI By Example"](https://www.amazon.ca/Programming-Game-Example-Mat-Buckland/dp/1556220782). This application has been completed for a school project at the Université du Québec à Chicoutimi (UQAC). The course is the following : [Artificial Intelligence for Video Games (8IAR125)](http://cours.uqac.ca/8IAR125).

<p align="center">
<img width="400px" height="400px" src="https://github.com/Graygzou/Raven-IA/blob/master/Images/raven.png"> <img width="390px" height="390px" src="https://github.com/Graygzou/Raven-IA/blob/master/Images/raven2.png">
</p>

## Objective
The main objective was to reviewed and improved the IA in the game. We also added features to the game like a new map,
new weapons and new game modes (team deathmatch, 1vs1, ...)


## Run the game
An `.exe` is available in the `FinalBuild` folder. To make it work, you need to download the entire `FinalBuild` folder which include lua variables, maps, etc. A UI will show up at start : it permits to run different modes and custom your game with custom AI behaviors for example.

<img align="right" width="250" height="250" src="https://github.com/Graygzou/Raven-IA/blob/master/Images/network.png">

## Neural Network
The final challenge we solved in this project was introducing a neural network in the game to make a bot leaned how to shoot. We fed our network with criterions that came from the game envrionment :

* Is the closest enemy visible ? `0` or `1`
* Does the closest enemy has his maximum health ? `0` or `1`
* Does the learning bot has his maximum health ? `0` or `1`
* The current weapon of the learning bot. `6` to `9`
* Does the distance (closest enemy)-(learning bot) is less than 200 ? `0` or `1`

The final outuput of the network is the decision of the bot to shoot or not in the direction of the closest enemy. `1` or `0`

We decided to expressed our inputs as binary values to make the neural learn as quickly as possible. We didn't want to record hours of gameplay in order to train it with all the possible cases.

## <a name="contributors"></a>Contributors
| Name    | Worked on        |
| ------------- |---------------|
| [Grégoire Boiron](https://github.com/Graygzou)   | Learning with Neural Network, Fuzzification principle, Custom behaviors, Controller |
| [Nguyễn Đức Hậu](https://github.com/Kihansi95)   | Add grenade weapon |
| [Thomas Faget](https://github.com/thomasfaget) | Dodge behavior |
| [Florian Rumiel](https://github.com/FloRul)   | Learning with Neural Network, Controller |
| [Vincent Pera](https://github.com/VincentPera) | Fuzzification principle  |
| [Sacha Vanleenne](https://github.com/carnageusp)   | Team and loot weapons mechanism | 
