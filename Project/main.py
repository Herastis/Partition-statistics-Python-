import os
import collections

def size(path):
	size = os.path.getsize(path) #Size in bytes
	return size

def dir(path):
	nrDir = 0 #Numar Directoare
	sizeDir = 0 #Dimensiune Directoare
	for (root, directories, files) in os.walk(path):
		for dirs in directories:
			full_fileName = os.path.join(root, dirs)
			nrDir += 1
			sizeDir += size(full_fileName)
	print("Number of Directories: " + str(nrDir))
	print("Size of Directories: " + str(sizeDir) + " bytes")

def files(path):
	nrFiles = 0 #Numar Fisiere
	sizeFiles = 0  # Dimensiune Fisiere
	nrExtensions = collections.Counter() #Numarul de aparitii al unei Extensii
	for (root, directories, files) in os.walk(path):
		for fileName in files:
			full_fileName = os.path.join(root, fileName)
			nrFiles += 1
			sizeFiles += size(full_fileName)
			name, ext = os.path.splitext(fileName)
			nrExtensions[ext] += 1
	# print (full_fileName)
	print("Number of Files: " + str(nrFiles))
	print("Size of Files: " + str(sizeFiles) + " bytes")
	print(nrExtensions)

def partition(path):
	dir(path)
	files(path)


#give partition
partition("C:")


