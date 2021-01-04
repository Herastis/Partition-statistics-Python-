import os
import collections
import matplotlib.pyplot as plt;

def dir(path):
    nrDir = 0  # Numar Directoare
    for (root, directories, files) in os.walk(path):
        for dirs in directories:
            nrDir += 1
    print("Number of Directories: " + str(nrDir))
    return nrDir

def files(path):
    nrFiles = 0  # Numar Fisiere
    nrExtensions = collections.Counter()  # Numarul de aparitii al unei extensii
    sizeFiles = collections.Counter()  # Dimensiunea pe care o ocupa o extensie
    for (root, directories, files) in os.walk(path):
        for fileName in files:
            full_fileName = os.path.join(root, fileName)
            nrFiles += 1
            name, ext = os.path.splitext(fileName)
            nrExtensions[ext] += 1
            sizeFiles[ext] += os.path.getsize(full_fileName)
    print("Number of Files: " + str(nrFiles))
    print("Number of extensions: " + str(nrExtensions))
    print("Size of extensions in bytes: " + str(sizeFiles))
    return nrFiles, sizeFiles, nrExtensions

def partition(path):
    nrDir = dir(path)
    nrFiles, sizeFiles, nrExtensions = files(path)

    fig, (ax1, ax2) = plt.subplots(1, 2)  # Separate fig in 2 subplots
    #Number of directories and files
    fig.suptitle("Number of directories: " + str(nrDir) + '\n' + "Number of files: " + str(nrFiles), fontweight="bold", color='blue')

    # -------------------Subplot 1: Pie chart for number
    # Data to plot
    labels = nrExtensions.keys()  # Extensions names
    sizes = nrExtensions.values()  # Number of occurrences for each extension

    ax1.pie(sizes, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax1.set_title('Number proportion')
    plt.axis('equal')

    # -------------------Subplot 2: Pie chart for size
    # Data to plot
    labels = nrExtensions.keys()  # Extensions names
    sizes = sizeFiles.values()  # Size of each extension

    ax2.pie(sizes, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax2.set_title('Size proportion')
    plt.axis('equal')
    plt.show()

# give partition
# partition("C:")
partition("C:\\test")
#partition("C:\\Jocuri")
