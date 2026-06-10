import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data_analyst_jobs.csv")

# ==========================================
# TOP JOB TITLES
# ==========================================

top_jobs = df['Job Title'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_jobs.plot(kind='bar')

plt.title("Top 10 Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_job_titles.png")

plt.show()

# ==========================================
# TOP LOCATIONS
# ==========================================

top_locations = df['Location'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_locations.plot(kind='bar')

plt.title("Top Hiring Locations")
plt.xlabel("Location")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_locations.png")

plt.show()

print("✅ Charts Created Successfully!")