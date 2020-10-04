import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import math


def f(x):
    return 0.3 * st.norm.pdf(x, 3, math.sqrt(1)) + 0.7 * st.norm.pdf(x, 8, math.sqrt(4))


def g(x):
    return st.norm.pdf(x, 6, math.sqrt(10))


def getB():
    return np.random.normal(6, math.sqrt(10), 1000)


def getMax(array, defaultValue = float('-inf')):
    maxValue = defaultValue
    for i in range(len(array)):
        arrayValue = array[i]
        currentValue = f(arrayValue) / g(arrayValue)

        if(currentValue > maxValue):
            maxValue = currentValue

    return maxValue


def getSamples(m, iter=10000):
    samples = []

    for i in range(iter):
        z = np.random.normal(6, math.sqrt(10))
        u = np.random.uniform(0, 1)

        if (f(z) / (m * g(z))) > u:
            samples.append(z)
            

    return samples

def setHistChart(chart, data, title):
    chart.hist(x=data, bins='auto', rwidth=0.85)
    chart.grid(alpha=0.75)
    chart.set_xlabel('Z')
    chart.set_ylabel('Quantidade')
    chart.set_title(title)
   
def main():

    b = getB()
    m = getMax(b)
    samples = getSamples(m)

    newM = getMax(samples, m)
    newSamples = getSamples(newM)

    fig, ax = plt.subplots(1,2)
    fig.set_size_inches(10,5)
    plt.subplots_adjust(wspace = 0.5)
       
    setHistChart(ax[0], samples, title='Amostragem por rejeição\nMáximo = {}'.format(m))
    setHistChart(ax[1], newSamples, title='Amostragem por rejeição\nMáximo = {}'.format(newM))
   
    plt.show()



if __name__ == '__main__':
    main()
