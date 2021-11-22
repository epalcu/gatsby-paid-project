
from flask_classful import FlaskView, route
from services.RedisService import RedisService
from flask import make_response, redirect, render_template, request, jsonify

class GatsbyController(FlaskView):
    #
    # Constructor
    #
    def __init__(self):
        self.redisService = RedisService()
        # for cid in [1, 2, 3]:
        #     self.redisService.getCustomerRateForEndpoint(str(cid), 'gatsby')
        return

    #
    # Routes
    #
    @route('/')
    def index(self):
        return make_response(redirect('/gatsby'), 302)

    @route('/gatsby', methods=['POST'])
    def gatsby(self):
        customerId = request.headers.get('x-customer-id')
        endpoint = 'gatsby'

        count = 'The invalid request is missing x-customer-id header.'
        if (customerId):
            count = self.redisService.incrementCustomerEndpointCounter(customerId, endpoint)
            if (type(count) is int):
                return make_response(render_template('gatsby.html', 
                    customerId=customerId,
                    endpoint=endpoint,
                    count=count), 200)

        return make_response(jsonify(message=str(count)), 404)

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

        