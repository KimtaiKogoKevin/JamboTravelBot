# PROJECT SUMMARY: Jambo Travel Bot
### Inspiration
 The idea for the Jambo Travel Bot was born out of a passion for artificial
intelligence, nurtured during a computer science degree. The decision to create a
customer-facing travel AI agent bot that assists with flight bookings was influenced by the
practicality and modern-world applicability of such a tool.
### Functionality
The bot serves as a flight booking agent, it integrates with the Amadeus API
using Open API specifications and cloud functions. The process involves three steps:
#### `Searching for flights`
Using the Amadeus Flight Offers Search API, the agent  returns the
cheapest flights for a given itinerary.
### `Confirming the availability and final price (including taxes and fees)`
Confirm the fares of the fligh offers using the Flight Offers Price API. This step also provides pricing for ancillary products like
additional bags or extra-legroom seats and details on the payment information required
to complete the booking.
### `Creating a flight order`
 Using the Flight Create Orders API, which performs the final
booking for a chosen flight and provides a unique booking ID and reservation details
once the reservation is completed.

######  Detailed APi Flow

 **GetOfferQuery**

 - This Query takes as input a query from the traveller , i.e the destination , origin and dates of travel , it obtains this data from the traveler and builds a request body.

 - The output of this query is a flight Offer ,it returns the flight details




 **FlightOffersPricing**

 - This query takes as input the previous flight offer and a payment Object . The payment object is only available in enterprise APIs not with self service APIs. In this project we use self service API so it only takes the flight offer input.

 - This query outputs the flight offer and tells you wether it is confirmed on top of this it adds any other ancilary data about the flight offer


The project functionality can be summarized as follows
1. Recieve a request from the traveler through the google vertex AI platform
2. Manipulate this input in any ways neccessary i.e build a request body
2. Call a cloud function which runs the Amadeus API logic
3. Return the results of the cloud function


### Construction
 The Jambo Travel Bot operates entirely on REST APIs and the Google Cloud
Platform. It was built using the Google Vertex AI Agent Builder, Google Cloud Functions /
Cloud Run, Amadeus Self Service Test APIs, and Google Cloud Storage Bucket.
 The bot takes input from the traveler through a prompt,it then  builds a request body using Swagger 3.0 Open API
specifications. It sends this request by triggering the respective cloud function, obtaining rhe data from Amadeus Api  and returns the
response to the user. [Amadeus] [https://developers.amadeus.com/]
In certain  use cases, the project stores JSON data in a Google Cloud Storage
Bucket and downloads it for use when calling the Amadeus API.
### Challenges
The project faced some challenges,such as
- lengthy debugging periods,
- difficulties in passing parameters from one agent to another,
- correcting incorrect responses and debugging certain errors to ensure the data being passed in the request body is valid according to amadeus APIs specifcations. [Amadeus][https://developers.amadeus.com/]
### Achievements
The integration of the [Amadeus Flight Search] [[https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search]] and [Flight Offers Price] [https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-price] API to the
Google Vertex AI agent using cloud functions and Open API Swagger 3.0 specifications is a
significant accomplishment.
### Learnings
The project provided valuable experience in creating an agent and giving it prompts
on Google Vertex AI Agent Builder.
- I learnt how to use examples to train the agent with input and output
summaries,
- Howto use an Open API specification tool to send requests from the Vertex AI agent to
Google Cloud Functions,
- Executing the Amadeus API from a cloud function and returning theresponse in the Vertex AI agent, storing output from API calls in Google Cloud Storage Buckets,
- Accessing the data in the GCS bucket from the cloud function for use when calling an API.

### Future Plans
 The goal for Jambo Travel is to evolve into a full travel assistant that can search for flights, `confirm flight offers`, `create a flight order`, `help users find the perfect stay at over 150,000 hotels worldwide`, `provide transportation services using an intellegent google vertex AI agent builder chat bot` , and `display flight seat map information and any other data on an intuitve usewr interface`.
