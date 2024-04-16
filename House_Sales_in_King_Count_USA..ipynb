# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
%matplotlib inline

# Upload dataset
filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(filepath)
df.head()

# Learn what data type used in dataset and learn basic statistic info about dataset
df.dtypes
df.describe()

# Drop unnecessary columns and the print basic statistical info again
df.drop(columns = ['id','Unnamed: 0'], axis = 1, inplace = True)
df.describe()

# Check if there are missing values in 'bedroom' and 'bathroom' columns
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

# Replace missing values with average of whole column
mean = df['bedrooms'].mean()
df['bedrooms'].replace(np.nan, mean, inplace=True)

mean = df['bathrooms'].mean()
df['bathrooms'].replace(np.nan, mean, inplace=True)

# Check if all replaced
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

# Cound unique floors and convert them into data frame
df['floors'].value_counts().to_frame()

# Show price for if there is waterfont view or no in boxplot
sns.boxplot(x = 'waterfront', y = 'price', data = df)

# Show if price is increasing or decreasing according to square feet with regplot
sns.regplot(x = 'sqft_above', y = 'price', data = df)
plt.show()

# Fit 'long' and 'price' into linear regression
X = df[['long']]
Y = df['price']

lm = LinearRegression()
lm.fit(X,Y)
lm.score(X,Y)

# Check R2 score of 'sqft_living' and 'price'
Z = df[['sqft_living']]
lm.fit(Z,Y)
print(lm.score(Z,Y))

# Create a list of tuples, first element in the tuple contains the name of the estimator and the second element in the tuple contains the model constructor
features =df[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]]   
lm.fit(features, Y)
lm.score(features, Y)

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)
y_pipe = pipe.predict(features)
print(r2_score(Y, y_pipe))

# We will split the data into training and testing sets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

# Create and fit a Ridge regression object using the training data also set the regularization parameter to 0.1, and calculate the R^2
from sklearn.linear_model import Ridge

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train,y_train)
yhat = RidgeModel.predict(x_test)
print(r2_score(yhat, y_test))

# Perform a second order polynomial transform on both the training data and testing data also create and fit Ridge regression object then check the R2 score
pr = PolynomialFeatures(degree=2)

x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train_pr, y_train)
y_hat = RidgeModel.predict(x_test_pr)

print(r2_score(y_test, y_hat))
