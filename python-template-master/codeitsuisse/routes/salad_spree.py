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

# data = {
#     "number_of_salads" : 3,
#     "salad_prices_street_map" : [['6', '9', '20', 'X', '20', '11', '2', '19', '5', '3', '7', 'X', '6', '18', '6', '7', '18', 'X', '4', '1', 'X', '2', '20', '16', '14', '15', 'X', '4', '4', '7', 'X', '17', 'X', '20', '20', '19', '4', 'X', '18', '20', '14', '5', '10', 'X', '2', '6', '2', '11', '5', '4', '4', '10', 'X', '11', '1', '9', '8', '12', '14', '3', '9', '5', '16', 'X', '12', '13', '6', '17', '5', '17', '20', 'X', 'X', '8', 'X', '11', '9', '4', 'X', 'X', 'X', '3', 'X', '18', '15', '19', '17', 'X', 'X', '3', '10', 'X', '10', '7', 'X', '7'],['16', '18', '13', '15', '11', '10', '17', '13', 'X', '7', '6', '9', '10', '15', '15', 'X', '7', '3', '2', '18', '6', 'X', '14', '2', '3', '19', '12', '6', '1', 'X', 'X', '8', '1', '3', '18', '8', 'X', '13', 'X', '1', '11', '20', '18', '17', '5', '17', '2', 'X', '18', '17', '4', '18', 'X', '11', '8', 'X', '12', 'X', '18', '2', '18', '20', '17', '8', '4', '7', 'X', '8', '15', '10', 'X', '15', '11', 'X', '10', 'X', '14', '12', '19', '2', '15', 'X', '16', '18', 'X', '19', '6', 'X', 'X', '7', '20', '7', 'X', '7', '15', '12']]
# }

def count_cost(data):

    street_array = data["salad_prices_street_map"]
    salads = data["number_of_salads"]
    min_cost = []
    all_cost = []

    for arr in street_array:
        for j in range(len(arr)):
            combi = arr[j:j+salads]
            if 'X' not in combi:
                combi = map(int, combi)
                min_cost.append(sum(combi))
        all_cost.append(min(min_cost))

    return min(all_cost)
            
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


    



    
