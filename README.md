# Iris Flower Classification: Exploratory Data Analysis and Visualization

## Overview

The goal of this analysis is to explore the characteristics of different Iris species based on their sepal and petal measurements and to visualize the relationships between these features.

## Data Collection and Description

The Iris dataset was obtained from the UCI Machine Learning Repository
Brief description of the dataset's features (columns):
    - Sepal Length (cm)
    - Sepal Width (cm)
    - Petal Length (cm)
    - Petal Width (cm)
    - Species (Iris-setosa, Iris-versicolor, Iris-virginica)
    - number of instances (rows) in the dataset = 150

## Data Cleaning and Pre-processing: 

    - Removed the 'Id' column.
    - Checked for and handled (if any) missing values. In our case, there were none.
    - Checked for and handled (if any) duplicate rows.

## Exploratory Data Analysis (EDA) and Visualization:

**Summary Statistics:**

Formatted table of summary statistics (mean, median, standard deviation, etc.) for each numerical feature, broken down by species.

**Descriptive Statistics**
 
![image7](https://github.com/user-attachments/assets/dc62730c-6a9c-44de-bb20-31742061024e)

To understand the characteristics of each Iris species, I created several visualizations:

**Histograms:** 
   
![image1](https://github.com/user-attachments/assets/5e49a38d-7483-48f5-99bf-390aeb79b590)

![image2](https://github.com/user-attachments/assets/03384e59-73f5-4a89-8859-7a9ba4b99bb0)

**Scatter Plot of Petal Length vs. Petal Width:**

This plot clearly shows three distinct clusters, indicating a strong relationship between petal dimensions and species. *Iris-setosa* has significantly smaller petals compared to the other two species.

![image3](https://github.com/user-attachments/assets/5b35e7eb-2bec-4d7a-9fbc-90fe06f43683)

![image4](https://github.com/user-attachments/assets/4b45ee59-3ab1-4fbb-ac06-f4839a042fcd)

**Box Plots of Sepal Length by Species:**

![image5](https://github.com/user-attachments/assets/cf6112d7-29a6-46a8-9d77-992bfef59af2)

The box plots reveal differences in sepal length distributions across species. *Iris-setosa* tends to have shorter sepals, while *Iris-virginica* has the longest.

![image6](https://github.com/user-attachments/assets/d51a8179-a0ad-402f-8748-841028d5b624)


**Key Insight:** 

Petal dimensions are highly discriminative for classifying Iris species. Sepal dimensions also provide some discriminatory power, though to a lesser extent.

## **Tools and Technologies:**

- Python
- Pandas
- Matplotlib
- VS Code 

## Conclusion
In conclusion
