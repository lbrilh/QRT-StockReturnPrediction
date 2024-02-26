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
Add non-linear features like volume weighted average price adjustment, price volume trend
Add Mean of RET grouped by SECTOR + DATE (rn only grouped by STOCK + DATE)

Do np.arcsinh transformation of volume


Summary: 
Hyperparameter tuning leads to overfitting and we achieve worse results than using default hyperparameter. RSI should be left to 20. 
Arcsinh transformation of volume does not help.

BEST SUBMISSION
- 10 day momentum + 20 day RSI + 5 day ADL grouped by sector

    Fold 1 - Accuracy: 52.54%
    Fold 2 - Accuracy: 50.63%
    Fold 3 - Accuracy: 51.77%
    Fold 4 - Accuracy: 52.03%
    Accuracy: 51.74% [51.04 ; 52.44] (+- 0.70)