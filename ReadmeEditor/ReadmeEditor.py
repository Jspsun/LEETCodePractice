import time
import datetime
import os.path

from Scraper import Scraper
from Writer import Writer

# ----------------------------------------------------------------------------------
# def main():

    # pushToGit()


def writeHeader():
    W.write()


def pushToGit():
    os.system("cd ~/AtomWorkspace/LEETCodePractice/")
    os.system("git add .")
    os.system("git commit -m \"added files\" ")
    os.system("git push")


if __name__ == "__main__":
    S = Scraper()
    W = Writer()

    qSolved = S.getQuestionsSolved()
    W.write('/'.join(qSolved))

    W.cleanup()
    S.cleanup()
