![featured-image](https://raw.githubusercontent.com/andela-mnzomo/project-dream-team-one/master/flask-crud-part-one.jpg)

The code for Part One of my three-part tutorial, *Build a CRUD Web App With Python and Flask*.



gcloud container clusters create cassandra --num-nodes=3 --machine-type "n1-standard-2"

kubectl cp holidays.csv cassandra-4k57q:/holidays.csv

CREATE KEYSPACE calendar WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2};

CREATE TABLE calendar.holidays (id int PRIMARY KEY, name text, description text, locations text, date text);

COPY calendar.holidays(id,name,description,locations,date) FROM 'holidays.csv' WITH DELIMITER=',' AND HEADER=TRUE;

docker build -t gcr.io/${PROJECT_ID}/holidays-app:v1 .

docker push gcr.io/${PROJECT_ID}/holidays-app:v1

kubectl run holidays-app --image=gcr.io/${PROJECT_ID}/holidays-app:v1 --port 8080

kubectl expose deployment holidays-app --type=LoadBalancer --port 80 --target-port 8080

kubectl get services
CREATE KEYSPACE pokemon WITH REPLICATION =
{'class' : 'SimpleStrategy', 'replication_factor' : 2};
