from flask import Flask, jsonify

# Initialize an instance of the Flask object
app = Flask(__name__)


# Use the route() decorator to tell Flask what URL should trigger our function
@app.route('/', methods=['GET'])
def home():

    return '<h1>Hello! This is the home page</h1>'


# Use the route() decorator to tell Flask what URL should trigger our function
@app.route('/api', methods=['GET'])
def api():

    return jsonify(result="ok", message="This is the API endpoint")


# This code only executes if it is ran directly (not imported)
if __name__ == '__main__':

    # Run the server
    app.run(host='0.0.0.0', debug=True)