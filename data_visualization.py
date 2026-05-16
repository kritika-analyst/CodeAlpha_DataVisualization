# Project : Data Visualization
# Author : Kritika
# Task 3 - Data Visualization of Netflix Movies and TV Shows

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")  # makes graphs cleaner 

df= pd.read_csv("netflix_titles.csv")  # reading this file

print(df.head())  # shows first 5 rows

# Creates a count plot for the 'type' colummn ,it counts how many movies and tv shows are present
sns.countplot(x= "type", data=df)

plt.title("Movies vs TV Shows on Netflix")      # adds title on the graph
plt.savefig("movies_vs_tvshows.png")   # Save graph image
plt.show()         # Display 1st graph


# Top 10 countries 
top_countries= df["country"].value_counts().head(10)  # counts top 10 values from the 'country' column

top_countries.plot(kind= "bar")   # creates a bar chart
plt.title("Top 10 Countries on Netflix")
plt.xlabel("country")           # adds x-axis label
plt.ylabel("count")             # adds y-axis label

plt.savefig("Top_10_countries.png")
plt.show()        # displays 2nd graph


# Content Ratings
sns.countplot(y= "rating", data=df)  # counts ratings and creates chart

plt.title("Content Ratings on Netflix")
plt.savefig("ratings_distribution.png")
plt.show()        # displays 3rd graph


# Release Year
release_year= df["release_year"].value_counts().head(15)   # counts top release years

release_year.plot(kind= "line")    # creates a line graph

plt.title("Release Year Trend")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.savefig("release_year_trend.png")
plt.show()       # displays 4th graph


print("Data Visualization Project 3 Completed Successfully")