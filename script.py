# Import libraries, pandas for data manipulation, matplotlib for visualization
import pandas as pd
import matplotlib.pyplot as plt

# Importing databases
df_workout = pd.read_csv("workout.csv")
df_three_keywords = pd.read_csv("three_keywords.csv")
df_workout_geo = pd.read_csv("workout_geo.csv")
df_keywords_geo = pd.read_csv("three_keywords_geo.csv")

# Exploring dataframes
# display(df_workout.head()) # Commented out for script, uncomment if running interactively
# display(df_three_keywords.head()) # Commented out for script
# display(df_workout_geo.head()) # Commented out for script
# display(df_keywords_geo.head()) # Commented out for script


# Analyzing worldwide workout interest trend
plt.figure(figsize=(14,6))
x = df_workout["month"]
y = df_workout["workout_worldwide"]
plt.plot(x,y)
plt.xticks(rotation = 90)
plt.title("Worldwide Workout Interest")
plt.xlabel("Month")
plt.ylabel("Interest")
plt.show()

year_str = "2020"
print("Peak year was ", year_str)


# Analyzing types of workout interest trends
plt.figure(figsize=(12,6))
plt.plot(df_three_keywords["month"], df_three_keywords["home_workout_worldwide"], label= "Home Workout")
plt.plot(df_three_keywords["month"], df_three_keywords["gym_workout_worldwide"], label = "Gym Workout")
plt.plot(df_three_keywords["month"], df_three_keywords["home_gym_worldwide"], label= "Home Gym")
plt.xticks(rotation=90)
plt.title("Types of Workout Interest")
plt.xlabel("Month")
plt.ylabel("Interest")
plt.legend()
plt.show()

peak_covid = "Home Workout"
current = "Gym Workout"

print("During covid, peak interest worldwide was on ", peak_covid, ", and currently on", current, ".")


# Comparing USA, AUS and JAP interest

countries_filt = df_workout_geo["country"].isin(["United States","Australia","Japan"])

# Filter the DataFrame and set the 'country' column as the index
df_filtered = df_workout_geo[countries_filt].set_index("country")


df_filtered.plot(kind="bar")
plt.xticks(rotation=30)
plt.title("Workout Interest by Country")
plt.xlabel("Country")
plt.ylabel("Interest")
plt.show()

top_country = "United States"

# Comparing Malaysia vs Philippines home workout interest
# Indexing country column
# df_keywords_geo.set_index("Country") # Commented out as set_index does not modify in-place by default


# Selecting COUNTRIES with .loc
selected_countries = df_keywords_geo.loc[["Malaysia","Philippines"], "home_workout_2018_2023"]
# display(selected_countries) # Commented out for script


# Comparing values
malaysia_value = selected_countries["Malaysia"]
philippines_value = selected_countries["Philippines"]

if malaysia_value > philippines_value:
    print("\nMalaysia has highest home workout interest.")
elif malaysia_value < philippines_value:
    print("\nPhilippines has highest home workout interest.")
else:
    print("\nHome workout interest is the same in Malaysia and the Philippines.")

# display(df_keywords_geo) # Commented out for script