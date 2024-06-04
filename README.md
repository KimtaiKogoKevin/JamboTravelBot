# Jambo Travel Bot: Project Summary

The **Jambo Travel Bot** is an AI-powered travel assistant designed to streamline flight bookings. Inspired by a passion for artificial intelligence, this project integrates with the Amadeus API using Open API specifications and cloud functions. Here's how it works:

1. **Flight Search**:
   - Utilizes the **Amadeus Flight Offers Search API** to find the cheapest flights for a given itinerary.
   - Returns flight details, including options and pricing.

2. **Price Confirmation**:
   - Uses the **Flight Offers Price API** to confirm availability and final pricing (including taxes and fees) for selected flights.
   - Provides additional information on ancillary products (e.g., extra baggage, seat upgrades) and payment requirements.

3. **Booking Creation**:
   - Utilizes the **Flight Create Orders API** to finalize bookings.
   - Generates a unique booking ID and reservation details upon successful completion.

### Construction
- **Components Used**:
  - Google Vertex AI Agent Builder
  - Google Cloud Functions / Cloud Run
  - Amadeus Self Service Test APIs
  - Google Cloud Storage Bucket

- **Workflow**:
  - User input prompts trigger the bot.
  - Swagger 3.0 Open API specifications guide request body construction.
  - Cloud functions execute Amadeus API logic.
  - Responses are returned to the user.

### Challenges
- Debugging: There were challenges debugging the last Amadeus API , the create flight orders APi , it should however be included ver soon .
- Parameter Passing: There were challenges passing data from one agent to the next
- Correcting Incorrect Responses: Sometimes the request body has incorrect data formats causing error 400 in the response , this is an error i think can be fixed when the agent is fine tuned well.

### Achievements
Successfully integrated the Amadeus Flight Search and Flight Offers Price APIs into the Google Vertex AI agent using cloud functions and Open API Swagger 3.0 specifications.

### Learnings
- Agent Creation: Defined prompts in Google Vertex AI Agent Builder.
- Training: Used examples for agent training.
- API Interaction: Sent requests from Vertex AI to Google Cloud Functions.
- Cloud Function Execution: Executed Amadeus API calls.
- Data Storage: Accessed Google Cloud Storage Buckets.

### Future Plans
Jambo Travel aims to evolve into a comprehensive travel assistant:
- Search for flights
- Confirm flight offers
- Create flight orders
- Assist with hotel bookings
- Provide transportation services
- Enhance the user interface (e.g., seat maps, chat integration)
