from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('subham-ki-kismat-firebase-adminsdk-vsx2z-889917f6ec.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    person = request.form['person']
    date = request.form['date']
    distance = float(request.form['distance'])  # Convert to float if necessary
    emissions = float(request.form['emissions'])
    reward_points = int(request.form['reward_points'])
    adjusted_reward = int(request.form['adjusted_reward'])

    # Save data to Firebase
    data = {
        'person': person,
        'date': date,
        'distance': distance,
        'emissions': emissions,
        'reward_points': reward_points,
        'adjusted_reward': adjusted_reward
    }
    
    db.collection('emissions_data').add(data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
