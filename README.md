Used the collaborative filtering based technique to build our model.As we didn't had any auxiliary data for hotels therefore we could not use the content based filtering.
To find the similarity between the users, we have used Euclidean distance and not Cosine/Jaccard distance method since the matrix was too sparse to contain any intersection between two users, therefore the similarity was more or less zero for almost every pair of user.
Net user bias for each user was calculated by multiplying the user bias with its similarity measures and the normalized contribution level 
Final rating are calculated using, scraped hotel average rating, user average rating and the net user bias, to fill in the remaining values.
Collaborative filtering was then followed by SVD to fill in the missing NA’s value to explain the remaining variance left in the data.
These rating were then cross-validated with surprise package.
