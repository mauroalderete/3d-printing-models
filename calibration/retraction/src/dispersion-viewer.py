import sys, getopt
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def usage():
    print("Usage")
    print("\tdispersion-viewer [options]")
    print("Show the dispersion of probes get by retraction test printed in a 3d graph.")
    print("")
    print("You can use the dispersion view to determine a optimal configure retraction.")
    print("Requires a CSV file passed by file option to read the distribution data.")
    print("Each line in the file contains the three float value that correspond a one probe.")
    print("\tFirst element, is retraction speed in mm/s")
    print("\tSecond element, is retraction Lenght in mm")
    print("\tThird element, is a relative value that express the realtion quality of one probe respect the others.")
    print("For more details, visit https://github.com/mauroalderete/3d-printing-models/tree/main/calibration/retraction")
    print("")
    print("Options")
    print("")
    print("\t-h, --help\tShow this description.")
    print("\t-v, --version\tShow version number.")
    print("\t-f, --file\tIs the file name with path with the distribution probes in CSV format")

def execute(file):
    f = open(file)
    r = csv.reader(f, delimiter=',')

    probes = {"x": [], "y": [], "z": []}

    for row in r:
        probes['x'].append(float(row[0]))
        probes['y'].append(float(row[1]))
        probes['z'].append(float(row[2]))

    x = np.array(probes['x'])
    y = np.array(probes['y'])
    z = np.array(probes['z'])

    fig = plt.figure(figsize=(4,4))

    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel("Retraction Speed [mm/s]")
    ax.set_ylabel("Lenght [mm]")
    ax.set_zlabel("Quality")

    ax.set_xlim(0,x.max())
    ax.set_ylim(0,y.max())
    ax.set_zlim(0,z.max())

    ax.scatter(x,y,z)

    plt.show()

def main(argv):
    file = ''

    try:
        opts, _ = getopt.getopt(argv, "hvf:", ["help", "file=", "version"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if len(opts)==0:
        print("file is required")
        usage()
        sys.exit(2)

    for opt, arg in opts:
            if opt in ('-h', "--help"):
                usage()
                sys.exit(0)
            elif opt in ("-v", "--version"):
                print('v0.1.0')
                sys.exit(0)
            elif opt in ("-f", "--file"):
                file = arg
    execute(file)

if __name__ == "__main__":
   main(sys.argv[1:])