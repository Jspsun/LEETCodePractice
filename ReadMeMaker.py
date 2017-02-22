import time
import datetime
o = open('Out.md', 'w')

noOfQsSolved = 9

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(0, 100)]
print date_list
o.write('# LEETCodePractice\n')
o.write('Some of the code I\'ve written in preparation for coding interviews. Check out my journey to getting ~~less crappy~~ better at technical interviews!\n')
o.write('\n')
o.write('___\n')
o.write('\n')
o.write('**So far (as of ' + time.strftime("%B %d, %Y") + ') my count is at:**\n')
o.write('#' + str(noOfQsSolved) + '\n')

'''

*Unique problems solved*

___

##ProgressLog
|Date               |Questions Solved|
|------------------:|:---------------|
|January 30, 2017:  |  **62**        |
|December 30, 2016: |  **40**        |
|November 30, 2016: |  **20**        |
|October 30, 2016:  |  **5**         |
'''


o.close()
