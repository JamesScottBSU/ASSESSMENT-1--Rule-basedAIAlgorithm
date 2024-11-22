import pandas as pd

# File path to the dataset
file_path = r'C:\Users\Splas\OneDrive\Documents\GitHub\ASSESSMENT-1--Rule-basedAIAlgorithm\Code\gym_members_exercise_tracking.csv'

# Load dataset
df = pd.read_csv(file_path)

# Function for classifying age ranges
def categorise_age(age):
    if age <= 18:
        return '0-18'
    elif 19 <= age <= 35:
        return '19-35'
    elif 36 <= age <= 50:
        return '36-50'
    else:
        return '51+'

# Function for BMI categorisation
def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

# Applies the functions above
df['Age_Category'] = df['Age'].apply(categorise_age)
df['BMI_Level'] = df['BMI'].apply(classify_bmi)

# Function to find most common workout by categories
def most_common_workout(df, goal_category, goal_value):
    # Find the most common workout for the specific category, e.g., age or gender
    category_df = df[df[goal_category] == goal_value]
    
    # Find the most common workout and total number of members in the category
    most_common_workout = category_df['Workout_Type'].mode()[0]
    member_count = category_df.shape[0]
    
    return most_common_workout, member_count

genders = ['Male', 'Female']  # Lists genders
age_ranges = ['0-18', '19-35', '36-50', '51+']  # Lists age ranges
bmi_levels = ['Underweight', 'Normal', 'Overweight', 'Obese']  # Lists BMI categories

# Find most common workout for gender and the number of members that are male/female
for gender in genders:
    workout, count = most_common_workout(df, 'Gender', gender)  # Uses function to find most common workout and member count 
    if workout:  # If there was an output
        print(f"Most common workout for {gender} is: {workout}")  # Print the popular workout for each gender
        print(f"Total number of {gender} members: {count}\n")  # Print the number of members of that gender

for age_range in age_ranges:
    workout, count = most_common_workout(df, 'Age_Category', age_range)  # Uses the function to find the most common workout of the age range and number of members in the age group
    if workout:
        print(f"The most common workout for ages {age_range} is: {workout}")  # Prints the most common workout
        print(f"Total number of members in {age_range} age group: {count}\n")  # Prints the number of members in that age range

for bmi_level in bmi_levels:
    workout, count = most_common_workout(df, 'BMI_Level', bmi_level)  # Finds most common workout for BMI and number of members in that BMI category
    if workout:
        print(f"Most common workout for {bmi_level} is: {workout}")  # Prints most common workout
        print(f"Total number of members in the {bmi_level} category: {count}\n")  # Prints the number of members in that BMI category


def workout_type_counts(df):
    workout_counts = df['Workout_Type'].value_counts()  # Count the occurrences of each workout type
    return workout_counts

workout_counts = workout_type_counts(df)
print("Total Members for Each Workout Type:\n")
for workout_type, count in workout_counts.items():
    print(f"{workout_type}: {count} members")