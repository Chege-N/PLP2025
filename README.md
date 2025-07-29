Iris Dataset Analysis and Visualization

Overview
This project demonstrates data analysis and visualization using the Iris dataset. The script uses the Pandas library to load and analyze the dataset and the Matplotlib library (with Seaborn styling) to create visualizations. 
The analysis includes exploring the dataset, computing basic statistics, grouping data by species, and generating four types of plots to visualize patterns and relationships.DatasetThe Iris dataset is a classic dataset in machine learning, containing 150 samples of iris flowers with the following features:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Species (categorical: setosa, versicolor, virginica)

The dataset is sourced from a public URL: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv.

Requirements
To run the script, you need the following Python libraries:
pandas
matplotlib
seaborn (for enhanced plot styling)

Install the dependencies using pip:bash

pip install pandas matplotlib seaborn

Script Description
The script (.py) performs the following tasks:
Task 1: Load and Explore the DatasetLoads the Iris dataset using Pandas.
Displays the first 5 rows using .head().
Checks data types and missing values using .info() and .isnull().sum().
Notes that the dataset is clean (no missing values), with comments for handling missing values if needed.

Task 2: Basic Data Analysis
Computes basic statistics (mean, median, standard deviation, etc.) for numerical columns using .describe().
Groups the data by species and calculates the mean of numerical features.
Summarizes findings, such as setosa having smaller measurements and virginica having the largest.

Task 3: Data Visualization
Creates four visualizations in a 2x2 grid:
Line Chart: Plots petal length across sample indices for each species (pseudo-time series).
Bar Chart: Compares average sepal length across species.
Histogram: Shows the distribution of petal length.
Scatter Plot: Visualizes the relationship between sepal length and petal length, colored by species.

