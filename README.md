# iTrainingWebApp
Development code for the AMS Project, using python flask to create the training app iTraining

## Ubuntu
### Setup the repository (first time)

Run the following lines on a terminal:
1) First create a venv : 
```bash
python3 -m venv venv
```
2) Load venv on bash
```bash
source venv/bin/activate
```
3) Install the requirements 
```bash
pip install -r requirements.txt
```
###### Done

----

### Run the Flask App
Run the following lines on a terminal:
```bash
export FLASK_APP=app.py
```
if you want to see errors activate debug:
```bash
export FLASK_DEBUG=1
```
```bash
flask run
```
The app is going to be hosted on the link for example
```bash
<code> * Running on http://127.0.0.1:5000/</code>
```
------

### Windows users, follow instructions bellow
https://flask.palletsprojects.com/en/1.1.x/installation/

-----

### Flask documentation

https://flask.palletsprojects.com/en/1.1.x/

------

### Auto Deployment

The app is auto deployed on the main server

https://itraining-ams.azurewebsites.net/
