metric: accuracy of the predicted residual stock return sign (predict whether it goes up or down)

I do not pursue a classical time series analysis approach since this is a classification task.

From a first EDA, no feature seems to be highly influential of the outcome. To gain a better understanding of feature importance, I will no proceed with fitting a RandomForest. The RF feature importance suggest to aggregate features older than >= 6 days in one. 

first submission resultet in test score of 0.49

Ideas: 
Feature engineering
    - Ask chatgpt for possible features
    - add min/max to statistics?
    - Average of last 5 and last 20 days (also conditioned?)
    - Ratio features
    - Consider more metrics

look at rule to decide if up or down 
How are they doing CV?