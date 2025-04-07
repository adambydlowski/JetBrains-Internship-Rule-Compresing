# JetBrains-Internship-Rule-Compresing

## Author
Adam Bydłowski

## Description
To address the task of compressing the rule set while preserving the key insights, we developed a methodical approach that focuses on reducing redundancy, optimizing for generalization, and ensuring that the core relationships defining the prediction of an "old" donor remain intact. The solution involves several key steps, outlined below:

### 1. Understanding the Data and Rules:
The input consisted of two main components:

A dataset with multiple biomarkers, where each column represents a biomarker and the values are either `True`, `False`, or `NA`.

A set of generated rules that correlate specific biomarkers (or combinations of biomarkers) to the label `donor_is_old`.

Each rule is structured as:

``` code
LHS => donor_is_old
```
where the left-hand side (LHS) is composed of predicates (biomarkers), which are either present (`True`) or negated (`NOT`), connected by the `AND` operator. The right-hand side (RHS) always states `donor_is_old == True`.

### 2. Preprocessing the Data:
Before performing rule compression, we preprocess the dataset to handle missing values (`NA`). We ignore these values during rule evaluation to ensure that incomplete data doesn't interfere with the compression process.

### 3. Identifying Redundant Rules:
A significant part of the solution is identifying and eliminating redundant rules. We accomplish this by:

Checking if one rule is a more specific version of another: If the conditions of one rule are fully contained within another (e.g., `A AND B => donor_is_old` is more general than `A AND B AND C => donor_is_old`), the more specific rule is removed.

Removing duplicate literals in given rule (e.g. `A AND A => B` is changed to `A => B`).

### 4. Ranking and Scoring Rules:
After eliminating redundancy and simplifying the rules, we rank the remaining rules based on their usefulness. This is done by considering factors such as:

Support: How frequently the rule holds true in the dataset.

Confidence: The reliability of the rule in predicting `donor_is_old`.

Lift: How much more likely `donor_is_old` is to be true when the rule holds. We use these metrics to identify the most important and useful rules and retain only the top rules with the highest scores.

Length: There is a length penalty. Longer the rule => lower this metric.

### 5. Output:
The final step is to produce the compressed rule set. The output contains:

The simplified and compressed list of rules that maintain the core predictive power.

These rules are sorted by their usefulness, ensuring that the most relevant and generalizable rules are prioritized.

## Project Structure

The project consists of the following files:

`compress.py` – file that manages compressing process.\
`redundant_rules.py` – file in charge of getting rid of redundant rules.\
`scoring.py` – file in charge of scoring the rules and cutting the worst rules from results.\
`main.py` – the main file that initiates the entire compressing process.

## Installation and usage

### Requirements

- Python 3.13
- Python's `sympy` package
- Python's `pandas` package

### Usage
To run the program specify your desired results in `main.py` and then simply run it.

