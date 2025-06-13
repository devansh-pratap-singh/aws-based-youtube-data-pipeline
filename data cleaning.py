import pandas as pd

df = pd.read_csv("YouTube Trending Videos.csv")

# Step 1: Drop unnecessary columns
columns_to_drop = ["ratings_disabled", "comments_disabled", "snippet_assignable", "kind", "thumbnail_link", "etag", "id"]
df.drop(columns=columns_to_drop, inplace=True)

# Step 2: Rename columns to snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Step 3: Convert date fields
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce', format='%y.%d.%m')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Step 4: Handle missing values
df['description'].fillna('No description available', inplace=True)

# Step 6: Optional - Remove outliers (e.g., using quantiles)
numeric_cols = ['views', 'likes', 'dislikes', 'comment_count']
for col in numeric_cols:
    upper_limit = df[col].quantile(0.99)
    df = df[df[col] <= upper_limit]

# Get unique mappings between category_id and snippet_title
category_mapping = df[['category_id', 'snippet_title']].drop_duplicates().sort_values(by='category_id')

# Display the mapping
print(category_mapping)

# Clean and fix 'trending_date'
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m', errors='coerce')

# Drop rows where trending_date couldn't be parsed
df = df.dropna(subset=['trending_date'])

# Convert to standard date string format
df['trending_date'] = df['trending_date'].dt.date

# Save cleaned data
df.to_csv("cleaned_youtube_trending.csv", index=False)