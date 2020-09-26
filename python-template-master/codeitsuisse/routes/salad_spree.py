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

def count_cost(data):

    all_cost = []
    street_array = data["salad_prices_street_map"]

    for i in range(len(street_array)):
        number_of_salads = 0
        cost = 0
        consecutive_salad = 0
        for j in street_array[i]:
            if j == 'X':
                consecutive_salad = 0
            else:
                cost += int(j)
                number_of_salads += 1
                consecutive_salad += 1
                if number_of_salads == data["number_of_salads"] and consecutive_salad == data["number_of_salads"]:
                    all_cost.append(cost)
                    break

    if len(all_cost) > 0:
        return json.dumps({"result" : min(all_cost)})
    else:
        return json.dumps({"result" : 0})
        
# print(count_cost(data))


    
