import pickle
from pathlib import Path

# Define the path to the pickle file
file_path = Path(r"C:\Users\prems\Desktop\Fakeuser_detection\Fakeuser_detection\spam_detection1.pkl")

# Load the model from the pickle file
with open(file_path, 'rb') as file:
    model = pickle.load(file)

# Now `model` contains the loaded object (e.g., your trained model)
print("Model loaded successfully!")