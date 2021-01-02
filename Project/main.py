import os
import collections
import matplotlib.pyplot as plt;
import plotly.graph_objects as go

plt.rcdefaults()
import numpy as np

'''
def size(path):
	size = os.path.getsize(path) #Size in bytes
	return size
'''


def dir(path):
    nrDir = 0  # Numar Directoare
    sizeDir = 0  # Dimensiune Directoare
    for (root, directories, files) in os.walk(path):
        for dirs in directories:
            full_fileName = os.path.join(root, dirs)
            nrDir += 1
            # skip if it is symbolic link
            if not os.path.islink(full_fileName):
                sizeDir += os.path.getsize(full_fileName)
    print("Number of Directories: " + str(nrDir))
    print("Size of Directories: " + str(sizeDir) + " bytes")
    return nrDir, sizeDir


def files(path):
    nrFiles = 0  # Numar Fisiere
    sizeFiles = 0  # Dimensiune Fisiere
    nrExtensions = collections.Counter()  # Numarul de aparitii al unei Extensii
    for (root, directories, files) in os.walk(path):
        for fileName in files:
            full_fileName = os.path.join(root, fileName)
            nrFiles += 1
            # skip if it is symbolic link
            if not os.path.islink(full_fileName):
                sizeFiles += os.path.getsize(full_fileName)
            name, ext = os.path.splitext(fileName)
            nrExtensions[ext] += 1
    # print (full_fileName)
    print("Number of Files: " + str(nrFiles))
    print("Size of Files: " + str(sizeFiles) + " bytes")
    print(nrExtensions.keys())
    print(nrExtensions.values())
    return nrFiles, sizeFiles, nrExtensions


def partition(path):
    nrDir, sizeDir = dir(path)
    nrFiles, sizeFiles, nrExtensions = files(path)

    # Data to plot
    labels = nrExtensions.keys()
    print("Keys:" + str(labels))
    sizes = nrExtensions.values()

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.pie(sizes, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)

    ax1.set_title('Partitions',
                  fontweight="bold")
    plt.axis('equal')
    fig.suptitle('Partition-statistics')

    # Sublot 2

    ax2.set_axis_off()

    """"
    table = ax2.table(
        cellText=[[nrExtensions.keys()],[nrExtensions.values()]],
        colLabels=("Extensions", "Number of Occurences"),
        cellLoc='center',
        loc = 'upper left'
    )
    """

    ax2.set_title('Number of files',
                 fontweight="bold")
    plt.show()


# give partition
#partition("C:")
#partition("C:\\test")
partition("C:\\Jocuri")
