from flask import Flask, request, jsonify, abort
from google.cloud import pubsub_v1
import json

app = Flask(__name__)

@app.route("/bubble-sort", methods=['POST'])
def bubble_sort():
    data = request.get_json()
    lista = data['lista']
    algoritmo = data['algoritmo']
    # print('ojo', lista, algoritmo)
    if lista and algoritmo:
        publisher = pubsub_v1.PublisherClient()
        project_id = "top-creek-395501"
        topic_id = "new-list"
        topic_path = publisher.topic_path(project_id, topic_id)
        data_published = json.dumps(data ).encode("utf-8")
        print(topic_path)
        future = publisher.publish(topic_path, data_published)
        print(f"Published messages to {topic_path}.")
        print('future', future.result())
        return jsonify({"mensaje": "Datos recibidos correctamente."}), 200
    else:
        return jsonify({"mensaje": "Datos recibidos incorrectos."}), 400

if __name__ == '__main__':
    app.run(debug=True)

# pip freeze > requirements.txt

# curl -X POST -H "Content-Type: application/json" -d '{
#   "lista": [3, 4, 1, 22],
#   "algoritmo": "bubble"
# }' http://172.17.0.3:5000/bubble-sort

# gcloud pubsub topics create new-list
# gcloud pubsub subscriptions create new-list-sub --topic new-list

# docker build --tag python-docker .
# docker run python-docker:latest