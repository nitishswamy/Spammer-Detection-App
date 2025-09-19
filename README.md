# Spammer Detection and Fake User Identification System

This project is a tool designed to spot spammers and fake accounts on online platforms. It uses a machine learning approach to examine user profile details and determine if an account is real or suspicious, making digital spaces safer and more reliable.

### Features
1. Employs Logistic Regression to classify accounts accurately
2. Offers a Flask-powered web app for simple user interaction
3. Includes a form to input user data effortlessly
4. Provides immediate prediction outcomes

### Technologies Used
Python: Core programming language
Flask: Web framework for the interface
scikit-learn: Machine learning library
pandas: Data processing tool
HTML/CSS: Frontend design

### Installation
Set up the project on your machine with these steps:

#### Clone the repository:
  git clone https://github.com/nitishswamy/Spammer-Detection-App.git

#### Move into the project folder:
  cd your-repo-name

#### Install required packages:
  pip install -r requirements.txt

Note: Ensure Python is installed on your system.

Important: The pre-trained model is included as spam_detection.pkl. No additional training is needed.

### Usage
##### Run the application with these steps:

1. Launch the Flask server:
  python app.py

2. Open your browser and visit http://127.0.0.1:5000/.
3. Enter user profile details in the form and submit to see the prediction.
4. Check the "About" page for more project details.

#### Contributing
We welcome contributions! Feel free to submit pull requests or raise issues for suggestions or enhancements.

#### License
This project is licensed under the MIT License. See the LICENSE file for details.
