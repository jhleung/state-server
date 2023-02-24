from flask import Flask, request, Response
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json
app = Flask(__name__)

states = []
states_file = 'states.json'


@app.before_first_request
def loadStatesFromJson():
    with open(states_file, 'r') as file:
        for state in file:
            states.append(json.loads(state))


@app.route('/', methods=['POST'])
def getState():
    longitude = request.values.get('longitude')
    latitude = request.values.get('latitude')
    if longitude is None or latitude is None:
        return Response(
            "Bad Request. Please supply a longitude and latitude.\n",
            status=400
        )

    for state in states:
        borders = state['border']
        border_tuple = [tuple(x) for x in borders]

        state_polygon = Polygon(border_tuple);
        point = Point(longitude, latitude)

        if (point.within(state_polygon)):
            return Response(
                "[\"{}\"]\n".format(state['state']),
                status=200
            )
    return Response(
            "No U.S. state found given coordinate.\n",
            status=200
        )


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0', port=8080)