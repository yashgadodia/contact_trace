# data = {
#     "number_of_salads" : 2,
#     "salad_prices_street_map" : [["2", "3", "X", "2"], ["4", "X", "X", "4"], ["3", "2", "X", "X"], ["X", "X", "X", "5"]]
# }

import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad_spree', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    street_array = data;

    result = count_cost(street_array)

    return result;


            


    



    
