import os
import sys

filew = sys.argv[1]

with open(filew) as f:
	lines = f.readlines()
count=1
for line in lines:
	words = line.split(' ')
	# print(words)
	cdir = words[0][:15]
	# print(cdir)
	if (count < 10):
		os.system("sox corpus/data/wav/"+cdir+'/'+words[0]+".wav task7/output/word0"+str(count)+".wav trim " + str(words[2]) +' '+ str(words[3]) )
		# print("sox corpus/data/wav/"+cdir+'/'+words[0]+".wav wav/word0"+str(count)+".wav trim " + str(words[2]) +' '+ str(words[3]) )
	else:
		os.system("sox corpus/data/wav/"+cdir+'/'+words[0]+".wav task7/output/word"+str(count)+".wav trim " + str(words[2]) +' '+ str(words[3]) )
		# print("sox corpus/data/wav/"+cdir+'/'+words[0]+".wav wav/word0"+str(count)+".wav trim " + str(words[2]) +' '+ str(words[3]) )
	count += 1