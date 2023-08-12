import numpy as np
from scipy import stats
conversion_rate_A = np.array([0.12, 0.15, 0.18, 0.10, 0.14, 0.16, 0.11, 0.13, 0.09, 0.17])
conversion_rate_B = np.array([0.09, 0.11, 0.13, 0.08, 0.12, 0.14, 0.10, 0.11, 0.07, 0.15])
mean_A = np.mean(conversion_rate_A)
mean_B = np.mean(conversion_rate_B)
std_A = np.std(conversion_rate_A, ddof=1)
std_B = np.std(conversion_rate_B, ddof=1)
n_A = len(conversion_rate_A)
n_B = len(conversion_rate_B)
t_statistic = (mean_A - mean_B) / np.sqrt((std_A*2 / n_A) + (std_B*2 / n_B))
df = n_A + n_B - 2
p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df=df))
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference.")
    
print("Calculated t-statistic:", t_statistic)
print("Degrees of freedom:", df)
print("Calculated p-value:", p_value)
