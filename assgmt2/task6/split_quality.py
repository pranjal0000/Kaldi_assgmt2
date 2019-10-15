from shutil import copyfile
import sys

test_dir = sys.argv[1]
test_dir = test_dir

split_files = [".backup/feats.scp", "feats.scp", "text", "utt2dur", "utt2num_frames", "utt2spk", "wav.scp"]

files = split_files + ['spk2utt']

cfiles = {}

classes = ['g', 'm', 'n', 'l']

for c in classes:
	cfiles[c] = {}

# for grp in classes:
# 	for file in files:
# 		print ("Opened file " + test_dir + grp + '/' + file)
# 		f = open(test_dir + grp + '/' + file, 'w+')
# 		f.write("100")
# 		cfiles[grp][file] = f

for grp in classes:
	for file in files:
		cfiles[grp][file] = ""
		
# g, m, n, l
for file_name in split_files:

	with open(test_dir+'/'+file_name) as f:
		lines = f.readlines()

	for line in lines:
		grp = line[line.find(' ')-1]
		# cfiles[grp][file_name].write(line)
		cfiles[grp][file_name] += line

with open(test_dir+'/spk2utt') as f:
	words = f.read().split()

x = {}
x['g'] = x['m'] = x['n'] = x['l'] = 0
c = 0


for word in words:
	if word[0] == 'S':
		for grp in classes:
			# cfiles[grp]['spk2utt'].write(word)
			if x[grp] == 1:
				continue
			if c == 1:
				cfiles[grp]['spk2utt'] += '\n'
			cfiles[grp]['spk2utt'] += word + ' '
			x[grp] = 1

			# x['grp'] = 0

			# if (x == 0):
			# 	# cfiles[grp]['spk2utt'].write(' ')
			# 	cfiles[grp]['spk2utt'] += ' '
			# else:
			# 	# cfiles[grp]['spk2utt'].write('\n')
			# 	cfiles[grp]['spk2utt'] += '\n'
		c += 1
		

	else:
		flag = 0
		grp = word[-1]
		#cfiles[grp]['spk2utt'].write(word)
		x[grp] = 0
		cfiles[grp]['spk2utt'] += word + ' '

		# if (x['grp'] == 0):
		# 	# cfiles[grp]['spk2utt'].write(' ')
		# 	cfiles[grp]['spk2utt'] += ' '
		# else:
		# 	# cfiles[grp]['spk2utt'].write('\n')
		# 	cfiles[grp]['spk2utt'] += '\n'

	# for grp in classes:
	# 	x['grp'] = 1-x['grp']

leftover = ['conf/mfcc.conf', 'cmvn.scp', 'frame_shift']

for file in leftover:
	for grp in classes:
		copyfile(test_dir+'/'+file, test_dir+grp+'/'+file)

for grp in classes:
	for file in files:
		with open(test_dir + grp + '/' + file, 'w+') as f:
			# print ("Writing to grp ", grp, "FILE: ", file)
			f.write(cfiles[grp][file])

		# print("FILE " + test_dir + grp + '/' + file)
		# if (cfiles[grp][file] == ''):
		# 	print("blank string")


