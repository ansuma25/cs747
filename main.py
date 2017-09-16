import numpy as np
import sys, getopt
import readFile as rf
import lpPolicyIter as lp

def main(argv):
    filePath = ''
    algo = ''
    bSize = 0
    rndSeed = 0
    bORr = 0
    
    try:
        opts, args = getopt.getopt(argv,"hm:a:b:r:",["mdp=","algorithm=","batchsize=","randomseed="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-m","--mdp"):
            filePath = arg
        elif opt in ("-a", "--algorithm"):
            algo = arg
        elif opt in ("-b", "--batchsize"):
            bSize = arg
            bORr = 1
        elif opt in ("-r", "--randomseed"):
            rndSeed = arg
            bORr = 2

    print('mdp path = ', filePath)
    print('algo = ', algo)
    print('Batch Size = ', bSize)
    print('Random Seed = ', rndSeed)

    nS, nA, R, T, gamma = rf.readFile(filePath)
    
    print(nS)
    print(nA)
    print(R)
    print(T)
    print(gamma)

    lp.lppi(nS, nA, R, T, gamma)

if __name__ == "__main__":
    main(sys.argv[1:])
