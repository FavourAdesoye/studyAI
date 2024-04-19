import requests

def get_api_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get-data')
def get_data():
    # Replace with your actual API URL and parameters if needed
    api_url = "https://blackboard.vsu.edu/webapps/calendar/viewPersonal"
    api_data = get_api_data(api_url)

    if isinstance(api_data, dict):
        # Process the API data here (e.g., store in a database)
        return jsonify(api_data)
    else:
        return jsonify({"error": api_data})  # Return error as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
