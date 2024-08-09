# Machine Learning - Life Expectancy


## Tabel of Content

 - [Introduction](#Introduction)
 - [Dataset](#Dataset)
 - [Project Structure](#Project-Structure)
 - [Installation](#Installation)
 - [Feature Correlation](#Feature-Correlation)
 - [Usage](#Model-Training)
 - [Modeling](#Modeling)
 - [Results](#Results)
 - [Contact](#Contact)

## Introduction

## Dataset

Here is a preview of the life expectancy dataset. The dataset used for this project can be found [here](https://github.com/ndanh318/Life-Expectency/tree/master/data/sources)
| Country                                              | Year | Status     | Life expectancy | Adult Mortality | infant deaths | Alcohol | percentage expenditure | Hepatitis B | Measles | BMI  | under-five deaths | Polio | Total expenditure | Diphtheria | HIV/AIDS | GDP         | Population  | thinness  1-19 years | thinness 5-9 years | Income composition of resources | Schooling |
|------------------------------------------------------|------|------------|-----------------|-----------------|---------------|---------|------------------------|-------------|---------|------|-------------------|-------|-------------------|------------|----------|-------------|-------------|----------------------|--------------------|---------------------------------|-----------|
| Afghanistan                                          | 2015 | Developing | 65              | 263             | 62            | 0.01    | 71.27962362            | 65          | 1154    | 19.1 | 83                | 6     | 8.16              | 65         | 0.1      | 584.25921   | 33736494    | 17.2                 | 17.3               | 0.479                           | 10.1      |
| Afghanistan                                          | 2014 | Developing | 59.9            | 271             | 64            | 0.01    | 73.52358168            | 62          | 492     | 18.6 | 86                | 58    | 8.18              | 62         | 0.1      | 612.696514  | 327582      | 17.5                 | 17.5               | 0.476                           | 10        |
| Afghanistan                                          | 2013 | Developing | 59.9            | 268             | 66            | 0.01    | 73.21924272            | 64          | 430     | 18.1 | 89                | 62    | 8.13              | 64         | 0.1      | 631.744976  | 31731688    | 17.7                 | 17.7               | 0.47                            | 9.9       |
| Afghanistan                                          | 2012 | Developing | 59.5            | 272             | 69            | 0.01    | 78.1842153             | 67          | 2787    | 17.6 | 93                | 67    | 8.52              | 67         | 0.1      | 669.959     | 3696958     | 17.9                 | 18                 | 0.463                           | 9.8       |
| Afghanistan                                          | 2011 | Developing | 59.2            | 275             | 71            | 0.01    | 7.097108703            | 68          | 3013    | 17.2 | 97                | 68    | 7.87              | 68         | 0.1      | 63.537231   | 2978599     | 18.2                 | 18.2               | 0.454                           | 9.5       |


## Project Structure
```bash
life_expectency/
├── data/			        # Data files
├── images/                   		# Saved evaluate
├── models/                   		# Saved models
├── src/                      		# Source code for the project
│   ├── config.py           		# Script for configuration settings
│   ├── download_dataset.py             # Script for download dataset
│   ├── train.py                        # Script for training models
├── requirements.txt          		# Python packages required
├── README.md                 		# Project documentation
```

## Installation

To run this project locally, follow these steps:

**1. Clone the repository**
```bash
 git clone https://github.com/ndanh318/Life-Expectency.git
```
**2. Navigate to the project directory**
```bash
cd life_expectancy
```
**3. Install the required packages**
```bash
pip install -r requirements.txt
```

## Feature Correlation

The heatmap below shows the correlations between different features in the stroke classification dataset. The values range from -1 (strong negative correlation) to 1 (strong positive correlation).

![Correlation Heatmap](https://github.com/ndanh318/Life-Expectency/blob/master/images/correlation.png)

## Usage
To train the model and evaluate it, you can use the provided scripts and notebooks.
### Download dataset
Download dataset using `download_data.py` script
```bash
python src/download_data.py
```

### Model training
Train the regression model using the `train.py` script.
```bash
python src/train.py
```
### Evaluate
Evaluate the model's performance using the `evaluation.py` script.
```bash
python src/evaluate.py
```

## Modeling

Several regression models were tested, including:

-   **Linear Regression**
-   **Random Forest Regressor**
-   **Decision Tree Regressor**

The models were evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²).

## Results

The best-performing model was the **Random Forest Regressor**, with the following metrics:

![Random Forest Regressor]()

-   **Mean Absolute Error (MAE):** 0.96
-   **Mean Squared Error (MSE):** 1.10
-   **R-squared (R²):** 2.97

These results indicate that the model can effectively predict life expectancy based on the provided features.

## Contact

For any questions or issues, please contact me at ngoduyanh8888@gmail.com.

