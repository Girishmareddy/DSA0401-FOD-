import numpy as np 
house_data = np.array([ 

    [3, 1200, 250000], 

    [4, 1500, 300000], 

    [5, 1800, 350000], 

    [4, 1600, 280000], 

    [5, 2000, 400000], 

    [6, 2200, 420000], 

    [3, 1400, 260000], 

    [4, 1700, 310000], 

    [5, 1900, 370000], 

    [4, 1800, 320000] 

]) 
bedrooms_column = house_data[:, 0]  

houses_with_more_than_four_bedrooms = house_data[bedrooms_column > 4] 

average_sale_price = np.mean(houses_with_more_than_four_bedrooms[:, 2])   

print("Average sale price of houses with more than four bedrooms:", average_sale_price) 
