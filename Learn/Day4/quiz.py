  
# Python code to demonstrate stdev() function
 
# importing Statistics module
import statistics
 
# creating a simple data - set
sample = [28, 35, 40, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 68, 70]
 
# Prints standard deviation
# xbar is set to default value of 1
print("Standard Deviation of sample is % s "
                % (statistics.stdev(sample)))