import re
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw() # hide root
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

results = []
errors = []
filename = root.filename
outFilename = filename[:-4] + '__Converted.txt'
errorFilename = filename[:-4] + '__Errors.txt'
    
with open(filename, newline = '') as f:
    for line in f:
        #replace newlines
        outStr = re.sub( r"[\\n]+" , " ", line)
        #replace multiple spaces
        outStr = re.sub( r"\s{2,}" , " ", outStr)
        #replace double quotes as long as not preceeded by digit (inch)
        outStr = re.sub( r"(?<!\d)\"+" , "", outStr)
        #check if it is a valid I/O number
        match = re.search( r"^[*\s]*([IQ])" , outStr)
        #arbitrary min length
        if(len(outStr) >= 12):
            if match:
                firstLetter = match.group(1)
                results.append(outStr)
        else:
            errors.append(outStr)
        
        
with open(outFilename, 'w') as outputfile:
    for resultRow in results:
        outputfile.write(resultRow + '\n')

if len(errors) > 0:
    with open(errorFilename, 'w') as errorfile:
        for errorRow in errors:
            errorfile.write(errorRow + '\n')
