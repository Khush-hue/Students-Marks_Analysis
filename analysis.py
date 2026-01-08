import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_excel("datamarks.ods", engine='odf')
# print(df.shape)
# df.to_csv("marks.csv", index=False)

# Load dataset
df = pd.read_csv("marks.csv")

print("Dataset Preview:\n", df.head())

# modify based on actual columns
subjects = ["Maths", "Science", "English", "History"]  

# Stats per subject
for subject in subjects:
    if subject in df.columns:
        print(f"{subject} stats:")
        print("Average:", df[subject].mean())
        print("Max:", df[subject].max())
        print("Min:", df[subject].min())
        print()

# Plot total marks per student
df["Total"] = df[subjects].sum(axis=1)

plt.bar(df["Name"], df["Total"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Student Marks Comparison")
plt.xticks(rotation=90)
plt.show()

# How are toppers performing
topper = df.loc[df["Total"].idxmax()]
print("Topper Details:")
print(topper)

#Result Determination
df["Result"] = df[subjects].apply(
    lambda x: "Fail" if (x < 35).any() else "Pass",
    axis=1
)
print(df[["Name", "Result"]])


# Marks Percentage Calculation
df["Percentage"] = (df["Total"] / (len(subjects) * 100)) * 100
print(df[["Name", "Percentage"]])
pass_count = df[df["Result"] == "Pass"].shape[0]
fail_count = df[df["Result"] == "Fail"].shape[0]


# Pass Fail Analysis
result_count = df["Result"].value_counts()
plt.bar(result_count.index, result_count.values)
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.title("Pass vs Fail Distribution")
plt.show()