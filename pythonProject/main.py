# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def main():
    # Use a breakpoint in the code line below to debug your script.
    #print('Hello there')
    #print(repeat('Yay', True))
    stringTester()


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
