from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main Request Successful')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status Request Successful')
    return {"result": "OK - healthy"}, 200

@app.route("/metrics")
def metrics():
    app.logger.info('Metric Request Successful')
    return {
        "data": {
            "UserCount": 140, 
            "UserCountActive": 23
            }
        }, 200

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
