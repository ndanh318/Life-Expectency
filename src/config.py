from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

# models
models = {
    "linear_regression": LinearRegression(),
    "random_forest": RandomForestRegressor(),
    "decision_tree": DecisionTreeRegressor(),
}

# params
lr_params = {
    'preprocessor__categorical__imputer__strategy': ["most_frequent", "constant"],
    'preprocessor__numerical__imputer__strategy': ["mean", "median"],
    'model__copy_X': [True, False],
    'model__fit_intercept': [True, False],
    'model__n_jobs': [1, 5, 10, 15, None],
    'model__positive': [True, False]
}
rf_params = {
    'preprocessor__categorical__imputer__strategy': ["most_frequent", "constant"],
    'preprocessor__numerical__imputer__strategy': ["mean", "median"],
    'model__bootstrap': [True, False],
    'model__max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
    'model__max_features': ['auto', 'sqrt', "log2"],
    'model__min_samples_leaf': [1, 2, 4],
    'model__min_samples_split': [2, 5, 10],
    'model__n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
}
dtree_params = {
    'preprocessor__categorical__imputer__strategy': ["most_frequent", "constant"],
    'preprocessor__numerical__imputer__strategy': ["mean", "median"],
    "model__splitter": ["best", "random"],
    "model__max_depth": [1, 3, 5, 7, 9, 11, 12],
    "model__min_samples_leaf": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "model__min_weight_fraction_leaf": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    "model__max_features": ["auto", "log2", "sqrt", None],
    "model__max_leaf_nodes": [None, 10, 20, 30, 40, 50, 60, 70, 80, 90]
}
params = [lr_params, rf_params, dtree_params]
