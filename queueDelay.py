# required imports
import random
import numpy as nmp
import matplotlib.pyplot as plt

# vars
arrivalList = nmp.array([0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745])
expw = [0, 0, 0, 0, 0, 0, 0, 0, 0]
timeslots = 10 ** 6
serveRate = 0.75


# simulation function
def checkExpectedSimulation(arrivalRate, mu, timeslots=10 ** 6):
    queue = 0
    queues = []
    exit = 0
    #looping through time slots
    for i in range(timeslots):
        enter = 0
        exit = 0
        entered = nmp.random.uniform(0, 1)
        exited = nmp.random.uniform(0, 1)
        if entered <= arrivalRate:
            enter = 1
        else:
            enter = 0

        if queue + enter > 0:
            if exited > mu:
                exit = 0
            else:
                exit = 1

        queue = queue + enter - exit
        queues.append(queue)

#obtain average length, all lengths at each time from loop
    expL = sum(queues) / len(queues)
    return expL


def main():
    counter = 0
    for i in arrivalList:
        expL = checkExpectedSimulation(arrivalList[counter], serveRate)
        expw[counter] = float(expL / i)
        counter += 1

#printing the plot
    W = nmp.array(expw)
    print('W; ', W)
    plt.plot(arrivalList, W)
    plt.show()


if __name__ == '__main__':
    main()
