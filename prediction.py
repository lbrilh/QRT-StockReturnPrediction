import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from lightgbm import LGBMClassifier
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import sweetviz as sv

_Xtrain = pd.read_csv("x_train.csv", index_col='ID')
_y = pd.read_csv("y_train.csv", index_col='ID')
_y[['RET']].replace({True: 1, False: 0}, inplace=True)

#train = pd.concat([_y,_Xtrain], axis=1)
_Xtest = pd.read_csv('x_test.csv', index_col='ID')

print('Number of elements in Sector: ', _Xtrain['SECTOR'].nunique())
print('Number of elements in Industries: ', _Xtrain['INDUSTRY'].nunique())
print('Number of elements in Industries_Group: ', _Xtrain['INDUSTRY_GROUP'].nunique())
print('Number of elements in Sub_Industries: ', _Xtrain['SUB_INDUSTRY'].nunique())

# Feature engineering
new_features = []

# Conditional aggregated features
shifts = [1]  # Choose some different shifts
statistics = ['mean', 'median', 'min', 'max']  # the type of stat
gb_features = ['SECTOR', 'DATE']
target_features = ['RET', 'VOLUME']
for target_feature in target_features:
    tmp_name = '_'.join(gb_features)
    for shift in shifts:
        for stat in statistics:
            name = f'{target_feature}_{shift}_{tmp_name}_{stat}'
            feat = f'{target_feature}_{shift}'
            new_features.append(name)
            for data in [_Xtrain]:
                data[name] = data.groupby(gb_features)[feat].transform(stat)

COLUMNS = ['STOCK', 'SECTOR', 'INDUSTRY_GROUP']
#COLUMNS = []
for day in range(6,21):
    COLUMNS.append(f'RET_{day}')
    COLUMNS.append(f'VOLUME_{day}')

print(_y)
_Xtrain.drop(columns=COLUMNS, inplace=True)

_Xtest.drop(columns=COLUMNS, inplace=True)

parameters = {
    'boosting_type': ['rf', 'gbdt'],
    'num_estimators': [100, 500, 1000, 10000],
    'num_leaves': [31, 50, 100],
    'max_depth': [2**3, 2**4, 20],
    'random_state': [0],
    'n_jobs': [-1],
    'min_child_samples': [20, 100, 1000], 
    'feature_fraction': [0.5,0.6,0.7,0.8,0.9], 
    'early_stopping_rounds': [100], 
    'verbose': [-1], 
    'objective': ['binary']
}

search = GridSearchCV(LGBMClassifier(), param_grid=parameters, n_jobs=-1, scoring='accuracy')
search.fit(_Xtrain, _y)

#model = LGBMClassifier(boosting_type='gbdt', feature_fraction=0.8, num_estimators=10000)

#model.fit(_Xtrain,outcome)

#_ypred = model.predict(_Xtest)
#df_results = pd.DataFrame({'RET': _ypred})
#df_results.set_index(keys='ID', inplace=True)
#df_results.to_csv('y_test.csv')

print('Accuracy', accuracy_score(_y, search.best_estimator_.predict(_Xtrain)))

pd.set_option('display.max_columns', None) 
_feat_imp = pd.DataFrame([search.best_estimator_.feature_name_,search.best_estimator_.feature_importances_])
print(_feat_imp)

raise ValueError

_Xytrain = pd.merge(_y, _Xtrain)
print(_Xytrain.head())
analyze_report = sv.analyze(_Xytrain, target_feat='RET')
analyze_report.show_html()


for column in _Xtrain.columns: 
    print('Missing values in ', column, ': ', _Xtrain[column].isna().sum())
    print()

RET_columns = [f'RET_{day}' for day in range(1,21)]
VOLUME_columns = [f'VOLUME_{day}' for day in range(1,21)]

pd.set_option('display.max_columns', None) 
print(_Xtrain.agg(['min', 'max']))
print(_Xtrain[['RET_1']].std())
# min max show large range --> standardscaler 
Preprocessor = Pipeline(steps=[
    #('impute', SimpleImputer(strategy='mean')),
    ('scale', StandardScaler()) 
])

pipeline = Pipeline(steps=[
    ('preprocessing', ColumnTransformer([('RET', Preprocessor, RET_columns)]))
])

_Xtrain_scaled = pd.DataFrame(pipeline.fit_transform(_Xtrain), columns=RET_columns)
print(_Xtrain_scaled[['RET_1']])
sum_dropped = 0
print(_Xtrain_scaled[abs(_Xtrain_scaled['RET_1']) > 3][['RET_1']].count())