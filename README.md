# Stock Return Prediction Challenge Solution

## Overview

This repository contains my solution for QRT's stock return prediction challenge. Given the low signal-to-noise ratio in financial data, extracting meaningful patterns is extremely challenging. To do that, I used feature engineering to create aggregated features reducing the noise in the data. 


## Challenge Description

The challenge aims to predict the residual return of a stock in the US market using 20 days of historical data, including residual stock returns and relative volumes. The key objective is to predict the sign of a stock's residual return. Data provided includes various features like industry indexes, sector indexes, and historical returns and volumes.

For more details about the challenge, visit the [official website](https://challengedata.ens.fr/participants/challenges/23/).

## Data Description

The datasets are split into inputs and outputs, comprising:

- **Input datasets:** 47 columns including date index, stock index, industry and sector indexes, historical residual returns, and relative volumes.
- **Output datasets:** 2 columns, including a unique row identifier and the binary target, indicating the sign of the residual stock return.

The challenge provides 418,595 observations for training and 198,429 for testing.

## Solution Approach

### Data Preparation and Preprocessing
- **Data Loading:** Training and test datasets were loaded with a focus on recent historical data (last 5 days) to reduce noise.
- **Preprocessing:** Initial preprocessing involved dropping historical returns and relative volumes beyond the last 5 days to concentrate on the most relevant temporal patterns. Additonally, all rows containing only missing values for the returns over the past 5 days have been dropped. After EDA the missing values have been imputed using its median. 

### Analysis and Feature Engineering
- **Feature Engineering:** New featues include: Average return conditioned on group and sector; weekly moving average and volatility (stdev) of stock & volume; relative volume & return of stock compared to its sector; residual return momentum; ten day sector return & volume volatility; relative strength index per sector; advance-decline line conditioned on sector. Detailed explanaions can be found in the notebook.

### Model Selection and Training
- **Models Used:** Employed RandomForestClassifier with small depth (to prevent overfitting) and a relatively large number of trees. To identify trends quickly, LGBM's version of RF has been used. 
- **Parameter Tuning and Validation:** Conducted model evaluation using 4-Fold cross-validation.

### Results / Achievements

- **Accuracy:** Achieved an accuracy of **0.5197** (username: lucabri), surpassing the benchmark score of 0.5131.
- **Ranking:** Placeing me **33rd out of 313** participants.

## Usage

To run this solution:

1. Clone this repository to your local machine.
2. Create a virtual environment including all packages (run: conda env create -f environment.yml)
3. Place the challenge data files in the appropriate directory (as specified in the notebook).
4. Open the Jupyter Notebook and execute the cells sequentially.