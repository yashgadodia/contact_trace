# data = {
#     "number_of_salads" : 2,
#     "salad_prices_street_map" : [["2", "3", "X", "2"], ["4", "X", "X", "4"], ["3", "2", "X", "X"], ["X", "X", "X", "5"]]
# }

import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = count_cost(data)

    return jsonify(result)

# data ={
#     'number_of_salads': 3, 
#     'salad_prices_street_map': [['X', '5', '9'], ['19', '9', '2'], ['4', '15', '4'], ['X', 'X', 'X'], ['3', 'X', 'X'], ['7', 'X', '7'], ['15', '15', '3'], ['8', '20', '7'], ['18', '19', '2'], ['15', '14', '4'], ['X', '15', 'X'], ['13', 'X', '7'], ['X', '5', '10']]
# } 
def count_cost(data):

    street_array = data["salad_prices_street_map"]
    salads = data["number_of_salads"]

    all_cost = []

    for arr in street_array:
        min_cost = []
        for j in range(len(arr)):
            cost = 0
            salad_count = 0
            combi = arr[j:j+salads]
            for elem in combi:
                if elem.isnumeric() and salad_count != salads:
                    cost += int(elem)
                    salad_count += 1
                if salad_count == salads:
                    min_cost.append(cost)
        try:
            all_cost.append(min(min_cost))
        except ValueError:
            pass
    if len(all_cost) == 0:
        return {"result": 0}

    return {"result": min(all_cost)}
            
        # store_cost = []
        # store = street_array[arr]
        # print(store[arr:salads])
        # for j in street_array[i]:

    # all_cost = []

    # for i in range(len(street_array)):
    #     number_of_salads = 0
    #     cost = 0
    #     consecutive_salad = 0
    #     min_store_cost = []
    #     for j in street_array[i]:
    #         if j == 'X':
    #             consecutive_salad = 0
    #         else:
    #             cost += int(j)
    #             number_of_salads += 1
    #             consecutive_salad += 1
    #             if number_of_salads == data["number_of_salads"] and consecutive_salad == data["number_of_salads"]:
    #                 all_cost.append(cost)
    #                 break

    # if len(all_cost) > 0:
    #     return min(all_cost)
    # else:
    #     return 0
    

# print(count_cost(data))


    
