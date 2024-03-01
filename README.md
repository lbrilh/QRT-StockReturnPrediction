# Stock Return Prediction Challenge Solution

## Overview

This repository contains my solution for a stock return prediction challenge inspired by a Kaggle-like competition. The challenge focuses on employing quantitative investment strategies by analyzing historical data to predict the trend of a stock in the near future. Given the low signal-to-noise ratio in financial data, extracting meaningful patterns is extremely challenging. This project leverages Machine Learning techniques to analyze vast amounts of data and identify patterns that can inform better trading decisions.

## Challenge Description

The challenge aims to predict the residual return of a stock in the US market using 20 days of historical data, including residual stock returns and relative volumes. The key objective is to predict the sign of a stock's residual return, excluding the market impact. Data provided includes various features like industry indexes, sector indexes, and historical returns and volumes.

For more details about the challenge, visit the [official website](https://challengedata.ens.fr/participants/challenges/23/).

## Data Description

The datasets are split into training inputs and outputs, and test inputs, comprising:

- **Input datasets:** 47 columns including date index, stock index, industry and sector indexes, historical residual returns, and relative volumes.
- **Output datasets:** 2 columns, including a unique row identifier and the binary target, indicating the sign of the residual stock return.

The challenge provides 418,595 observations for training and 198,429 for testing.

## Solution Approach

This solution employs [describe your methodology, e.g., a specific machine learning model or algorithm, feature engineering techniques, data preprocessing steps].

### Key Features

- Utilizes historical residual returns and relative volumes.
- Incorporates additional information such as industry and sector indexes.
- [Any other key features or data processing steps used in your solution].


## Usage

To run this solution:

1. Clone this repository to your local machine.
2. Place the challenge data files in the appropriate directory (as specified in the notebook).
3. Open the Jupyter Notebook and execute the cells sequentially.

## Results and Evaluation

This solution [briefly describe your results and how they compare to the benchmark or other solutions, if applicable].

## License

This project is open-sourced under the [specify license] license.

## Contact

For any inquiries or feedback, please reach out to [your email or contact information]