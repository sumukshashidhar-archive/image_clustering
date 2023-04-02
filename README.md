# image_clustering
Clustering Large Sets of Images with K-Means Clustering. Performance Optimized.

# Motivation

The purpose of this project is to conduct image clustering on a substantial dataset. The objective of this clustering is currently undisclosed and will be revealed in due course, as it is part of a larger project. Currently, the image dataset at hand comprises over 80 gigabytes of content extracted from video, segregated by scene.

# Steps

## Preliminary

### Removing No Data Images

- Our primary aim is to eliminate images that contain little to no meaningful content. Such images may comprise of pixels that are virtually identical across the entire dataset. For instance, images containing only a single color would be classified as such. We intend to filter out these images as a preliminary step in our image clustering procedure.
- This should assist the k-means algorithm in finding the real clusters / similar images

### De-duplicating images

- To further streamline the training process, we also intend to de-duplicate our image dataset, effectively removing any identical copies of images. This action will considerably reduce the overall size of our training set, while retaining all the essential features and variations.
