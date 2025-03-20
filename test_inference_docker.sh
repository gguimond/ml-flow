#!/bin/bash
# Instruction on inference formart:
# https://stackoverflow.com/questions/75096564/unrecognized-content-type-parameters-format-when-serving-model-on-databricks-ex
# https://mlflow.org/docs/latest/deployment/deploy-model-locally.html#local-inference-server-spec

curl http://127.0.0.1:6002/invocations -H 'Content-Type: application/json' -d '{
  "dataframe_split": {
    "data": [[6.1, 2.8, 4.7, 1.2]]
  }
}'

curl http://127.0.0.1:6002/invocations -H 'Content-Type: application/json' -d '{
  "dataframe_split": {
    "data": [[5.7, 3.8, 1.7, 0.3]]
  }
}'