import json
import requests
import os

from loguru import logger
from flask import Flask, request

app = Flask(__name__)


@app.route("/route", methods=["POST"])
def reroute():
    # Decode the request body
    body = request.data.decode("utf-8")

    # Convert to dict
    body = json.loads(body)
    logger.debug(f"Body: {body}")

    # Parse body for alert name on an alarm alerting state
    state = body.get("state")
    if state == "alerting":
        
        # Set the URL depending on the dag config
        url = f"https://api.github.com/repos/NuwanCW/ML-monitoring-kubernetes/dispatches"
        Bearer=os.getenv('Bearer')
        data={"event_type": "from grafana"}
        hed = {'authorization': 'Bearer '+ Bearer}
        try:
            response = requests.post(url,json=data,headers=hed)
            logger.info(response.status_code)    
            return response.status_code
        except Exception as e:
            logger.error(f"Could not trigger Airflow DAG due to {e}")

    return "Training time!"


@app.route("/health", methods=["GET"])
def index():
    return "Alive!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)
