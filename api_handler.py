from flask import Flask, jsonify
import api_handler #test

app = Flask(__name__) #test

@app.route('/api/get-data') #test
def get_data():
    api_data = api_handler.get_api_data("https://blackboard.vsu.edu/webapps/calendar/viewPersonal")

if __name__ == '__main__': #test
    app.run(debug=True)