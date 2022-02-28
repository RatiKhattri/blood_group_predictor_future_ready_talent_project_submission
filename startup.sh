az webapp config set --resource-group <blood_group_predictor> --name <bloodgrouppredictorapp> --startup-file "<python -m uvicorn application:blood_group_predictor --host 0.0.0.0>"
