import time
import datetime
import os.path

from Scraper import Scraper
from Writer import Writer


def writeHeader():
    W.writeln('# LEETCodePractice')
    W.writeln('Some of the code I\'ve written in preparation for coding interviews. Check out my journey to getting ~~less crappy~~ better at technical interviews!')
    W.writeln('')
    W.writeln('___')
    W.writeln('')


def writeQsSolved():
    qSolved = S.getQuestionsSolved()
    W.writeln('**So far (as of ' + time.strftime("%B %d, %Y") + ') my count is at:**   ')
    W.writeln('# ' + str(qSolved[0]))
    W.writeln('*Unique problems solved*')
    W.writeln('### Thats almost ' + str(round(qSolved[0] * 100.0 / qSolved[1], 2)) + '% of all of leecode!')
    W.writeln('___')


def writeLog():
    W.writeln('## ProgressLog')
    W.writeTableRow("date", "Questions Solved")
    W.writeTableRow("-:", ":-")
    W.writeTableRow("July 30, 2017:", "**173**")
    W.writeTableRow("June 30, 2017:", "**171**")
    W.writeTableRow("May 30, 2017:", "**170**")
    W.writeTableRow("April 30, 2017:", "**168**")
    W.writeTableRow("July 30, 2017:", "**165**")
    W.writeTableRow("June 30, 2017:", "**160**")
    W.writeTableRow("May 30, 2017:", "**156**")
    W.writeTableRow("April 30, 2017:", "**138**")
    W.writeTableRow("March 30, 2017:", "**129**")
    W.writeTableRow("February 28, 2017:", "**102**")
    W.writeTableRow("January 30, 2017:", "**62**")
    W.writeTableRow("December 30, 2016:", "**40**")
    W.writeTableRow("November 30, 2016:", "**20**")
    W.writeTableRow("October 30, 2016:", "**5** ")


def pushToGit():
    os.system("cd ~/AtomWorkspace/LEETCodePractice/")
    os.system("git add .")
    os.system("git commit -m \"added files\" ")
    os.system("git push")


S = None
W = None

if __name__ == "__main__":
    S = Scraper()
    W = Writer()

    writeHeader()
    writeQsSolved()
    writeLog()

    W.cleanup()
    S.cleanup()

    pushToGit()
