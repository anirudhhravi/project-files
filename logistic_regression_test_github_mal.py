# Required Python Packages
import pandas as pd
import numpy as np
import pdb
import plotly.plotly as py
import plotly.graph_objs as go
import xlrd

#py.sign_in('anirudhhravi1998', 'Ani12345')

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logistic_regression_model = LogisticRegression()
# Files
DATA_SET_PATH = "F:\\Research\\IEEE SS12\\Malaria_data.csv"


def dataset_headers(dataset):
    """
    To get the dataset header names
    :param dataset: loaded dataset into pandas DataFrame
    :return: list of header names
    """
    return list(dataset.columns.values)

print("In dataset_headers")

def unique_observations(dataset, header, method=1):
    """
    To get unique observations in the loaded pandas DataFrame column
    :param dataset:
    :param header:
    :param method: Method to perform the unique (default method=1 for pandas and method=0 for numpy )
    :return:
    """
    try:
        if method == 0:
            # With Numpy
            observations = np.unique(dataset[[header]])
        elif method == 1:
            # With Pandas
            observations = pd.unique(dataset[header].values.ravel())
        else:
            observations = None
            print ("Wrong method type, Use 1 for pandas and 0 for numpy")
    except Exception as e:
        observations = None
        print ("Error: {error_msg} /n Please check the inputs once..!".format(error_msg=e.message))
    return observations

print("In unique_observations")

def feature_target_frequency_relation(dataset, f_t_headers):

    """
    To get the frequency relation between targets and the unique feature observations
    :param dataset:
    :param f_t_headers: feature and target header
    :return: feature unique observations dictionary of frequency count dictionary
    """

    feature_unique_observations = unique_observations(dataset, f_t_headers[0])
    unique_targets = unique_observations(dataset, f_t_headers[1])

    frequencies = {}
    for feature in feature_unique_observations:
        frequencies[feature] = {unique_targets[0]: len(
            dataset[(dataset[f_t_headers[0]] == feature) & (dataset[f_t_headers[1]] == unique_targets[0])]),
            unique_targets[1]: len(dataset[(dataset[f_t_headers[0]] == feature) & (dataset[f_t_headers[1]] == unique_targets[1])])}
    return frequencies

print("In feature_target_frequency_relation")

def train_logistic_regression(train_x, train_y,test_x):
    """
    Training logistic regression model with train dataset features(train_x) and target(train_y)
    :param train_x:
    :param train_y:
    :return:
    """
    
    logistic_regression_model.fit(train_x, train_y)
    
    return logistic_regression_model

print("In train_logistic_regression")

def model_accuracy(trained_model, features, targets):
    """
    Get the accuracy score of the model
    :param trained_model:
    :param features:
    :param targets:
    :return:
    """
    accuracy_score = trained_model.score(features, targets)
    return accuracy_score

print("In model_accuracy")


def main():
    """
    Logistic Regression classifier main
    :return:
    """

    # Load the data set for training and testing the logistic regression classifier
    dataset = pd.read_csv(DATA_SET_PATH)
    print ("Number of Observations :: ", len(dataset))


    # Get the first observation
    print(dataset.head())

    headers = dataset_headers(dataset)
    print ("Data set headers :: {headers}".format(headers=headers))

    training_features = ['Gender', 'Glucose', 'Body_Temp','Heart_Rate']
    target = 'Malaria'

    # Train , Test data split
    train_x, test_x, train_y, test_y = train_test_split(dataset[training_features], dataset[target], train_size=0.993)
    print('\n')
    print("Model is training..")
    print('\n')
    print("Model has been trained successfully")
    print('\n')
    print("train_x size :: ", train_x.shape)
    print("train_y size :: ", train_y.shape)
    print('\n')
    print("Inputs from user - \n", test_x)
    print('\n')

    for feature in training_features:
        feature_target_frequencies = feature_target_frequency_relation(dataset, [feature, target])

    # Training Logistic regression model
    trained_logistic_regression_model = train_logistic_regression(train_x, train_y,test_x)

    train_accuracy = model_accuracy(trained_logistic_regression_model, train_x, train_y)

    #for row in dataset:
        #if row==112:
          #      test_x=row
           #     print(row)
                
    # Testing the logistic regression model
    test_accuracy = model_accuracy(trained_logistic_regression_model, test_x, test_y)
    print("edu_target_frequencies :: ", feature_target_frequency_relation(dataset, [training_features[3], target]))
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('System intialising')
    print('\n')
    print('Status of sensors - "True"')
    print('\n')
    print('Training the model . . .')
    print('\n')
    print('Testing the model . . .')
    print('\n')
    print("Inputs from user - \n", test_x)
    print('\n')
    print('Malarial Presence: ',logistic_regression_model.predict(test_x))
    print('[0]: Not affected with malaria')
    print('[1]: Affected with malaria')
    print('\n')
    print("Train Accuracy (%) :: ", train_accuracy*100,'%')
    print('\n')
    print("Test Accuracy (%)  :: ", test_accuracy*100,'%')
    print('\n')

print("In main")

if __name__ == "__main__":
    main()
