import pandas as pd

# Load the dataset from CSV file
file_path = r'C:\Users\Splas\Downloads\archive\gym_members_exercise_tracking.csv'
df = pd.read_csv(file_path)


print(df.columns)


# Define the classification function
def classify_gym_member(data):
    # Extracting important data from the row
    Workout_Frequency = data['Workout_Frequency']
    Session_Duration = data['Session_Duration']
    calories_burned = data['Calories_Burned']
    workout_type = data['Workout_Type']
    max_bpm = data['Max_BPM']
    avg_bpm = data['Avg_BPM']
    experience_level = data['Experience_Level']
    
     # Print the values to debug
    print(f"Workout_Frequency: {'workout_frequency (days/week)'}, Session_Duration: {'session_duration (hours)'}, Calories_Burned: {calories_burned}, Max_BPM: {max_bpm}, Avg_BPM: {avg_bpm}, Experience_Level: {experience_level}")
    
    # Rule for Casual User
    if Workout_Frequency <= 3 and max_bpm <= 160 and calories_burned <= 900:
        if workout_type in ['Yoga', 'Cardio'] and experience_level <= 2:
            return 'Beginner'

    # Rule for Intermediate
    if Workout_Frequency >= 3 and Workout_Frequency <= 4 and 900 < calories_burned <= 1300:
        if 160 <= max_bpm <= 180:
            return 'Intermediate'
        if workout_type in ['Cardio', 'Strength'] and experience_level in [2, 3]:
            return 'Intermediate'
    
    # Rule for Advanced
    if Workout_Frequency >= 4 and calories_burned > 1300 and max_bpm >= 180:
        if workout_type in ['HIIT', 'Strength'] and experience_level == 3:
            return 'Advanced'

# Apply the classification function to each row of the dataframe
df['Engagement_Level'] = df.apply(classify_gym_member, axis=1)

# Display the result with debugging information
print(df[['Age', 'Gender', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM', 'Calories_Burned', 'Workout_Type', 'Experience_Level', 'Engagement_Level']])