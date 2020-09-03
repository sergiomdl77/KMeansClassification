from scipy import spatial
import re


pattern = re.compile('[0-9]+')
IMG_DIMS_NUM = 784
K_PARTITIONS = 10
dataPoints = []         # data points/documents as extracted from dataset


def getTestData(vectorsTsvdFitted=None):

    dataFile = open(r"new_text4.txt", "r")

    curLine = dataFile.readline()  # reads first review

    while curLine:  # starts reading all reviews (one by one)

        dataPointStr = pattern.findall(curLine)  # extract all words (disposing of spaces/symbols)

        dataPoint = []

        for i in range(len(dataPointStr)):
            dataPoint.append(int(dataPointStr[i]))

        dataPoints.append(dataPoint)          #  adding the complete row (with 0's and 1's) to the main matrix

        curLine = dataFile.readline()   # reading next line in the loop

    dataFile.close()



def printMyPoints():
    for point in dataPoints:
        print(point)


def getNewCentroids(pointAdditions, pointCounters):
    means = [[] for x in range(K_PARTITIONS)]
    meanCentroid = []
    for i in range(K_PARTITIONS):
        for j in range(IMG_DIMS_NUM):
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
        for j in range(IMG_DIMS_NUM):
            if (centroids[i][j] != tempCentroids[i][j]):
                isDifferent = True
                break
        if isDifferent:
            break

    return isDifferent


def clusterize(centroids):
    length = len(dataPoints)

    # assigning random initial centroids
    for i in range(K_PARTITIONS):
        centroid = dataPoints[(i * 117) % length]
        centroids.append(centroid)

    changeOnCentroids = True

    counter = 0
    while (changeOnCentroids):
        print("pass number: " + str(counter))
#        print("centroids: " + str(centroids))

        counter += 1

        dataInClusters = []

        # these two arrays store (per cluster) the addition of attributes of its points
        # and the cont of the points for each corresponding cluster
        pointAdditions = [[0 for y in range(IMG_DIMS_NUM)] for x in range(K_PARTITIONS)]
        pointCounters = [0 for x in range(K_PARTITIONS)]

        # Associating data points with approriate centroids (creating clusters)
        for pIndex in range(len(dataPoints)):       # traversing all data points
            smallestDist = 10000000
            clusterNum = 0      # the number of cluster with smallest distance from
                                # current dataPoint to the cluster's centroid

            # comparing distance of each data point with all of the k (K_PARTITIONS) centroids
            for cIndex in range(len(centroids)):    # to obtain the smallest one.

                d = spatial.distance.cosine(centroids[cIndex], dataPoints[pIndex])
                if (d < smallestDist):
                    smallestDist = d
                    clusterNum = cIndex+1  # because de centroids/clusters ID's are from 1,2,3, ...

            # Adding the label (cluster's ID) of the dataPoint to the array of labels
            dataInClusters.append(clusterNum)

            #Adding each attribute of the dataPoint to each attribute-total
            # print("number of additions: ", str(len(pointAdditions)))
            # print("number of dataPoints: ", str(len(dataPoints)))

            for i in range(IMG_DIMS_NUM):
                pointAdditions[clusterNum-1][i] += dataPoints[pIndex][i]

            # keeping count of number of points per cluster
            pointCounters[clusterNum-1] += 1

        # print("clusters: " + str(dataInClusters))
        # print("additions: " + str(pointAdditions))
        # print("counters: " + str(pointCounters))

        tempCentroids = getNewCentroids(pointAdditions, pointCounters)

        changeOnCentroids = checkDifference(tempCentroids,centroids)
#        changeOnCentroids = False

        if (changeOnCentroids):
            centroids = tempCentroids

    return dataInClusters


def createOutput(dataInClusters):
    clustersDataFile = open(r"results2.dat","w")

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

# Small error with Numpy arrays

