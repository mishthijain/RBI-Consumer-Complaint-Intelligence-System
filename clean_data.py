import pandas as pd

# Load dataset
df = pd.read_csv("data/complaints.csv", low_memory=False)

# Basic Information
print("="*50)
print("DATASET SHAPE")
print("="*50)
print(df.shape)

print()

print("="*50)
print("COLUMN NAMES")
print("="*50)
print(df.columns)

print()

print("="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())