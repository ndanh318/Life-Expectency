import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from config import *

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, KFold
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def regression(reg, params, title):
    cv = KFold(n_splits=3, shuffle=True, random_state=42)
    # Randomize Grid Search
    n_iter_search = 20
    model = RandomizedSearchCV(reg,
                               param_distributions=params,
                               n_iter=n_iter_search,
                               scoring="r2",
                               n_jobs=6,
                               cv=cv,
                               verbose=2,
                               random_state=42)
    model.fit(x_train, y_train)
    print("The best score is {}".format(model.best_score_))
    print("The best params are {}".format(model.best_params_))

    # evaluate
    y_predict = model.best_estimator_.predict(x_test)
    print("R2: {}".format(r2_score(y_test, y_predict)))
    print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))
    print("MSE: {}".format(mean_squared_error(y_test, y_predict)))

    # save model
    model_path = "../models"
    model_pkl_file = "{}_model.pkl".format(title)
    with open(os.path.join(model_path, model_pkl_file), 'wb') as file:
        pickle.dump(model, file)


def boxplot(data, cols, save=False, title="Figure"):
    fig, axes = plt.subplots(4, 5, figsize=(10, 8))
    fig.suptitle("Boxplots of Numerical Columns", fontsize=16)
    axes = axes.flatten()
    for i, col in enumerate(cols):
        sns.boxplot(y=data[col], ax=axes[i])
        axes[i].set_title(col)

    if save:
        plt.savefig("../images/{}".format(title), bbox_inches="tight")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../data/sources/Life Expectancy Data.csv")
    print(data.info())

    target = "Life expectancy "
    data = data.dropna(subset=[target])
    categorical_cols = data.select_dtypes(include="object").columns
    numerical_cols = data.select_dtypes(include=("float64", "int64")).columns

    # visualize
    boxplot(data, numerical_cols, save=True, title="data_visualize")

    # remove outlier
    outlier_cols = ['Adult Mortality', 'infant deaths',
                    'percentage expenditure',
                    'Hepatitis B', 'Measles ',
                    'under-five deaths ', 'Polio',
                    'Total expenditure', 'Diphtheria ',
                    ' HIV/AIDS', 'GDP', 'Population',
                    ' thinness  1-19 years',
                    ' thinness 5-9 years',
                    'Income composition of resources',
                    'Schooling']
    for col in outlier_cols:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        data[col] = np.where((data[col] > upper_bound) | (data[col] < lower_bound), np.mean(data[col]), data[col])

    boxplot(data, numerical_cols)

    # correlation
    plt.figure(figsize=(10, 8))
    corr = data[numerical_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".1f")
    plt.savefig("../images/correlation", bbox_inches="tight")
    plt.show()

    # splitting data
    x = data.drop(target, axis=1)
    y = data[target]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # # preprocessing
    numerical_cols = numerical_cols.drop(labels=[target])
    categorical_transform = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    numerical_transform = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("categorical", categorical_transform, categorical_cols),
        ("numerical", numerical_transform, numerical_cols),
    ])

    for (name, model), param in zip(models.items(), params):
        reg = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ])
        regression(reg, param, name)

