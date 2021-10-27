# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:21:20 2021

@author: satishkumar.s
"""


import pandas as pd
import flask
from flask import request

"""
Mobilenumber to FIRSTNAME
Author: Srikar Kashyap Pulipaka
Date: 14 September 2021
Version: v1 with basic error handling

"""
app = flask.Flask(__name__)

data = pd.read_csv(r"C:\Users\satishkumar.s\Desktop\mccdata.csv", usecols=['MCC_MOBILE_NO','MCC_NAME','Pin Code','UNIT_CODE','REGION'])
data = data.set_index("MCC_MOBILE_NO").MCC_NAME.to_dict()


#####################################################################
@app.route("/MCC_NAME", methods=['GET'])
def get_MCC_NAME():
    """Gets MCC_NAME name from MCC_MOBILE_NO
    Returns:
        404 Not Found
    """
    try:
        MCC_MOBILE_NO = int(request.args.get("MCC_MOBILE_NO"))
    except ValueError as e:
        print("Please enter only integer")
        return "404"
    MCC_NAME = data.get(MCC_MOBILE_NO, '404')
    return MCC_NAME


app.run(host='0.0.0.0')
