from config.RedisConfig import RedisConfig
from flask_classful import FlaskView, route
from services.RedisService import RedisService
from services.RateLimitService import RateLimitService
from flask import make_response, redirect, render_template, request, jsonify

class GatsbyController(FlaskView):
    #
    # Constructor
    #
    def __init__(self):
        # NOTE: Ideally, this would be injected through the constructor;
        # However, the FlaskView module doesn't allow to pass arguments
        # when registering new controllers
        self.redisService = RedisService(RedisConfig())
        self.rateLimitervice = RateLimitService(self.redisService)

    #
    # Routes
    #
    @route('/')
    def index(self):
        return make_response(redirect('/gatsby'), 302)

    #
    # /gatsby route which takes in x-customer-id header to track user's request count
    #
    @route('/gatsby', methods=['POST'])
    def gatsby(self):
        customerId = request.headers.get('x-customer-id')
        endpoint = 'gatsby'

        if (customerId):
            if (self.rateLimitervice.isWithinRateWindow(customerId, endpoint)):
                return make_response(render_template('gatsby.html', customerId=customerId), 200)
            
            message = 'Hello, Gatsby customer {0}! You have exceeded your allowable request count for the \'/{1}\' endpoint'.format(customerId, endpoint)
            statusCode = 429
        else:
            message = 'The invalid request is missing x-customer-id header.'
            statusCode = 404

        return make_response(jsonify(message=message), statusCode)

    #
    # /gatsbyStats route which takes in customerId query parameter to display user's request count details
    #
    @route('gatsbyStats')
    def gatsbyStats(self):
        customerId = request.args.get('customerId')

        customerDetails = 'The invalid request is missing customerId query parameter.'
        if (customerId):
            customerDetails = self.redisService.getCustomerDetails(customerId)
            if (customerDetails):
                return make_response(render_template('gatsbyStats.html', customerDetails=customerDetails), 200)
            else:
                customerDetails = 'Please provide a valid customerId value.'

        return make_response(render_template('gatsbyStats.html', customerDetails=customerDetails), 404)

        