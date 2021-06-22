import matplotlib.pyplot as plt
import numpy as np
from .Hypothesistest import HypothesisTest


class MultipleTests(HypothesisTest):
    """ Hypothesis testing class for running and visualizing 
    multiple hypothesis tests between two groups in a Pandas
    DataFrame.
    
    Attributes:
        df (DataFrame)
        group_feature (str): The feature used to split the data into two groups.
        test_features (list): A list with all the features to test.
        samples (int): The number of samples (with replacement) taken from the data
                       in bootstraping.
    """
    
    def __init__(self, df, group_feature, test_features, samples=10000):
        HypothesisTest.__init__(self, df, group_feature, _, samples)
        self.test_features = self.test_features
        self.positive_group_averages = {}
        self.negative_group_averages = {}
        self.observed_differences = {}
        self.sampling_distributions = {}
        self.null_distributions = {}
        self.p_values = {}
        
        
    def bootstrap(self):
        """Function to resample the data multiple times and test the difference 
        in test_features between the two groups split using group_feature"""
        features_diffs = defaultdict(list)
        for i in range(self.samples):
            sample = self.df.sample(self.size, replace=True)
            sample_positive = sample.query(f'{self.group_feature} > 0')
            sample_negative = sample.query(f'{self.group_feature} == 0')
            feature_diff = 
            for feature in self.test_features:
                feature_diffs = sample_prof[feature].median() - sample_non_prof[feature].median()
                features_diffs[feature].append(feature_diffs)
        return features_diffs
    
    def run_test(self):
        """Function to run the hypothesis tests
        
        Args:
            print_results (bool)
            plot_results (bool)
            
        """
        self.observed_differences = {feature: self.calculate_difference(feature) for feature in self.test_features}
        self.sampling_distributions = self.bootstrap()
        self.null_distributions = {feature: self.calculate_null(feature, self.median_diffs[feature].std(),
                                                       self.samples) for feature in self.test_features}
        self.p_values = {feature: self.calculate_p_val(self.null_vals[feature],
                                                       self.obs_diff[feature]) for feature in self.test_features}
        return self.observed_differences, self.p_values

            
    def get_groups_averages(self):
        for feature in self.test_features:
            self.positive_group_average = self.df.query(f'{self.group_feature} > 0')[feature].median()
            self.negative_group_average = self.df.query(f'{self.group_feature} == 0')[feature].median()
            positive_group_averages[feature] = positive_group_average
            negative_group_averages[feature] = negative_group_average
        return self.positive_group_averages, self.negative_group_averages
    
    def get_results_df(self):
        results =  pd.DataFrame({'positive_average': self.positive_group_averages,
                                 'negative_average': self.negative_group_averages,
                                 'difference': self.observed_differences,
                                 'p_value': self.p_values})     
        return results
    

        
