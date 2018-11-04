# AT USSD App
This is a simple Flask app that talks to the Africa's Talking servers with USSD logic

## Getting started

Create an Africa's Talking account or sign into your account. Head over to the Sandbox section and get your API key to make sure that your app can be authenticated by the servers.

### Initializing the app
While in the project directory,activate python virtual environment by

```
source ./venv/bin/activate
```

Download the python file to your project folder. 
Install flask making sure all the dependencies are fulfiled

```
pip install flask
```
OR (depending on how your Python installation works)
```
pip3 install flask
```

Once done, run the file with

```
python3 app.py
```
OR (depeding on your python installation)
```
python app.py
```
The server should be up and running after that.

### Exposing the app to the internet
Get [ngrok](https://ngrok.com/)

Head over to where you have installed ngrok and run: 

```
./ngrok http 5000
```
This is the workflow for Unix based systems (Linux and MacOS) I'll add something for Windows later. Or check ngrok docs. 
That maps the localhost to a live link hosted by ngrok.

### Linking to Africa's Talking
Once your link is live, copy it and add it to the callback URL field on your create USSD channel section on your dashboard. Once done, head on to the simulator and use the USSD code generated from the dashboard. 

## It should be running!! 

If you have any problems, raise and issue here and I will be sure to help out!
