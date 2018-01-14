#File Comparator to compare text differences between two text files
#Created By Bellal Arezki Mustapha (Sudo)

#!/usr/bin/python

file1 = open("copy.txt",'r').read()   
file2 = open("original.txt","r").read()
diff = ""

print "Diff length = ",len(file1) - len(file2)

compt2 = 0
for  compt1 in xrange(len(file1)) :
     if file1[compt1] != file2[compt2] :
         diff += file1[compt1]
     else :
         compt2 += 1

print diff
         





