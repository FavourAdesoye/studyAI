from flask import Flask, jsonify
import api_handler  # Import the file containing get_api_data

app = Flask(__name__)

@app.route('/api/get-data')
def get_data():
    # Replace with your backend logic (call the Python function to fetch data)
    api_data = api_handler.get_api_data("https://blackboard.vsu.edu/webapps/calendar/viewPersonal")  # Use the imported function
    return jsonify(api_data)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production