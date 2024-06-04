# Test Case: Google Vertex AI  Flight Booking Agent Full Flow

## Test Case ID: 002

## Description:
This test case verifies that the Google Vertex AI agent correctly retrieves and returns information from the Amadeus API when deployed in a Cloud Function.
The vertex AI consists of 5 agents , three of which are active and in use , The five agents are
        - Travel Steering Agent
        - FlightSearch Agent
        - Confirm flight offer Price Agent
        - Create Flight order Agent ( not in use)

## Pre-requisites:
1. Google Vertex AI agent is properly set up and configured.
2. Cloud Function is deployed and linked to the Vertex AI agent.
3. Amadeus API is accessible and the API key is valid.

## Test Steps:
1. Greet the user , and determine their intent
2. If the user wants to travel , redirect them to the flight search agent
3. In the flight search agent , determine the following
    - the travelers origin location
    - the travelers destination location
    - the date and time of travelling
    - traveller information i.e how many travellers are included and if any otf them are children
4. Perform the flight search operation by calling the getFlightOffers tool
  - This tool executes a clous function using the request body collected above as a json input parameter
  - it returns the results of the getflightoffers
  - it displays the results to the users
  - if no other questtions are posed it terminates

5. Route the user to the Confirm Flight offer agent
    - Ask the user if he / she wants to see more flight information
    - download the flight offers from a google cloud bucket and use this values as input when calling the flight offers price APi
    -Return this flight information in a user firendly way



## Expected Result:
- The travel Agent should route the agents according to the specification in the examples , it should also pass the destination parameter to the flight search agent
- The flight search agent should return flight offers and provide information on the flight offers data from the amadeus API using the deifned getflightoffers cloud function
- The confirm flight offers agent should download the flight   offer details from the google cloud storage bucket and use the downloaded data to call the amadeus APi using the defined flightoffersprice cloud function
- The confirm flight offer agent should return the data as human readable information in a paragraph

## Actual Result:
- The travel agent works as expected but does not send the parameter to the user
- The flight search agent indeed returns the flight offers and successfully calls the amadeus API
- The confirm flight offer successfully downloads the data ,and uses it to call the amadeus API
    - The function sometimes returns the response as it is returned from the tool and does not summarise it in human readable form unless told
    -The function soemtimes fails to send the downlaoded data from google cloud storage bucket , returning an error 400 , normally trying again fixes the issue , this error seems to be caused by missing information in the request body hence the error 400.

## Status (Pass/Fail):
- Flight search agent calls amadeus API using cloud function and returns Status cose 200
- Confirm flight offer price returns the extra flight information and returns status code 200
- On the rare occcasion when the confirm flight offer price does not work it returns error 400 status code , this is mailnly due to missing information in the   request body.

## Notes:
- The create flight order agent is not included in this submission due to errors , however in the coming days it will be added.
- The plan is to iteratively progress and improve the Jambo Travel Bot
