import pandas as pd

# File path to the dataset
file_path = r'C:\Users\Splas\OneDrive\Documents\GitHub\ASSESSMENT-1--Rule-basedAIAlgorithm\Code\gym_members_exercise_tracking.csv'

# Load dataset
df = pd.read_csv(file_path)


# Finds total number of males and females, finds most common workout type for each gender
if 'Gender' in df.columns:  # if gender is found in column continue
    gender_counts = df['Gender'].value_counts()  # count number of times male /female in gender column
    gender_percentages = df['Gender'].value_counts(normalize=True) * 100  # using the gender count above calculate the percentage
    print("Members' Gender Distribution:")  # prints details about info
    for gender in gender_counts.index:  # loop for gender and its count.
        print(f"{gender}: {gender_counts[gender]} members ({gender_percentages[gender]:.2f}%)")  # print the gender, its count and a percentage. .2f

    gender_groups = df.groupby('Gender')['Workout_Type'].agg(lambda x: x.mode()[0])  # calculates which combination of gender and workout_type were the most common
    gender_group_counts = df.groupby('Gender')['Workout_Type'].size()
    print("\nMost Common Workouts by Gender:")  # prints details about section.
    for gender, workout in gender_groups.items():
        members_doing_workout = df[(df['Gender'] == gender) & (df['Workout_Type'] == workout)]
        print(f"{gender}: {workout} (Total: {members_doing_workout.shape[0]} members)")  # Print gender, count, and percentage


# function for categorising ages
def categorize_age(age):
    if age <= 18:
        return '0-18'
    elif 19 <= age <= 35:
        return '19-35'
    elif 36 <= age <= 50:
        return '36-50'
    else:
        return '51+'
# finds number of members in each age range, and the most popular workout types for each age group
if 'Age' and 'Workout_Type' in df.columns:
    # applies the function for categorising ages
    df['Age_Category'] = df['Age'].apply(categorize_age)
    age_counts = df['Age_Category'].value_counts()  # calculates the number of members in the age category
    age_percentages = df['Age_Category'].value_counts(normalize=True) * 100  # this then calculates the percentage
    print("\nAge Range Distribution:")  # prints info about the section
    for age_range in age_counts.index:  # prints the age range info
        print(f"{age_range}: {age_counts[age_range]} members ({age_percentages[age_range]:.2f}%)")

    age_groups = df.groupby('Age_Category')['Workout_Type'].agg(lambda x: x.mode()[0])  # finds the most common workout for each age group
    print("\nMost Common Workouts by Age Range:")  # prints info about section
    for age_range, workout in age_groups.items():  # prints the most common workout for each age group,
        print(f"{age_range}: {workout}")

# finds and shows all the workout types and the amount of members that do that workout type
if 'Workout_Type' in df.columns:
    workout_counts = df['Workout_Type'].value_counts()  # Count the occurrences of each workout type in the 'Workout_Type' column
    workout_percentages = df['Workout_Type'].value_counts(normalize=True) * 100  # calculate the percentages using the value above.
    print("\nWorkout Type Distribution:")  # prints info about section
    for workout_type in workout_counts.index:  # prints the total members that do that workout type. Also prints percentage.
        print(f"{workout_type}: {workout_counts[workout_type]} members ({workout_percentages[workout_type]:.2f}%)")


# function for categorising BMI levels
def classify_bmi(bmi):  # BMI levels are from the NHS website
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'
    
# calculates BMI levels and what category members are in. Then shows total number of members in each category BMI, along with percentages.
# also calculates the most popular workout types for each BMI category
if 'BMI' in df.columns:
    df['BMI_Level'] = df['BMI'].apply(classify_bmi)  # applies BMI classification for each member
    bmi_counts = df['BMI_Level'].value_counts()  # counts the amount of members in each category
    bmi_percentages = df['BMI_Level'].value_counts(normalize=True) * 100  # calculates the percentage
    print("\nBMI Level Distribution:")  # prints info about section
    for bmi_level in bmi_counts.index:  # prints the amount of members in each category
        print(f"{bmi_level}: {bmi_counts[bmi_level]} members ({bmi_percentages[bmi_level]:.2f}%)")
    
    bmi_groups = df.groupby('BMI_Level')['Workout_Type'].agg(lambda x: x.mode()[0])  # calculates the most popular workout for each category
    print("\nMost Common Workouts by BMI Level:")  # prints info about section
    for bmi_level, workout in bmi_groups.items():  # prints the most popular workout type for each category
        print(f"{bmi_level}: {workout}")
