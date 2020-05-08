from server.simulated_annealing import SimulatedAnnealing
import matplotlib.pyplot as plt
from server.city import City

cityList = [
    City(1,0),
    City(2,3),
    City(3,2.5),
    City(4,48),
    City(5,48),
    City(6,69),
    City(7,70),
    City(8,64),
    City(9,3),
    City(10,2.5),
    City(11,-13),
    City(12,-20),
    City(13,-9),
    City(14,-8.5),
    City(15,-8),
    City(16,2),
    City(17,-2),
    City(18,-10),
    City(19,-20),
    City(20,-15),
    City(21,-5),
    City(22,-4.5),
    City(23,-52),
    City(24,-53),
    City(25,0),
    City(26,-30),
    City(27,-51),
    City(28,81),
    City(29,84),
    City(30,82),
    City(31,40),
    City(32,50),
    City(33,51),
    City(34,63),
    City(35,45),
    City(36,54),
    City(37,29),
    City(38,21),
    City(39,22),
    City(40,39),
    City(41,39.5),
    City(42,40),
    City(43,28),
    City(44,24),
    City(45,24)
]

sa = SimulatedAnnealing(cityList, stoppingIteration=5000)
sa.executeAlgorithm()

plt.plot(sa.progress)
plt.ylabel('Best Energy')
plt.xlabel('Iteration')
plt.show()