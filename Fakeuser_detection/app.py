from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the Logistic Regression model from the pickle file
with open('spam_detection.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract user inputs from the form
            profile_pic = float(request.form['ProfilePic'])
            username_nums_length = float(request.form['UsernameNumsLength'])
            fullname_words = float(request.form['FullnameWords'])
            fullname_nums_length = float(request.form['FullnameNumsLength'])
            name_equals_username = float(request.form['NameEqualsUsername'])
            description_length = float(request.form['DescriptionLength'])
            external_url = float(request.form['ExternalURL'])
            private = float(request.form['Private'])
            posts = float(request.form['Posts'])
            followers = float(request.form['Followers'])
            follows = float(request.form['Follows'])

            # Predict the ID status
            features = [[profile_pic, username_nums_length, fullname_words, fullname_nums_length,
                         name_equals_username, description_length, external_url, private,
                         posts, followers, follows]]
            pred = model.predict(features)
            result = 'Genuine ID' if pred == 1 else 'Fake ID'
        except ValueError:
            result = 'Invalid input. Please make sure all inputs are numbers.'
        
        return render_template('index.html', result=result)

    return render_template('index.html', result='')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
