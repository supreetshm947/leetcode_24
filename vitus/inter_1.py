import pandas as pd

# Sample Data
data = {
    'school_id': ['sch_1', 'sch_2', 'sch_3', 'sch_4', 'sch_5', 'sch_11', 'sch_21', 'sch_6', 'sch_14', 'sch_8'],
    'state_code': ['!@sc_1', '))sc_2', '!@sc_2', 'sc_2)_', 'sc_3#@', 'sc4', '))sc_2', '!@sc_2', 'sc_2)_', 'sc_4#@'],
    'subjects': ['biology', 'biology', 'biology', 'biology', 'biology', 'biology', 'biology', 'biology', 'biology', 'biology maths english chemistry']
}

df = pd.DataFrame(data)

# Step 1: Clean `state_code`
# Step 1: Clean `state_code`
df['state_code'] = df['state_code'].str.replace(r'[^a-zA-Z0-9]', '', regex=True).str.strip()

# Step 2: Maintain the original order of state_code


# Step 3: Remove schools with fewer than 3 subjects
df = df[df['subjects'].apply(lambda x: len(x.split())) >= 3]

original_order = df['state_code'].drop_duplicates().tolist()

# Step 4: Explode `subjects` into separate rows
df_exploded = df.assign(subjects=df['subjects'].str.split()).explode('subjects')

# Step 5: Pivot table to count subjects per state
df_pivot = df_exploded.pivot_table(index='state_code', columns='subjects', aggfunc='size', fill_value=0)

# Step 6: Keep only required subjects
required_subjects = ['english', 'maths', 'physics', 'chemistry']
df_pivot = df_pivot.reindex(columns=required_subjects, fill_value=0)

# Step 7: Reorder state_code to match original order
df_pivot = df_pivot.reindex(original_order).reset_index()

# Step 8: Handle NaN values and convert counts to integer
df_pivot = df_pivot.fillna(0)  # Fill NaN values with 0
df_pivot[required_subjects] = df_pivot[required_subjects].astype(int)  # Convert to int

# Print final DataFrame
print(df_pivot)
