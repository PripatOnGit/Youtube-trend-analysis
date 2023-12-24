import pandas as pd

# Replace 'your_file.json' with the actual file path
file_path = 'D:\Priyanka\Data Engineering\Youtube-trend-analysis\source_data\IN_category_id.json'

# Read JSON file into a DataFrame
df = pd.read_json(file_path)

# Display the DataFrame
print(df)