# gatsby-paid-project

This application implements a rate limit for a single API endpoint.

## Steps to start locally

1. Clone repo
2. Install Docker
3. Install Python3
4. Navigate to root directory in repo
5. Run `source ./setup.sh` in terminal/console
6. Run `source ./startup.sh` in terminal/console

## Using the application

1. Open up Postman
2. Add `http://127.0.0.1:5000/gatsbyStats?customerId=1` to request URL
    * This endpoint displays the Redis details for customer 1. 
    * Please ensure you run this as a GET request.

3. Add `http://127.0.0.1:5000/gatsby` to request URL
    * This endpoint has the rate limiting enforced. 
    * Please include `x-customer-id` header to the request.
    * Please ensure you run this as a POST request.

## Youtube Video Tutorials

1. Running the application:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=KLzNo_IVYrg
" target="_blank"><img src="http://img.youtube.com/vi/KLzNo_IVYrg/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>