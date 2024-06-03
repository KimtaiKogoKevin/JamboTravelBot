import json
import os
import traceback
import functions_framework
from amadeus import Client, ResponseError
from google.cloud import storage
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set environment variables
project_id = 'project id' #Replace with actual project ID
bucket_name = 'BUCKET NAME' #Replace with the bucket name
file_name = 'flight-offer.json'

# Amadeus API credentials - safer to use environment variables
amadeus_client_id = os.environ.get('AMADEUS_CLIENT_ID')
amadeus_client_secret = os.environ.get('AMADEUS_CLIENT_SECRET')

# Initialize Amadeus client -  use environment variables if available
if amadeus_client_id and amadeus_client_secret:
    amadeus = Client(
        client_id=amadeus_client_id,
        client_secret=amadeus_client_secret
    )
else:
    logger.warning("Amadeus API credentials not found in environment. Using hardcoded values for testing purposes. "
                "This is insecure for production environments!")
    amadeus = Client(
        client_id='CLIENT-ID',  # Replace with actual IDs if needed
        client_secret='CLIENT SECRET'
    )

# Function to read data from Google Cloud Storage
def read_data_from_gcs(bucket_name, file_name):
    """Reads data from a file in a Google Cloud Storage bucket.

    Args:
      bucket_name: The name of the GCS bucket.
      file_name: The name of the file in the bucket.

    Returns:
      The content of the file as a string, or None if an error occurred.
    """
    try:
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        content = blob.download_as_string().decode('utf-8')
        return content
    except Exception as e:
        logger.error(f"Error reading from GCS: {e}")
        logger.error(traceback.format_exc()) # Log full traceback for detailed debugging
        return None

# Cloud Function entry point
@functions_framework.http
def flightOffersPrice(request):
    """HTTP Cloud Function to retrieve flight offers pricing.

    Args:
      request: The HTTP request.

    Returns:
      The HTTP response with detailed error messages.
    """
    try:
        logger.info("Request received") # Log the start of the request

        # Get JSON data from request or GCS bucket
        if request.method == 'POST':
            logger.info("POST request received")
            request_json = request.get_json(silent=True)
            if request_json and 'flightOffers' in request_json:
                logger.info("Flight offers found in request JSON")
                flight_offers = request_json['flightOffers']
            else:
                logger.info("Flight offers not in request, attempting to read from GCS")
                data = read_data_from_gcs(bucket_name, file_name)
                print(data)
                if data:
                    flight_offers = json.loads(data)
                    print(flight_offers)
                    logger.info("Successfully read flight offers from GCS")
                else:
                    return "Error: Flight offers not found in request or GCS.", 400
        else:
            logger.warning("Invalid request method")
            return 'Error: Only POST requests are supported.', 405

        logger.info("Constructing request body for Amadeus API")
        # Access the first flight offer
        # flight_offer = flight_offers['flightOffers'][0]



          # Extract the first two flight offers from the dictionary
        # flight_offers_to_price = dict(list(flight_offers.items())[:2])

        # Construct request body for Flight Offers Price API


        # flights = {
        #     "data": flight_offers
        # }
        # print(list(flight_offers.items())[:2])

        logger.info("Making API request to Amadeus")
        # Make API request
        response = amadeus.shopping.flight_offers.pricing.post(flight_offers)
        logger.debug(f"API response: {response.data}")


        logger.info("API request successful, returning response")
        # Return API response
        return response.data, 200

    except ResponseError as error:
        error_message = f'Error: {error} - Status Code: {error.response.status_code} - Details: {error}'
        logger.error(f"Full Error Details: {error.response}") # Add this line to print the full error
        logger.error(error_message)
        return error_message, error.response.status_code
    except Exception as e:
        error_message = f'An unexpected error occurred: {e}'
        logger.error(error_message)
        logger.error(traceback.format_exc()) # Log full traceback
        return error_message, 500
