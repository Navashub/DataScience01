#Standard Deviation
import numpy as np 

#population Data
population_data = [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

#sample data
sample_data = [9.5, 9.8, 10.2, 10.5, 10.8, 11.1, 11.4, 11.7, 12.0, 12.3, 12.6, 12.9, 13.2, 13.5, 13.8]

#calculating population standard deviation
population_std_dev = np.std(population_data)
(population_std_dev)
(population_std_dev*population_std_dev)

#calculating sample standard deviation
sample_std_dev = np.std(sample_data, ddof=1)
print(sample_std_dev)
print(sample_std_dev*sample_std_dev)

#ddof - refers to data degrees of freedom where
#by default, in NumPy's std() function, ddof is set to 0
#which calculates the population standard deviation
#to calculate the sample STD you should set ddof to 1