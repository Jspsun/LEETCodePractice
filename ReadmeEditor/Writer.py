class Wrinter(object):

    def __init__(self):
        self.o = open('READMEtest.md', 'w')

        # constants that I didnt want to put into an enum
        self.bold = 'BOLD'
        self.italic = 'ITALIC'
        self.strikeThrough = 'STRIKETHROUGH'

    def writeTableRow(self, left, right):
        self.o.write('| ' + left + ' | \n')

    def write(self, text, modifier=None):

        if modifier == self.bold:
            self.o.write('**' + text + '**')
        elif modifier == self.italic:
            self.o.write('*' + text + '*')
        elif modifier == self.strikeThrough:
            self.o.write('~~' + text + '~~')
        else:
            self.o.write(text)

    def writeLine(self, text, modifier=None):
        self.write(text, modifier)
        self.write(' \n')

    def cleanup(self):
        self.o.close()