import time
import datetime
import os.path


def main():
    printHeader()

    # base = datetime.datetime.today()
    # date_list = [base + datetime.timedelta(days=x) for x in range(0, 100)]

    printCount()
    printLog()

    o.close()
    os.system("cd ~/personal/LEETCodePractice/")
    os.system("git add .")
    os.system("git commit -m \"added files\" ")
    os.system("git push")

def printHeader():
    o.write('# LEETCodePractice\n')
    o.write('Some of the code I\'ve written in preparation for coding interviews. Check out my journey to getting ~~less crappy~~ better at technical interviews!\n')
    o.write('\n')
    o.write('___\n')
    o.write('\n')


def getNoOfQuestions():
    pathP = './Python'
    pathJ = './Java'
    pathJS = './Javascript'

    noOfPythonQsSolved = len([f for f in os.listdir(
        pathP) if os.path.isfile(os.path.join(pathP, f))])

    noOfJavaQsSolved = len([f for f in os.listdir(
        pathJ) if os.path.isfile(os.path.join(pathJ, f))])

    noOfJavaScriptQsSolved = len([f for f in os.listdir(
        pathJ) if os.path.isfile(os.path.join(pathJS, f))])
    noOfDuplicates = 20

    return noOfJavaQsSolved + noOfPythonQsSolved + noOfJavaScriptQsSolved - noOfDuplicates


def printCount():
    totalQuestions = 623.0
    o.write('**So far (as of ' + time.strftime("%B %d, %Y") +
            ') my count is at:**   \n')
    o.write('# ' + str(getNoOfQuestions()) + '\n')
    o.write('*Unique problems solved* \n')

    o.write('### Thats almost ' + str(round(getNoOfQuestions() /
                                            totalQuestions * 100, 2)) + '% of all of leecode! \n')
    o.write('___\n')


def printLog():
    o.write('## ProgressLog  \n')
    printTableRow("date", "Questions Solved")
    printTableRow("-:", ":-")
    printTableRow("July 30, 2017:", "**165**")
    printTableRow("June 30, 2017:", "**160**")
    printTableRow("May 30, 2017:", "**156**")
    printTableRow("April 30, 2017:", "**138**")
    printTableRow("March 30, 2017:", "**129**")
    printTableRow("February 28, 2017:", "**102**")
    printTableRow("January 30, 2017:", "**62**")
    printTableRow("December 30, 2016:", "**40**")
    printTableRow("November 30, 2016:", "**20**")
    printTableRow("October 30, 2016:", "**5** ")


def printTableRow(left, right):
    o.write('| ' + left + ' | ' + right + ' |   \n')


o = open('README.md', 'w')
if __name__ == "__main__":
    main()

'''
# LEETCodePractice
Some of the code I've written in preparation for coding interviews. Check out my journey to getting ~~less crappy~~ better at technical interviews!

___

**So far (as of March 13th) my count is at:**
#115

*Unique problems solved*

___

##ProgressLog
|Date               |Questions Solved|
|------------------:|:---------------|
|February 28, 2017: |  **102**       |
|January 30, 2017:  |  **62**        |
|December 30, 2016: |  **40**        |
|November 30, 2016: |  **20**        |
|October 30, 2016:  |  **5**         |
'''
