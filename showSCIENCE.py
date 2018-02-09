from models.StrTape import StrTape
from pydybm.time_series.rnn_gaussian_dybm import RNNGaussianDyBM
from pydybm.base.sgd import RMSProp
from sklearn.metrics import mean_squared_error
import os
import numpy as np
import matplotlib.pyplot as plt

def MSE(y_true,y_pred):
    MSE_each_coordinate = mean_squared_error(y_true,y_pred,multioutput="raw_values")
    return np.sum(MSE_each_coordinate)

def RMSE(y_true,y_pred):
    return np.sqrt(MSE(y_true,y_pred))



# making input "SCIENCE"
tape = StrTape()
tape.inputStr("SCIENCE")
timeSeries = []
for _ in range(tape.getLength()):
    timeSeries.append(np.array(tape.getNext()[1]))

#DyBM initialization parameters
in_dim   =       7 # dimension of the input time-series
out_dim  =       7 # dimension of the expected output time-series
rnn_dim  =     100 # dimension of RNN layer
max_iter = 1000000 # maximum number of learning epochs/iterations to run
SGD      = RMSProp # setting the SGD optimization method  

#setting RNN-G-DyBM hyperparameters
delay = 10
decay = [0.25, 0.50, 0.75]
sparsity = 0.1
spectral_radius = 0.95
leak = 1.0
learning_rate = 0.001

# Create and initialize a RNN-Gaussian DyBM
model = RNNGaussianDyBM(in_dim,out_dim, \
                        rnn_dim,spectral_radius,sparsity,\
                        delay=delay,decay_rates =decay,\
                        leak=leak, 
                        SGD=SGD())  
model.set_learning_rate(learning_rate)

errorList = []
for t in range(max_iter):
    #initialize the memory units in DyBM
    model.init_state() 
    result= model.learn(timeSeries, get_result=True)
    result= model.learn(timeSeries, get_result=True)
    #calculate the prediction error
    error = RMSE(result["actual"],result["prediction"])
    errorList.append(error)
    if len(errorList) > 10 and sum(errorList[-10:]) == 0:
        break
    if t%500 != 0:
        continue
    # pred = model.get_predictions(timeSeries)
    pred = list(timeSeries)
    for _ in range(len(timeSeries)):
        model.init_state()
        for p in pred:
            model._update_state(p)
        pred.append(model.predict_next())

    forprint = ["" for _ in range(len(pred[0]))]
    for i in range(len(forprint)):
        for p in pred:
            if p[i] > 0.5:
                forprint[i] += "■"
            else:
                forprint[i] += "□"
    # os.system("cls")
    print ('%d\t\tLearning epoch RMSE : %.5f' %(t, error))
    for f in forprint:
        print(f)
    plt.title("RMSE")
    plt.plot(errorList)
    plt.pause(0.0001)
    plt.clf()
     
