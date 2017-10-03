# Small python script that reads an input file
# Performs a modification and generates a new output file with new data based on the first Input file data.
# Format of Input and Output file "timestamp tx ty tz qx qy qz qw"
import sys
import numpy
import argparse


def read_trajectory(filename, matrix=True):
    """
    Read a trajectory from a text file. 
    
    Input:
    filename -- file to be read
    matrix -- convert poses to 4x4 matrices
    
    Output:
    New data file , based on Input file
    """
    file = open(filename)
    data = file.read()
    lines = data.replace(","," ").replace("\t"," ").split("\n") 
    list = [[float(v.strip()) for v in line.split(" ") if v.strip()!=""] for line in lines if len(line)>0 and line[0]!="#"]
    list_ok = []
    for i,l in enumerate(list):
    	print l
    	l[2]=l[2]*0.5  # We make a modification on the ground-truth data to get a new dataset based on the ground-truth . In this example field2 = field2*05 . Format of file = timestamp tx ty tz qx qy qz qw
    	list_ok.append(l)
    traj = list_ok
    #    if l[4:8]==[0,0,0,0]:
    #        continue
    #    isnan = False
    #    for v in l:
    #        if numpy.isnan(v): 
    #            isnan = True
    #            break
    #    if isnan:
    #        sys.stderr.write("Warning: line %d of file '%s' has NaNs, skipping line\n"%(i,filename))
    #        continue
    #    list_ok.append(l)
    #if matrix :
    #  traj = dict([(l[0],transform44(l[0:])) for l in list_ok])
    #else:
    #  traj = dict([(l[0],l[1:8]) for l in list_ok])
      
    return traj

parser = argparse.ArgumentParser(description='''
    This script computes the relative pose error from the ground truth trajectory and the estimated trajectory. 
    ''')
parser.add_argument('orig_file', help='ground-truth trajectory file (format: "timestamp tx ty tz qx qy qz qw")')
parser.add_argument('new_file', help='estimated trajectory file (format: "timestamp tx ty tz qx qy qz qw")')
args = parser.parse_args()
print ("Reading "+args.orig_file)
traj_gt = read_trajectory(args.orig_file,False) # reads trajectory from groundTruth and performs small changes

#Open a new outputFile, writing mode
fileOutput = open(args.new_file,'w')
for i,line in enumerate(traj_gt):
	#fileOutput.writelines(str(l)+'\n')  # works but it includes brackets and commas
	for j,field in enumerate(line):
		fileOutput.write(str(field)+' ')
	fileOutput.write('\n')

	
fileOutput.close()

