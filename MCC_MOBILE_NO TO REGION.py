# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:12:31 2021

@author: satishkumar.s
"""
import pandas as pd
import flask
from flask import request

"""
MOBILE_NUMBER to REGION
Author: Srikar Kashyap Pulipaka
Date: 14 September 2021
Version: v1 with basic error handling

"""
app = flask.Flask(__name__)

data = pd.read_csv(r"C:\Users\satishkumar.s\Desktop\mccdata.csv", usecols=['MCC_MOBILE_NO','MCC_NAME','Pin Code','UNIT_CODE','REGION'])
data = data.set_index("MCC_MOBILE_NO").REGION.to_dict()
@app.route("/REGION", methods=['GET'])
def get_REGION():
    """Gets REGION from MCC_MOBILE_NO
    Returns:
        404
    """
    try:
        MCC_MOBILE_NO = int(request.args.get("MCC_MOBILE_NO"))
    except ValueError as e:
        print("Please enter only integer")
        return "404"
    REGION = data.get(MCC_MOBILE_NO, '404')
    return REGION


app.run(host='0.0.0.0')