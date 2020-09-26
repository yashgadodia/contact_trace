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

    return result

# data = {
#     "number_of_salads" : 3,
#     "salad_prices_street_map" : [["X", "X", "2"], ["2", "3", "X"], ["X", "3", "2"]]
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
        
        if len(min_cost) == 0:
            return 0

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


    

            


    



    
