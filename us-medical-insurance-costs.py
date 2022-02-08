#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# Aims of the project
# 1. Find out the average age of the patients in the dataset.
# 2. Analyze where a majority of the individuals are from.
# 3. Look at the different costs between smokers vs. non-smokers.
# 4. Figure out what the average age is for someone who has at least one child in this dataset.

# In[14]:


#Import in the insurance.csv data file
import csv

insurance_dict = {}
with open('insurance.csv',newline='') as insurance_csv:
    #headers = insurance_csv.readline()
    insurance_lines = csv.DictReader(insurance_csv)
    patient = 1
    for line in insurance_lines:
        insurance_dict[patient] = line
        patient +=1
#print(headers)
print(insurance_dict[1])
#insurance_dict is the dataset and the file is now closed so now corruption of the data could occur


# Find the average age of the patinets in the dataset

# In[32]:


#Find average age of patients in the dataset
def average_age(dict_set):
    dict_values = dict_set.values()
    age = 0
    num_of_patients = 0
    for patient in dict_values:
        patient_age = patient["age"]
        age += int(patient_age)
        num_of_patients += 1
    return age/num_of_patients


dataset_average_ages = average_age(insurance_dict)
print(dataset_average_ages)
print("The average age of the patients in the dataset is " + str(round(dataset_average_ages, 1)) + " years old.")


# Identify the location of the patients and where the most come from

# In[37]:


#produce an array of the totals for each location and identify the largest area

#sub function to calculate the area with the largest number of patients 
def largest_area(locations):
    largest = ""
    count = 0
    for area in locations:
        if locations[area] > count:
            count = locations[area]
            largest = area
    return largest, count

def location(insurance_dictionary):
    patient_values = insurance_dictionary.values()
    areas = []
    for patient in patient_values:
        current_area = patient["region"]
        areas.append(current_area)
    # create dictionary of areas to store the number of patients in each area
    areas_with_count = {}
    for area in areas:
        if areas_with_count.get(area) == None:
            count = areas.count(area)
            areas_with_count[area] = count
    #identify largest area
    biggest_location, num_of_patients = largest_area(areas_with_count)
    return areas_with_count, biggest_location, num_of_patients

location_with_count, biggest_location, location_number = location(insurance_dict)
print(location_with_count)
print("The region with the most patients is " + biggest_location + " with a total of " + str(location_number) + " patients" )


# Difference in cost between smokers and non-smokers

# In[44]:


#function to calculate the difference in average cost between smokers and non smokers

def cost_of_smoking(insurance):
    insurance_values = insurance.values()
    #total costs for smokers and non smokers
    smokers_total = 0
    number_of_smokers = 0
    non_smokers_total = 0
    number_of_non_smokers = 0
    for patient in insurance_values:
        current_cost = float(patient["charges"])
        if patient["smoker"] == 'yes':
            smokers_total += current_cost
            number_of_smokers += 1
        elif patient["smoker"] == 'no':
            non_smokers_total += current_cost
            number_of_non_smokers += 1
    average_cost_smokers = smokers_total/number_of_smokers
    print(average_cost_smokers)
    average_cost_non_smokers = non_smokers_total/number_of_non_smokers
    print(average_cost_non_smokers)
    difference_in_cost = average_cost_smokers - average_cost_non_smokers
    return round(difference_in_cost,2)

difference = cost_of_smoking(insurance_dict)
print("The cost of smoking is on average $" + str(difference) + " extra in insurance cost.")


# Average age of parents (someone with at least one child)

# In[46]:


#Calculate the average age for a parent
def parental_age(insurance):
    insurance_values = insurance.values()
    total_age = 0
    number_of_parents = 0
    for patient in insurance_values:
        current_age = int(patient["age"])
        children = int(patient["children"])
        if children > 0:
            total_age += current_age
            number_of_parents +=1
    average_age = total_age/number_of_parents
    return round(average_age, 1)

average_parental_age = parental_age(insurance_dict)
print("The average age of parents in the dataset is " + str(average_parental_age))
        

