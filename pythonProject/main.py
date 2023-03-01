# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import matplotlib
import matplotlib as plt
import numpy as np
import pandas as pd







def main():
    #Use a breakpoint in the code line below to debug your script.
    #print('Hello there')
    #print(repeat('Yay', True))
    #stringTester()
    #print(np.array([1, 4, 2, 5, 3]))
    #x1 = np.random.randint(10, size=6)
    #x3 = np.random.randint(10, size=(3, 4))
    #print(x1)
    #print(x3)

    #colors = ['red', 'blue', 'green']
    #print(colors)
    #print(len(colors))

    #squares = [1, 4, 9, 16]
    #sum = 0
    #for num in squares:
        #sum += num
        #x = lambda a: a + 19
        #x = lambda a, b: a * b
        #print(x(5, 6))
        #i = 0
        #for i in range(100):
            #print(i)

    data = pd.read_csv('height.csv')
    print(data)
    np.array(data['height(cm)'])
    heights = np.array(data['height(cm)'])
    print(heights)

    print("Mean height:       ", heights.mean())
    print("Standard deviation:", heights.std())
    print("Minimum height:    ", heights.min())
    print("Maximum height:    ", heights.max())

    print("25th percentile:   ", np.percentile(heights, 25))
    print("Median:            ", np.median(heights))
    print("75th percentile:   ", np.percentile(heights, 75))




def repeat(s, exclaim):
    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def stringTester():
    s = "hi"
    print(s)
    print(s[0])
    print(len(s))
    print(s + "there")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
