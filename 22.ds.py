import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv("C:\\Users\\giris_pu2cvr5\\Downloads\\customer_reviews.csv")
ratings = data["rating"].values
confidence_level = float(input("Enter the confidence level (between 0 and 1): "))

sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1)
std_error = sample_std / np.sqrt(len(ratings))
degrees_of_freedom = len(ratings) - 1
t_score = np.abs(stats.t.ppf((1 - confidence_level) / 2, df=degrees_of_freedom))
margin_of_error = t_score * std_error
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error
print("Sample Mean Rating:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("Standard Error of the Mean:", std_error)
print("Degrees of Freedom:", degrees_of_freedom)
print("t-score:", t_score)
print("Margin of Error:", margin_of_error)
print(f"Confidence Interval for Mean Rating: ({confidence_interval_lower:.2f}, {confidence_interval_upper:.2f})")
