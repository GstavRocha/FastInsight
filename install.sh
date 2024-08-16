#!/bin/bash

start_time=$(date +%s)
echo "Init Process";
touch .env;
echo ".env" >> .gitignore;
echo 'Install Mongo Local';
sudo apt-get install gnupg curl;
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor;
echo 'Verify SOURCE.list';
echo 'Password SUPERUSER';
sudo touch /etc/apt/sources.list.d/mongodb-org-7.0.list;
echo "Criando o source.list";
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" |
sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list;
sudo cat /etc/apt/sources.list.d/mongodb-org-7.0.list;
sudo apt-get update;
echo "Intalling MongoDB";
sudo apt-get install -y mongodb-org;
sudo systemctl start mongod;
echo "finalizado";
echo 'Creation Enviroment Python ';
python3 -m venv env-pymongo-fastapi 
echo "env-pymongo-fastapi/" >> .gitignore
sudo source env-pymongo-fastapi/bin/activate
echo 'Requeriments Python'; 
pip install -r requeriments.txt;
end_time=$(date +%s);
duration=$((end_time - start_time));
echo "Time in this Install $duration";
