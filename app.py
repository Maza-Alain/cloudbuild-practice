from flask import Flask, request, jsonify, abort
from google.cloud import pubsub_v1
import json
import time
app = Flask(__name__)
import pymysql
import os

def obtener_conexion():
    db_host = os.getenv("DATABASE_HOST")
    db_user = os.getenv('DATABASE_USER')
    db_pass = os.getenv("DATABASE_PASS")
    db_name = os.getenv('DATABASE_NAME')
    db_port = os.getenv("DATABASE_PORT")
    # db_host = os.environ["DATABASE_HOST"]
    # db_user = os.environ["DATABASE_USER"]
    # db_pass = os.environ["DATABASE_PASS"]
    # db_name = os.environ["DATABASE_NAME"]
    # db_port = os.environ["DATABASE_PORT"]
    return pymysql.connect(host=db_host,
                                user=db_user,
                                password=db_pass,
                                port= db_port ,
                                db=db_name)
    # return pymysql.connect(host='127.0.0.1',
    #                             user='root',
    #                             password='qwerty123',
    #                             port= 3306 ,
    #                             db='db-algoritmos')

def insert_record(tipo, tiempo, largoLista):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Consultas(tipo, tiempo, largoLista) VALUES (%s, %s, %s)",
                       (tipo, tiempo, largoLista))
    conexion.commit()
    conexion.close()

def bubble_algoritm(list):
    n = len(list)
    for i in range(n):
        # print('la i', i)
        for j in range(0, n-i-1):
            # print('la j', j)
            if list[j] > list[j+1]:
                list[j], list[j+1] =list[j+1], list[j]
    return list

def selection_algoritm(list):
    n = len(list)
    for i in range(n):
        # print('la i', i)
        min_index = i
        for j in range(i+1, n):
            # print('la j', j)
            if list[j] < list[min_index]:
                min_index = j
        # Intercambia el elemento mínimo con el primer elemento no ordenado
        list[i], list[min_index] = list[min_index], list[i]
    return list

def insertion_algoritm(list):
    n = len(list)
    for i in range(1, n):
        # Almacena el elemento actual
        elemento_actual = list[i]
        # Comienza a comparar con el elemento anterior en la parte ordenada
        j = i - 1
        # Desplaza los elementos mayores hacia la derecha
        while j >= 0 and elemento_actual < list[j]:
            list[j + 1] = list[j]
            j -= 1
        # Coloca el elemento actual en su posición correcta en la parte ordenada
        list[j + 1] = elemento_actual
    return list

@app.route("/bubble-sort", methods=['POST'])
def bubble_sort():
    data = request.get_json()
    lista = data['lista']
    if lista:
        print(f'Lista a ordenar {lista}')
        tiempo_inicio = time.time()
        sortedList = bubble_algoritm(lista)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        insert_record('bubble sort', tiempo_ejecucion, len(lista))
        print(f'lista ordenada {sortedList}')
        print(f'tiempo {tiempo_ejecucion}')
        return jsonify({"mensaje": "Datos recibidos correctamente."}), 200
    else:
        return jsonify({"mensaje": "Datos recibidos incorrectos."}), 400
    
@app.route("/selection-sort", methods=['POST'])
def selection_sort():
    data = request.get_json()
    lista = data['lista']
    if lista:
        print(f'Lista a ordenar {lista}')
        tiempo_inicio = time.time()
        sortedList = selection_algoritm(lista)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        insert_record('selection sort', tiempo_ejecucion, len(lista))
        print(f'lista ordenada {sortedList}')
        print(f'tiempo {tiempo_ejecucion}')
        return jsonify({"mensaje": "Datos recibidos correctamente."}), 200
    else:
        return jsonify({"mensaje": "Datos recibidos incorrectos."}), 400
    
@app.route("/insertion-sort", methods=['POST'])
def insertion_sort():
    data = request.get_json()
    lista = data['lista']
    if lista:
        print(f'Lista a ordenar {lista}')
        tiempo_inicio = time.time()
        sortedList = insertion_algoritm(lista)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        insert_record('insertion sort', tiempo_ejecucion, len(lista))
        print(f'lista ordenada {sortedList}')
        print(f'tiempo {tiempo_ejecucion}')
        return jsonify({"mensaje": "Datos recibidos correctamente."}), 200
    else:
        return jsonify({"mensaje": "Datos recibidos incorrectos."}), 400


if __name__ == '__main__':
    app.run(debug=True)



# curl -X POST -H "Content-Type: application/json" -d '{
#   "lista": [3, 4, 1, 22]
# }' http://127.0.0.1:5000/bubble-sort

# gcloud pubsub topics create new-list
# gcloud pubsub subscriptions create new-list-sub --topic new-list

# docker build --tag python-docker .
# docker run python-docker:latest

# python -m venv venv
# source venv/bin/activate

        # publisher = pubsub_v1.PublisherClient()
        # project_id = "top-creek-395501"
        # topic_id = "new-list"
        # topic_path = publisher.topic_path(project_id, topic_id)
        # data_published = json.dumps(data ).encode("utf-8")
        # print(topic_path)
        # future = publisher.publish(topic_path, data_published)
        # print(f"Published messages to {topic_path}.")
        # print('future', future.result())