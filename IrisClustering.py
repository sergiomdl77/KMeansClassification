from scipy import spatial
from scipy.spatial import distance

Kpartitions = 3
dataPoints = []         # data points as extracted from dataset


def getTestData():

    dataFile = open(r"iris_new_data.txt", "r")

    curLine = dataFile.readline()  # reads first review
    while curLine:  # starts reading all reviews (one by one)

        dataPointStr = curLine.split()
        dataPoint = []

        for i in range(4):
            dataPoint.append(float(dataPointStr[i]))

        dataPoints.append(dataPoint)          #  adding the complete row (with 0's and 1's) to the main matrix

        curLine = dataFile.readline()   # reading next line in the loop

    dataFile.close()



def printMyPoints():
    for point in dataPoints:
        print(point)


def getNewCentroids(pointAdditions, pointCounters):
    means = [[] for x in range(Kpartitions)]
    meanCentroid = []
    for i in range(Kpartitions):
        for j in range(4):
            if pointCounters[i] != 0:
                meanCentroid.append(pointAdditions[i][j]/pointCounters[i])
            else:
                meanCentroid.append(pointAdditions[i][j])

        means[i] = meanCentroid
        meanCentroid = []

    return means


def checkDifference(tempCentroids, centroids):
    isDifferent = False
    for i in range(len(centroids)):
        for j in range(4):
            if (centroids[i][j] != tempCentroids[i][j]):
                isDifferent = True
                break
        if isDifferent:
            break

    return isDifferent

def clusterize(centroids):
    length = len(dataPoints)

    # assigning random initial centroids
    for i in range(Kpartitions):
        centroid = dataPoints[(i * 97) % length]
        centroids.append(centroid)

    changeOnCentroids = True

    counter = 0
    while (changeOnCentroids):
        print("pass number: " + str(counter))
        print("centroids: " + str(centroids))

        counter += 1

        dataInClusters = []

        # these two arrays store (per cluster) the addition of attributes of its points
        # and the cont of the points for each corresponding cluster
        pointAdditions = [[0,0,0,0] for x in range(Kpartitions)]
        pointCounters = [0 for x in range(Kpartitions)]

        # Associating data points with approriate centroids (creating clusters)
        for pIndex in range(len(dataPoints)):       # traversing all data points
            smallestDist = 10000000
            clusterNum = 0      # the number of cluster with smallest distance from
                                # current dataPoint to the cluster's centroid

            # comparing distance of each data point with all of the k (Kpartitions) centroids
            for cIndex in range(len(centroids)):    # to obtain the smallest one.

                d = spatial.distance.cosine(centroids[cIndex], dataPoints[pIndex])
                if (d < smallestDist):
                    smallestDist = d
                    clusterNum = cIndex+1  # because de centroids/clusters ID's are from 1,2,3, ...

            # Adding the label (cluster's ID) of the dataPoint to the array of labels
            dataInClusters.append(clusterNum)

            #Adding each attribute of the dataPoint to each attribute-total
            for i in range(4):
                pointAdditions[clusterNum-1][i] += dataPoints[pIndex][i]

            # keeping count of number of points per cluster
            pointCounters[clusterNum-1] += 1

        print("clusters: " + str(dataInClusters))
        print("additions: " + str(pointAdditions))
        print("counters: " + str(pointCounters))

        tempCentroids = getNewCentroids(pointAdditions, pointCounters)

        changeOnCentroids = checkDifference(tempCentroids,centroids)
#        changeOnCentroids = False

        if (changeOnCentroids):
            centroids = tempCentroids

    return dataInClusters


def createOutput(dataInClusters):
    clustersDataFile = open(r"results.dat","w")

    for clusterID in dataInClusters:
        clustersDataFile.write(str(clusterID)+ '\n')

    clustersDataFile.close()


def main():
    centroids = []
    dataInClusters = []
    getTestData()
    dataInClusters = clusterize(centroids)
    print(centroids)
    print(dataInClusters)
    createOutput(dataInClusters)


if __name__ == "__main__":
    main()