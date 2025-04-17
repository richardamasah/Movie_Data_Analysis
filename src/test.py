#testing my functions
deleted columns = drop_columns(data)

# Convert release_date to datetime and extract year
df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year

yearly_trends = df.groupby('release_year')[['revenue_musd', 'budget_musd']].mean().dropna()

plt.figure(figsize=(12, 6))
yearly_trends.plot(kind='line', marker='o')
plt.title('Yearly Trends: Avg Revenue & Budget')
plt.xlabel('Release Year')
plt.ylabel('Million USD')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='popularity', y='vote_average', alpha=0.6)
plt.title('Popularity vs Rating')
plt.xlabel('Popularity')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show()

#revenue vs budget
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='budget_musd', y='revenue_musd', hue='original_language', alpha=0.7)
plt.title('Revenue vs Budget')
plt.xlabel('Budget (Million USD)')
plt.ylabel('Revenue (Million USD)')
plt.legend(title='Language', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



# roi chart
df['roi'] = pd.to_numeric(df['roi'], errors='coerce')

# Step 2: Extract the main genre (first one before "|")
df['main_genre'] = df['genres'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else None)

# Step 3: Drop missing values for clean plot
df_roi = df.dropna(subset=['roi', 'main_genre'])

# Step 4: Plot ROI distribution by main genre
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_roi, x='main_genre', y='roi')
plt.xticks(rotation=45)
plt.title('ROI Distribution by Genre')
plt.tight_layout()
plt.show()





