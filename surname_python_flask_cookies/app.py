from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/setcookies', methods=['POST'])
def set_cookies():

    data = request.json  

    response = make_response(jsonify({"message": "Cookies have been set!"}))

    for key, value in data.items():
        response.set_cookie(key, value)  

    return response

@app.route('/getcookies', methods=['GET'])
def get_cookies():

    cookies = request.cookies 

    return jsonify(cookies)  

if __name__ == '__main__':
    app.run(debug=True)
