import numpy as np
import scipy.stats as stats
new_drug_data = [2.5, 3.1, 2.9, 2.8, 3.2, 2.7, 2.8, 3.0, 2.6, 3.3,
                 2.4, 2.9, 3.1, 2.7, 3.0, 3.2, 2.8, 3.1, 3.0, 2.6,
                 3.2, 2.9, 2.8, 3.1, 2.7, 2.6, 2.9, 2.8, 3.0, 3.2,
                 3.1, 2.8, 2.7, 2.9, 3.0, 2.8, 3.3, 2.5, 3.1, 2.7,
                 2.9, 2.8, 3.2, 2.6, 3.1, 2.9, 2.7, 3.0]
placebo_data = [1.6, 1.8, 1.5, 1.9, 1.7, 1.4, 1.9, 1.6, 1.8, 1.7,
                 1.5, 1.6, 1.7, 1.8, 1.9, 1.5, 1.6, 1.8, 1.7, 1.9,
                 1.6, 1.5, 1.7, 1.9, 1.8, 1.6, 1.5, 1.9, 1.8, 1.6,
                 1.7, 1.6, 1.8, 1.9, 1.5, 1.7, 1.6, 1.8, 1.9, 1.7,
                 1.5, 1.7, 1.8, 1.6, 1.9, 1.7, 1.5, 1.8]
alpha = 0.05
mean_new_drug = np.mean(new_drug_data)
std_dev_new_drug = np.std(new_drug_data, ddof=1)  
mean_placebo = np.mean(placebo_data)
std_dev_placebo = np.std(placebo_data, ddof=1)
t_score = stats.t.ppf(1 - alpha/2, df=49)
margin_of_error_new_drug = t_score * (std_dev_new_drug / np.sqrt(50))
margin_of_error_placebo = t_score * (std_dev_placebo / np.sqrt(50))
confidence_interval_new_drug = (mean_new_drug - margin_of_error_new_drug, mean_new_drug + margin_of_error_new_drug)
confidence_interval_placebo = (mean_placebo - margin_of_error_placebo, mean_placebo + margin_of_error_placebo)
print("95% Confidence Interval (New Drug Group):", confidence_interval_new_drug)
print("95% Confidence Interval (Placebo Group):", confidence_interval_placebo)
