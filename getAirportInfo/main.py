import amadeus
from flask import Flask, request, make_response
import json
from amadeus import Location
from amadeus import Client, ResponseError

app = Flask(__name__)

@app.route('/keyword', methods=['GET'])
def getAirportInfo():
    iata_code = request.args.get('keyword')
    if not iata_code:
        return make_response(json.dumps({"error": "City IATA Code is missing"}), 400)

    try:
        amadeus = Client(
            client_id='b9mXOtZEc0pbUhQBuMjwYA7qGJB6zjx9',
            client_secret='eHUxsx9lfYUQ5Pcv'
        )
        response = amadeus.reference_data.locations.get(
            keyword=iata_code,
            subType=Location.AIRPORT
        )
        
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.data
        if data:
            airport_data = data[0]
            response = {
                "keyword": iata_code,
                "content": airport_data
            }
            return make_response(json.dumps(response), 200, {'Content-Type': 'application/json'})
        else:
            return make_response(json.dumps({"error": "Airport not found"}), 404)

    except ResponseError as error:
        return make_response(json.dumps({"error": f"Amadeus API Error: {error}"}), error.response.status_code)
    except Exception as error: 
        return make_response(json.dumps({"error": f"An error occurred: {error}"}), 500)


if __name__ == "__main__":
    app.run(debug=True)
