# cs484-k-means-classification

Accuracy Improvement Approaches:
	For this homework it was required to implement the clustering method called K-means, which is very useful for data mining when 
  we need to categorize data points into different groups.  For part 1 we were given a dataset that was relatively small (from a 
  data mining perspective) which was ideal to test the behavior of the algorithm.  Developing the steps for the algorithm itself 
  was enough to obtain a good accuracy on it.  Due to the small number of features in the dataset for the Iris Clustering problem, 
  I did not see the need to utilize any type of dimension reduction strategies.  Therefore my focus had to switch to a different 
  was in which to calculate the distance.


Distance Calculation:
	 In the first homework for this course, I was actually compelled to implement my own Euclidean Distance calculation due to how
   critical it was to save as much time as possible since the amount of data to process was considerably big.  In this homework,
   the number of calculations was much lower, which allowed me to use the Euclidean function provided by the scipy library in Python.  
   Unfortunately the Euclidean distance does not take into account the different trends of distribution of points in the 
   multidimensional space.  After submitting the results of Part 1 for this homework I achieved a level of accuracy that, 
   while not extremely low, it did not inspire much confidence about the behavior of the K-means algorithm.  In light of that 
   I was forced to utilize the Cosine distance function, as a second approach.

	After trying the Cosine distance for the new calculation of the distance, the accuracy of the K-means spiked to a 0.95,
	which is something that reflected the well behavior of the algorithm, at least with a small dataset.


The Selection of Initial Centroids:
	It is also a fact that the selection of initial centroids can make a difference in the outcome of the K-means clustering
  algorithm.  It actually proved to be true in the Part 1 of this homework, when my initial score was 0.65 (with Euclidean 
  Distance) and it when up to 0.69 (also with Euclidean Distance) after changing the location of the initial centroids.  
  This behavior brought a sense of caution about trying different locations of such initial centroids in order to get 
  better results.  


Dimension Reduction:
	Part 1 was about solving a problem that dealt with only 4 features, which would not requiere any dimension reduction. 
  For Part 2 of this project we were given almost the same kind of problem as in the Part 1, with  the difference that 
  in this case we were analyzing images, which made for a dataset that contained 784 features, which is not as large a 
  number of dimensions as with text data mining, but it is still sizable enough to consider Dimension reduction techniques.  
  For the matter of dimension reduction I attempted to transform the dimension vectors into a smaller matrix, which could 
  change the accuracy scores.  I decided to first make use of numpy arrays so that I could use a csr_matrix from the scipy 
  package. This was necessary to transform the sparse matrix into TSVD with a smaller number of components. 

	The reason why I wanted to try this was largely due to the statistical manipulation of the data that take effect when
	truncating a TSVD sparse matrix.  It is well known that the feature reduction (transformation) that happens during the 
	truncation of a TSVD sparse matrix involves getting rid of columns in the matrix that are correlated.  It would also 
	eliminate all columns of the matrix that were mostly populated by 0’s.  The expectation was to make the data in the 
	vectors more relevant, and consequently changing the result in the calculation of the distances between data points. 
	This in turn could have compensated for the possibility of data that has outliers.  


Overview and Assignment Goals:

The objectives of this assignment are the following:
Implement the K-means Algorithm
Assess the performance of the algorithm
Think about Best Metrics for Evaluating Clustering Solutions

Detailed Description:

For the purposes of this assignment, implement the K-means algorithm. I was not allowed to use any existing
libraries except for pre-processing the data.

For Evaluation Purposes (Leaderboard Ranking), Miner will use the V-measure in the sci-kit learn library that
is considered an external index metric to evaluate clustering. Essentially your task is to assign each of the
instances in the input data to k clusters identified from 1 to K.

For the leaderboard evaluation for Part 1, set K to 3. Submit your best results. The leaderboard will report the
V-measure on 50% of sampled dataset.

Running Instructions:
	In order to get a smooth running of this program, there are a few simple requirements that need to be met:  

	For Part 1:
	The name of the source code is IrisClustering.py
	The dataset was stored in a file called:  iris_new_data.txt
	The results will be stored in a file called:  results.dat
	The files called train_drugs.dat and test.dat must reside in the same folder where the source
		code file is saved.

