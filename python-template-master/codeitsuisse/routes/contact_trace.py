import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluate1():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data;
    result = contact_trace(data)
    # logging.info("My result :{}".format(result))
    return jsonify(result);


# check diff between infected and origin
def contact_trace(data):

    infected_genome = data['infected']['genome'].split('-')
    origin_genome = data['origin']['genome'].split('-')

    infected_origin_name = data['infected']['name']

    diff_infected_origin = 0

    for i in range(0, len(infected_genome)):
        for j in range(0, 3):
            if infected_genome[i][j] != origin_genome[i][j]:
                if j == 0 and "*" not in infected_origin_name:
                    infected_origin_name += "*"

                diff_infected_origin += 1

    priority_cluster = []
    less_cluster = []

    # check diff between cluster and origin genome (x) and cluster and infected genome (y)
    for item in data['cluster']:

        cluster_elem_genome = item['genome'].split('-')
        infected_name = data['infected']['name']

        diff_elem_origin = 0
        diff_elem_infected = 0

        # diff b/w cluster and origin
        for i in range(0, len(cluster_elem_genome)):
            for j in range(0, 3):
                if cluster_elem_genome[i][j] != origin_genome[i][j]:
                    if j == 0 and "*" not in item["name"]:
                        item["name"] += "*"
                    diff_elem_origin += 1

        # diff b/w cluster and infected
        for i in range(0, len(cluster_elem_genome)):
            for j in range(0, 3):
                if cluster_elem_genome[i][j] != infected_genome[i][j]:
                    if j == 0 and "*" not in infected_name:
                        infected_name += "*"
                    diff_elem_infected += 1

        # diff b/w x+y and z
        if (diff_elem_infected + diff_elem_origin) <= diff_infected_origin and diff_infected_origin <= 4 and diff_elem_infected <= 2 and diff_elem_origin <= 2:
            if diff_elem_infected == 1 and diff_elem_origin == 1:
                priority_cluster.append(
                    [infected_name, item["name"], data["origin"]["name"]])
            elif diff_infected_origin > 2:
                less_cluster.append(
                    [infected_name, item["name"], data["origin"]["name"]])
            else:
                if "*" in item["name"]:
                    less_cluster.append(
                        [infected_name, item["name"][0:-1]])
                else:
                    less_cluster.append([infected_name, item["name"]])

    clusters = []

    if diff_infected_origin >= 2:
        if priority_cluster:
            for item in priority_cluster:
                string = " -> ".join(item)
                clusters.append(string)
        elif less_cluster:
            if diff_infected_origin == 2:
                clusters.append(
                    " -> ".join([infected_name, data["origin"]["name"]]))
            for item in less_cluster:
                string = " -> ".join(item)
                clusters.append(string)

    elif diff_infected_origin < 2:
        clusters.append(
            " -> ".join([infected_origin_name, data["origin"]["name"]]))
        if priority_cluster:
            for item in priority_cluster:
                string = " -> ".join(item)
                clusters.append(string)
        elif less_cluster:
            for item in less_cluster:
                string = " -> ".join(item)
                clusters.append(string)

    return clusters


# print(contact_trace(data))




