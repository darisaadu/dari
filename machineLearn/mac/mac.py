from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
import numpy as np 

# LinearRegression

# apple = np.array([155, 156, 157])
# n = len(apple)
# model = LinearRegression().fit(np.arange(n).reshape((n,1)), apple)
# print(model.predict([[3],[4]]))


# LogisticRegression

# X = np.array([[0, 'No'],[10, 'No'],[60, 'Yes'],[90, 'Yes']])
# n = len(X)

# model = LogisticRegression().fit(X[:,0].reshape(n,1),X[:,1])
# print(model.predict([[2],[12],[13],[40],[90]]))

# for i in range(20):
#     print('x=' + str(i) + '-->' + str(model.predict_proba([[i]])))

# using KMeans

## Data (Work (h) / Salary ($))
X = np.array([[35, 7000], [45, 6900], [70, 7100],
              [20, 2000], [25, 2200], [15, 1800]])

kmeans = KMeans(n_clusters=2).fit(X)


## Result & puzzle
cc = kmeans.cluster_centers_
# print(cc)

from sklearn.neighbors import KNeighborsRegressor
import numpy as np 


## Data (House Size (square meters) / House Price ($))
X = np.array([[35, 30000], [45, 45000], [40, 50000],
              [35, 35000], [25, 32500], [40, 40000]])

KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1), X[:,1])
res = KNN.predict([[30]])
# print(res)


from sklearn.neural_network import MLPRegressor
import numpy as np 


## Questionaire data (WEEK, YEARS, BOOKS, PROJECTS, EARN, RATING)
X = np.array(
    [[20,  11,  20,  30,  4000,  3000],
     [12,   4,   0,   0, 1000,  1500],
     [2,   0,   1,  10,   0,  1400],
     [35,   5,  10,  70,  6000,  3800],
     [30,   1,   4,  65,   0,  3900],
     [35,   1,   0,   0,   0, 100],
     [15,   1,   2,  25,   0,  3700],
     [40,   3,  -1,  60,  1000,  2000],
     [40,   1,   2,  95,   0,  1000],
     [10,   0,   0,   0,   0,  1400],
     [30,   1,   0,  50,   0,  1700],
     [1,   0,   0,  45,   0,  1762],
     [10,  32,  10,   5,   0,  2400],
     [5,  35,   4,   0, 13000,  3900],
     [8,   9,  40,  30,  1000,  2625],
     [1,   0,   1,   0,   0,  1900],
     [1,  30,  10,   0,  1000,  1900],
     [7,  16,   5,   0,   0,  3000]])


## One-liner
neural_net = MLPRegressor(max_iter=10000).fit(X[:,:-1], X[:,-1])


res = neural_net.predict([[20, 1, 10, 50, 1000]])
# print(res)