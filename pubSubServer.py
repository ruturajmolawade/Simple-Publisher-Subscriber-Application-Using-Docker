from flask import Flask,redirect, url_for,request,render_template,make_response,session,jsonify
from flask_cors import CORS
import sys,io
import responses
import requests
import contextlib
from pubsub import Subscriber, Publisher

app = Flask(__name__)
CORS(app)
app.secret_key='Axcv'

@app.route('/publisher')
def publisher():
   return render_template('publisher.html')

@app.route('/publishEvent')
def publishEvent():
    responses.add(responses.GET,
            'https://maps.googleapis.com/maps/api/directions/json',
             body='{"status":"OK"}',
             status=200,
             content_type='application/json'
             )
    event = str(request.args.get('event'))
    message = str(request.args.get('message'))
    publisherObj = Publisher()
    publishedMessageDict = publisherObj.publish(event,message)
    return jsonify(output = 'SUCCESS')
    # publishedMesage = publishedMessageDict[]


@app.route('/subscribeToEvent')
def subscribeToEvent():
    responses.add(responses.GET,
            'https://maps.googleapis.com/maps/api/directions/json',
             body='{"status":"OK"}',
             status=200,
             content_type='application/json'
             )

    event = str(request.args.get('event'))
    subscriberName = str(request.args.get('name'))
    subscriberObj = Subscriber(subscriberName)
    message = subscriberObj.register(event)
    return jsonify(message_out = message,output='SUCCESS')

@app.route('/subscriber')
def subscriber():
   return render_template('subscriber.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=81,debug=False)
   #app.run()

 