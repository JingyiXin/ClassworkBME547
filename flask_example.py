from flask import Flask, request
from blood_calculator import hdl_analysis

app = Flask(__name__)


# "/" means no route needed really since we're just checking if it's on
@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
def info():
    my_output = "This server is for BME 547"
    return my_output


@app.route("/hdl", methods=["POST"])
def hdl_analysis():
    """
    Input should look like {"hdl": 50, "patient_id": 200} 
    
    :return:
    """
    in_data = request.get_json()
    hdl_value = in_data["hdl"]
    answer = hdl.analysis(hdl_value)
    return answer


if __name__ == '__main__':
    app.run()

"""
www.google.com/maps
"""