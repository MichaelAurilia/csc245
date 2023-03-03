#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys


import matplotlib as matplotlib
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style

#python
#s python compiled or interperted?
    #interperted
    #its a slow language because its not compiled
    #easy to work with data and very high level coding
    #ASSEMBLY LOW LEVEL ,BYTCODE ,
    #JAVA C# PYTHON -->VERY HIGH OUTPUT PER LINE OF CODE LANGUAGES ABSTRACT TASKS AWAY FROM DEVELOPER
    #C++ used for perfomance intensive applications very popular for HighFrequency Trading graphics games
    #Google got tired of coding in C++ for performantt apps and invented go as intermdiary between something like
    #java and c++
    #C
    #loosely typed
#.PY EXTENSIONS

# Gather our code in a main() function
def main():
    #print('Hello there');
    #print(repeat('Yay', True))
   # stringTester()
 #   x1 = np.random.randint(10, size=6)  # One-dimensional array
   # x3 = np.random.randint(10, size=(3, 4,5))

    l = np.random.random(100)
    # print(np.sum(l))
    # print(sum(l))
    # print(l)
    # print(np.min(l))
    data = pd.read_csv('height.csv')
    #print(data)
    heights = np.array(data['height(cm)'])
    #print(heights)
    #print("Mean height:       ", heights.mean())
    #print("Standard deviation:", heights.std())
    #print("Minimum height:    ", heights.min())
    #print("Maximum height:    ", heights.max())
    #print("25th percentile:   ", np.percentile(heights, 25))
    #print("Median:            ", np.median(heights))
    #print("75th percentile:   ", np.percentile(heights, 75))

    plt.hist(heights)
    plt.title('Height Distribution of US Presidents')
    plt.xlabel('height (cm)')

    #plt.style
    #plt.ylabel('number');
    #plt.show()

    #print(np.array([1, 4, 2, 5, 3]))

    # a = np.array([0, 1, 2])
    # b = np.array([5, 5, 5])
    # c = np.array([5, 5, 5, 22, 20, 30])
    # print(a + 5)
    # M = np.ones((3, 3))
    # print(M+a)
    a = np.arange(3)
    b = np.arange(3)[:, np.newaxis]
    #print(a+b)

    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 50)[:, np.newaxis]

    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
    plt.colorbar
    plt.show()

    data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['apple', 'banana', 'carrot', 'dragon fruit'])
    #print(data)

    population_dict = {'California': 38332521,
                       'Texas': 26448193,
                       'New York': 19651127,
                       'Florida': 19552860,
                       'Illinois': 12882135}
    population = pd.Series(population_dict)
    #print(population['California'])
    print(population['California':'New York'])

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    stringTester()
    # result = s + s + s # can also use "s * 3" which is faster (Why?)
    # if exclaim:
    #     result = result + '!!!'
    # return result

def stringTester():
    s = "   hi hi  "
    print(s)
    print(s[0])
    print(len(s))
    print(s+" there")
    print(s.upper())

    print(s.strip())
    print(s.find('hi'))
    print(s.replace('hi', 'bye'))
    s1 = "TRIGGER_NOTIFICATION_SERVICE-uat"

    print(s1.split('-')[0])
    time_hour = 23
    mood = "notthirsty"

    if time_hour >= 0 and time_hour <= 24:
        print('Suggesting a drink option...')
        if mood == 'sleepy' and time_hour < 10:
            print('coffee')
        elif mood == 'thirsty' or time_hour < 2:
            print('lemonade')
        else:
            print('water')
#{1000] --> will increase the size of that list
    colors = ['red', 'blue', 'green']
    print(colors[0])  ## red
    print(colors[2])  ## green
    print(len(colors))  ## 3

    squares = [1, 4, 9, 16]
    sum = 0
    # for square in squares:
    #  sum += square
    #  # x = lambda a: a + 10
     # x = lambda a, b: a * b
     # print(x(5, 6))
     # print(x(5))
    #
    # for i in range(100):
    #     print(i)

        ## Access every 3rd element in a list
    i = 0
    # while i < len(squares):
    #     print(squares[i])
    #     i = i + 3

    squares.insert(2,35)
    for square in squares:
     print(square)

    print(sum)  ## 30

    def repeat(s, exclaim,randomLambdaFunction):
        """
        Returns the string 's' repeated 3 times.
        If exclaim is true, add exclamation marks.
        """

        #stringTester()
        # result = s + s + s # can also use "s * 3" which is faster (Why?)
        # if exclaim:
        #     result = result + '!!!'
        # return result
#list similar to an array but its not neceserally an array undernath

# s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
# s.strip() -- returns a string with whitespace removed from the start and end
# s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
# s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
# s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
# s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
# s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
# s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()










