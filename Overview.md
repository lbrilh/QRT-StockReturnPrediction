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
Compare try with exclusive momentum (e.g. day 5-11,etc.) and overlapping momentum 5,10,15,20 day momentum 
Add median momentum as scale 
Compare how best model works when we add median as in previous best run (sector_date_median)
Exclude less important features

Summary: 
- Individual week momentum: not good 
    Fold 1 - Accuracy: 51.56%
    Fold 2 - Accuracy: 50.43%
    Fold 3 - Accuracy: 51.04%
    Fold 4 - Accuracy: 51.01%
    Accuracy: 51.01% [50.61 ; 51.41] (+- 0.40)

- 10 day momentum + median 
    Fold 1 - Accuracy: 52.15%
    Fold 2 - Accuracy: 50.31%
    Fold 3 - Accuracy: 51.72%
    Fold 4 - Accuracy: 51.79%
    Accuracy: 51.49% [50.79 ; 52.20] (+- 0.70)
    Global Accuracy: 0.5832391691252882

- 5, 10, 15, 20 day momentum + median
    Global Accuracy: 0.582063808693367

- 5, 10, 15, 20 day momentum + median + 20 day RSI
    Fold 1 - Accuracy: 52.46%
    Fold 2 - Accuracy: 50.34%
    Fold 3 - Accuracy: 51.49%
    Fold 4 - Accuracy: 51.87%
    Accuracy: 51.54% [50.76 ; 52.31] (+- 0.78)
    Global Accuracy: 0.5826610446851969

- 5, 10, 15, 20 day momentum + median + 10 day RSI
    Fold 1 - Accuracy: 52.38%
    Fold 2 - Accuracy: 50.32%
    Fold 3 - Accuracy: 51.46%
    Fold 4 - Accuracy: 51.94%
    Accuracy: 51.52% [50.76 ; 52.29] (+- 0.77)
    Global Accuracy:0.5824364839522689

- 10 day momentum + median + 10 day RSI
    Fold 1 - Accuracy: 52.06%
    Fold 2 - Accuracy: 50.32%
    Fold 3 - Accuracy: 51.67%
    Fold 4 - Accuracy: 51.86%
    Accuracy: 51.48% [50.80 ; 52.16] (+- 0.68)
    Global Accuracy: 0.5828426044267132

- 10 day momentum + median + 10 day RSI without mean volume, std volume and ratios of mean RET, VOLUME
    Fold 1 - Accuracy: 52.04%
    Fold 2 - Accuracy: 50.24%
    Fold 3 - Accuracy: 51.69%
    Fold 4 - Accuracy: 51.82%
    Accuracy: 51.45% [50.74 ; 52.16] (+- 0.71)
    Global Accuracy: 0.5806280533690082

- 5, 10, 15, 20 day momentum + median + 10 day RSI + 20 day Sum_ADL
    Fold 1 - Accuracy: 52.20%
    Fold 2 - Accuracy: 50.30%
    Fold 3 - Accuracy: 51.47%
    Fold 4 - Accuracy: 51.90%
    Accuracy: 51.46% [50.74 ; 52.19] (+- 0.72)
    Global Accuracy: 0.5832296133494189