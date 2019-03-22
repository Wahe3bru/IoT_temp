# IoT_temp
A multi stage project in learning IoT; the logic and planning involved. <br>
Hoping to pick up new skills as they are required.
##### skills to learn:
- unit testing
- data pipeline/s (luigi / airflow)
- software development best practices
- AWS (boto)

### Proposed stages of development
#### stage: Hardware
- [x] setup pi
- [x] connect sensor to pi
- [x] remote setup for headless pi

#### stage: GSheets
- [x] post sensor data to gsheets (<s>15</s> 30 min intervals)
- [x] daily statistics script (executed at 11pm)
- - [x] min, mean, max for temp and humidity logged
- - [ ] optional: add outside temperature from weather api

#### stage: AWS RDS
- [ ] create aws rds (mySQL or Postgres)
- [ ] db design (schema)
- [ ] Update db
- - [ ] goal: research aws lambda
- - [ ] interim: py script to update db

#### stage: Dashboard
- [ ] interim: GSheets graphs
- [ ] basics Dash Dashboard
- - [ ] optional: Tableau Dashboard
- [ ] web accessible Dash Dashboard (login)

#### Further stages:
- a similar pipeline using Azure and GCP
- using a NoSQL db
