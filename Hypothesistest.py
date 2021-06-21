import matplotlib.pyplot as plt
import numpy as np

class HypothesisTest:
    """ Generic hypothesis test class for calculating
        and visualizing a hypothesis test of difference
        between two groups using the bootstrap method
        on pandas dataframes.
        
        Attributes:
            df (DataFrame)
            group_feature (str) representing the feature that split the data into two groups
            test_feature (str) representing the feature to test the difference in\
            samples (int) respresenting the number of samples for bootstraping the data
    """
    
    def __init__(self, df, group_feature, test_feature, samples=10000):

        
        self.df = df
        self.size = self.df.shape[0]
        self.group_feature = group_feature
        self.test_feature = test_feature
        self.samples = samples
        
    def bootstrap(self):
        """Function to resample the data multiple times and test the difference 
        in test_feature between the two groups split using group_feature"""
        
        diffs = []
        for i in range(self.samples):
            sample = self.df.sample(self.size, replace=True)
            sample_positive = sample.query(f'{self.group_feature} > 0')
            sample_negative = sample.query(f'{self.group_feature} == 0')
            feature_diff = sample_prof[self.test_feature].median() - sample_non_prof[self.test_feature].median()
            diffs.append(feature_diff)
        return np.array(diffs)
            
    def calculate_difference(self, feature):
        """Function for calculation of the sample difference in test_feature between the two
        groups split using group_feature"""
        
        median_positive = self.df.query(f'{self.group_feature} > 0')[feature].median()
        median_negative = self.df.query(f'{self.group_feature} == 0')[feature].median()
        return median_positive - median_negative
        
    def calculate_null(self, feature, std, size):
        """Function for simulating the null hypothesis of the difference in test_feature between
        the two groups split using group_feature"""
        
        null_vals = np.random.normal(0, std, size)
        return null_vals
    
    def calculate_p_val(self, null_vals, obs_diff):
        """Function to calculate p-value which is the probability that the statistic observed came
        from the null distribution"""
        
        p = (null_vals > obs_diff).mean()
        return p
    
    def run_test(self, print_results=True, plot_results=True):
        """Function to run the hypothesis test
        
        Args:
            print_results (bool)
            plot_results (bool)
            
        """
        self.obs_diff = self.calculate_difference(self.test_feature) 
        self.median_diffs = self.bootstrap()
        self.null_vals = self.calculate_null(self.test_feature, self.median_diffs.std(), self.samples)
        self.p = self.calculate_p_val(self.null_vals, self.obs_diff)
        if print_results or plot_results:
            self.final_results()
    
    def plot_sampling_dist(self):
        """Function to plot the sampling distribution of the statistic after bootstraping"""
        
        plt.hist(self.median_diffs)
        plt.title('Sampling Distribution of {} Median Difference'.format(self.feature.capitalize()),
                                                                         fontsize=7, fontfamily='serif')
        plt.xticks(fontsize=5, fontfamily='serif', fontweight='light')
        plt.yticks(fontsize=5, fontfamily='serif', fontweight='light')
                  
    def plot_null_dist(self):
        """Function to plot the null distribution of the statistic which is derived from the 
        null hypothesis (the hypothesis that there is no statistical difference between the 
        two groups being compared)"""
        
        plt.hist(null_diffs)
        plt.axvline(self.obs_diff, linestyle='-', color='red', alpha=0.8)
        plt.title('Null Distribution of {} Median Difference'.format(self.feature.capitalize()),
                                                                     fontsize=7, fontfamily='serif')
        plt.xticks(fontsize=5, fontfamily='serif', fontweight='light');
        plt.yticks(fontsize=5, fontfamily='serif', fontweight='light');
        
        
    def final_results(self, print_results, plot_results):
        """Function to print and/or plot the results of a finished hypothesis test
        
        Args:
            print_results (bool): print the observed difference, p-value and result of the test
                                  (Failed to reject or Rejected the null hypothesis)
            plot_results (bool): plots the sampling and the null distribution, and shows where the 
                                 observed difference lies on the null distribution
        
        """
        if print_results:
            print('Observed difference:', self.obs_diff)
            print('P-Value:', self.p)
            print('Failed to reject' if self.p > 0.05 else 'Rejected', 'the null hypothesis.')
            
        if plot_results:
            fig = plt.figure(figsize=(9, 3))
            plt.subplot(1, 2, 1)
            self.plot_sampling_dist()
            plt.subplot(1, 2, 2)
            self.plot_null_dist()
