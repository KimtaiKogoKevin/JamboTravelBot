import functions_framework
import json
from flask import Request
from google.cloud import logging
from google.cloud import storage
from amadeus import Client, ResponseError

# Initialize the Google Cloud Logging client
logging_client = logging.Client()
logger = logging_client.logger(__name__)

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

# Define the GCS bucket and file name
bucket_name = 'travelstore'  # Replace with your actual bucket name
file_name = 'flight-offer.json'

@functions_framework.http
def getFlightOffers(request: Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    
    # Initialize the Amadeus client
    amadeus = Client(
      client_id='b9mXOtZEc0pbUhQBuMjwYA7qGJB6zjx9',
      client_secret='eHUxsx9lfYUQ5Pcv'
    )
    
    # Get the request body
    request_json = request.get_json(silent=True)
    
    if request_json is not None and 'currencyCode' in request_json:
        currency_code = request_json['currencyCode']
        origin_destinations = request_json.get('originDestinations', [])
        travelers = request_json.get('travelers', [])
        sources = request_json.get('sources', [])
        search_criteria = request_json.get('searchCriteria', {})
        
        # Log the request data
        logger.log_text(f"Currency Code: {currency_code}")
        logger.log_text(f"Origin Destinations: {origin_destinations}")
        logger.log_text(f"Travelers: {travelers}")
        logger.log_text(f"Sources: {sources}")
        logger.log_text(f"Search Criteria: {search_criteria}")
        
        # Create the request body
        body = {
            'currencyCode': currency_code,
            'originDestinations': origin_destinations,
            'travelers': travelers,
            'sources': sources,
            'searchCriteria': search_criteria
        }
        
        try:
            # Make the API request
            response = amadeus.shopping.flight_offers_search.post(body)
            logger.log_text(f"Response: {response.data}")
            print(response.data)

            # Store the response in GCS
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.upload_from_string(json.dumps(response.data), content_type='application/vnd.amadeus+json')

            return json.dumps(response.data)
        except ResponseError as error:
            logger.log_text(f"Error: {error}")
            return json.dumps({"error": str(error)}), 500 
    else:
        return 'Error: Invalid request body.', 400
