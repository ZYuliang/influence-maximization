''' File for testing different files
'''
__author__ = 'ivanovsergey'

from IC import runIC, runIC2
from representativeNodes import representativeNodes
from degreeDiscount import degreeDiscountIC, degreeDiscountIC2, degreeDiscountStar
from singleDiscount import singleDiscount
from generalGreedy import generalGreedy
from newGreedyIC import newGreedyIC
from degreeHeuristic import degreeHeuristic
from randomHeuristic import randomHeuristic
import networkx as nx
#import matplotlib.pylab as plt
import multiprocessing # for parallelizing IC running
from itertools import repeat, izip
import os

if __name__ == '__main__':
    import time
    start = time.time()

    # read in graph
    G = nx.Graph()
    with open('graphdata/hep.txt') as f:
        n, m = f.readline().split()
        for line in f:
            u, v = map(int, line.split())
            try:
                G[u][v]['weight'] += 1
            except:
                G.add_edge(u,v, weight=1)
            # G.add_edge(u, v, weight=1)
    print 'Built graph G'
    print time.time() - start

    #calculate initial set
    seed_size = 5
    S = degreeDiscountIC(G, seed_size)
    print 'Initial set of', seed_size, 'nodes chosen'
    print time.time() - start

    # write results S to file
    with open('visualisation.txt', 'w') as f:
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 200 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(G, S)
        avg += float(len(T))/iterations
        # print i, 'iteration of IC'
    print 'Avg. Targeted', int(round(avg)), 'nodes out of', len(G)
    print time.time() - start

    console = []
