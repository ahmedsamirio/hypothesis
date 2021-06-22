# hypothesis-test

hypothesis-test is a python package for running hypothesis tests directly on pandas dataframes.

# Installation 

## Dependencies

hypothesis-test requires:
* Python (>=3.7)
* NumPy (>= 1.19.2)
* pandas (>= 1.1.3)
* matplotlib (>= 3.3.2)

# Project Motivation

This project was done after writing several classes and functions to run multiple hypothesis tests on a pandas dataframe for an analysis, which later inspired me to package them and use them easily at anytime, and share them as they might be useful to other people as well.


# Usage

The package until now is designed to run a hypothesis test of difference in a feature average between two groups. So you need to have two groups that you want to figure out the presence of a statistical difference between.

```python
test = HypothesisTest(df, group_feature, test_feature)
```

`group_feature` is the feature that divides the dataframe into two groups, which should be a binary feature with 1 for positive group and 0 for negative group.  
`test_feature` is the feature whose average difference will be tested for significance using bootstraped samples from the dataframe.

Then you would run and visualize the test results using
```python
test.run_test(print_results=True, plot_results=True)
```
`print_results` will print the observed difference in the dataset, and the p-value, and whether the null hypothesis (that there is a statistical difference betwee the two groups) was rejected or not.  
`plot_results` will plot the sampling distribution of the difference between two groups, and the null distribution with a vertical line showing where the observed difference in the dataset lies on the null distribution.

