import json
from airflow.decorators import dag, task
from datetime import datetime

# Caminho para o arquivo connections.json
connections_file = '/opt/airflow/config/connections.json'

# Função para gerar os comandos de adição de conexões
def generate_add_connection_command(conn_id, conn_json):
    # Garante que o conn_id está dentro de conn_json e remove qualquer duplicação.
    conn_json.pop("conn_id", None)  # Remover o conn_id, pois ele já é passado como argumento.
    
    return f"""
    docker exec airflow_30-airflow-apiserver-1 airflow connections add '{conn_id}' --conn-json '{json.dumps(conn_json)}'
    """

# Carregue as conexões do arquivo JSON
with open(connections_file, 'r') as f:
    connections = json.load(f)

# Defina a DAG
@dag(
    'add_airflow_connections_from_json',
    description='DAG para adicionar várias conexões ao Airflow no Docker com base em um arquivo JSON',
    catchup=False,
)
def add_airflow_connections():
    # Definindo a task para adicionar conexões
    @task.bash
    def add_connection_to_airflow(conn_id, conn_json):
        command = generate_add_connection_command(conn_id, conn_json)
        return command

    # Criação das tasks dinamicamente
    for conn in connections:
        conn_id = conn.get('conn_id')
        if conn_id:  # Verifica se existe o conn_id
            add_connection_to_airflow(conn_id, conn)

# Instanciando a DAG
dag_instance = add_airflow_connections()
