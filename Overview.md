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


RFClassifier uses only sqrt(n_features) in each prediction! << 0.5

Try LGBM and RF using only sqrt(n_features)/n_features as feature fraction and compare (maybe using a table)
It seems like even 0.5 might use way tooo many features



TODO's: 
Adding aggregated / conditional volume metrics does not seem valuable

Add relative RET / Sector Return
Add stddev ret week 1 / Volume or overall return of the stock in week 1

Adjusted return over volume to get returns due to volume shortage clear (COULD BE HUGHE)