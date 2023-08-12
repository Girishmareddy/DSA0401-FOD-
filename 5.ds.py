import numpy as np
import matplotlib.pyplot as plt
fuel_efficiency = np.array([25, 30, 28, 22, 35, 26])
average_efficiency = np.mean(fuel_efficiency)
model_index_1 = 2
model_index_2 = 4  
initial_efficiency = fuel_efficiency[model_index_1]
improved_efficiency = fuel_efficiency[model_index_2]
percentage_improvement = ((improved_efficiency - initial_efficiency) / initial_efficiency) * 100

print("Average fuel efficiency:", average_efficiency, "mpg")
print("Percentage improvement between models", model_index_1, "and", model_index_2, ":", percentage_improvement, "%")
plt.hist(fuel_efficiency)



