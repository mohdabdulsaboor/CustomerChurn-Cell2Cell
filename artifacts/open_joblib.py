import joblib
import os

# Set working directory
os.chdir(r"C:\Users\dell\Desktop\Cell2Cell_Project")

# Load the preprocessor
preprocessor = joblib.load("artifacts/preprocessor.joblib")

# Show summary
print(preprocessor)
