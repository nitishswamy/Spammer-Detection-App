import pickle
from pathlib import Path

# Define the path to the pickle file
file_path = Path(r"C:\Users\prems\Desktop\Fakeuser_detection\Fakeuser_detection\spam_detection1.pkl")

# Load the model from the pickle file
with open(file_path, 'rb') as file:
    model = pickle.load(file)

# Print success message
print("Model loaded successfully!")

# Print the type of the loaded object
print(f"Type of the loaded object: {type(model)}")

# If the object is a scikit-learn model, print its details
if hasattr(model, '__class__'):
    print(f"\nModel class: {model.__class__.__name__}")

if hasattr(model, 'get_params'):
    print("\nModel parameters:")
    params = model.get_params()
    for key, value in params.items():
        print(f"{key}: {value}")

# Print other relevant attributes (if available)
if hasattr(model, 'coef_'):
    print("\nModel coefficients:")
    print(model.coef_)

if hasattr(model, 'intercept_'):
    print("\nModel intercept:")
    print(model.intercept_)

if hasattr(model, 'feature_importances_'):
    print("\nFeature importances:")
    print(model.feature_importances_)

# Print the model itself (optional)
print("\nLoaded model:")
print(model)