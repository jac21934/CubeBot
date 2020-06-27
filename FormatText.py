
IndentSize = 4
CharLimit = 45

BreakChars = [' ',  ',', '.', '\n', '\t', ':', ';']

IndentString = ' ' * IndentSize # This is so weird 


def BreakUpLines(inputString, LineSize):
    Lines = []
    # break long strings
    while(len(inputString) > LineSize): 

        # Gene ray does use ***...*** and --- as breaks,
        # so give those more importance
        breakIndex = inputString.rfind('*', 0, LineSize)
        if(breakIndex == -1): 
            breakIndex = inputString.rfind('---', 0, LineSize)
            # otherwise get the rightmost instance of a breakchar,
            # and break on it
            if(breakIndex == -1): 
                breakIndex = max([inputString.rfind(bc, 0, LineSize) for bc in BreakChars])

        breakIndex = breakIndex + 1 # break after the char so we don't start lines with commas
        if(breakIndex > 0 and breakIndex < len(inputString)):
            print(inputString)
            Lines.append(inputString[0:breakIndex])  
            print(inputString[0:breakIndex])
            inputString = inputString.replace(inputString[0:breakIndex], '')
        else:
            # if we can't break, then just print the whole thing
            Lines.append(inputString) 
            inputString = '' # need to delete what's next because of the append statement
            break

    # this grabs whatevers left, or get the whole string if < LineSize
    # the while loop will leave the last time sometimes if we don't do this
    Lines.append(inputString)
    return Lines


#recombine broken up strings
def FormatLines(Lines):
    outputString = ""
    for l in Lines: 
        # don't print the dumb lines that are all *
        if(l == '*' * len(l)):
            continue
        l = IndentString + l.lstrip()
        if l is not Lines[-1]:
           l = l + '\n'

        outputString = outputString + l

    return outputString


# Make the message to send
def BuildMessage(inputString): 

    Lines = BreakUpLines(inputString, CharLimit)

    outputString = FormatLines(Lines)

    # This give it that nice code block feel. Could also 
    # put some kind of CSS parsing here, since discord supports that
    return '```' + outputString + '```'