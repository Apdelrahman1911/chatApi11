from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Getting IP address of the visitor
    ip_address = request.remote_addr
    return f'Your IP address is: {ip_address}'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
