## Pattern Recognition Project: Image Compression with K-means Clustering

This project implements a GUI application for image compression using the K-means clustering algorithm.

**DESCRIPTION**

Image compression refers to reducing the size of an image while minimizing the impact on its quality. This is typically done by removing unnecessary 
data or representing it with less detail. Various compression techniques are used to reduce the file size without significant loss in quality.


**WHAT IS K-MEANS CLUSTERING?** 

The k-means algorithm belongs to the hard and iterative clustering algorithms, which are based on the Euclidian distance. 
The k-means clustering algorithm aims to Partition the n observations into k clusters in which each observation belongs to the cluster with the nearest mean.
The core idea of k-means is to define a centroid for each cluster. So, these centroids should be selected in a cunning way because the different locations of centroids cause different results.
Thus, the better choice is to place them as much as possible far away from each other.

**WHY DO WE USE K-MEANS algorithms to compress images?**

Color Reduction: Images often contain millions of colors, but the human eye can only perceive a limited number of distinct colors. 
K-means clustering can group similar colors together, effectively reducing the number of unique colors in the image.

Computational Efficiency: K-means clustering is relatively fast and scalable, making it suitable for processing large images with many pixels.
It iteratively assigns pixels to the nearest cluster centroid and updates the centroids until convergence.

Simple Implementation: The algorithm itself is conceptually straightforward and easy to implement.
It doesn't require complex calculations or extensive parameter tuning, making it accessible for basic image compression tasks.

Lossy Compression: While K-means clustering is a lossy compression technique (meaning some information is lost during compression),
it often achieves satisfactory results with minimal perceptual loss, especially when the number of clusters (colors) is chosen carefully


------------------
Team name:Red Team 
------------------
--------- team member ----------

1-اسلام شريف غندر. 
2-محمود محمد الصادي.
3-هاني محمد سعد.
4-امير عرفات مقبل.
5-معاذ السيد عبد الوكيل.





