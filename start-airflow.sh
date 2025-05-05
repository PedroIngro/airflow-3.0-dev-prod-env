#!/bin/bash

# Caminho do arquivo cfg customizado
CFG_FILE="./config/airflow.cfg"

# Verifica se airflow.cfg existe
if [ -f "$CFG_FILE" ]; then
  echo "🟢 airflow.cfg encontrado. Iniciando com docker-compose.override.yaml..."
  docker compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
else
  echo "🟡 airflow.cfg não encontrado. Iniciando apenas com docker-compose.yaml..."
  docker compose -f docker-compose.yaml up -d
fi
