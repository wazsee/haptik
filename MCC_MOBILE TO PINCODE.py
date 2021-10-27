# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:35:02 2021

@author: satishkumar.s
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:22:47 2021

@author: satishkumar.s
"""
# -*- coding: utf-8 -*
import pandas as pd
import flask
from flask import request

"""
MOBILE_NUMBER to pincode
Author: Srikar Kashyap Pulipaka
Date: 14 September 2021
Version: v1 with basic error handling

"""
app = flask.Flask(__name__)

data = pd.read_csv(r"C:\Users\satishkumar.s\Desktop\mccdata.csv", usecols=['MCC_MOBILE_NO','MCC_NAME','Pin Code','UNIT_CODE','REGION'])
data = data.set_index("MCC_MOBILE_NO")['Pin Code'].to_dict()
@app.route("/PinCode", methods=['GET'])
def get_PinCode():
    """Gets pincode from MCC_MOBILE_NO
    Returns:
        Data not found
    """
    try:
        MCC_MOBILE_NO = int(request.args.get("MCC_MOBILE_NO"))
    except ValueError as e:
        print("Please enter only integer")
        return "404"
    PinCode = data.get(MCC_MOBILE_NO, '404')
    return str(int(PinCode))


app.run(host='0.0.0.0')