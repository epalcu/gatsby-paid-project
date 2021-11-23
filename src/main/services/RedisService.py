import json
import time
import redis

class RedisService():
    #
    # Constructor
    #
    def __init__(self, redisConfig):
        self.service = redis.StrictRedis(
            host=redisConfig.getHost(), 
            port=redisConfig.getPort(), 
            password=redisConfig.getPassword(), 
            decode_responses=True)
        return

    #
    # Public Methods
    #
    def getCustomerDetails(self, customerId):
        try:
            customerDetails = json.loads(self.service.get(customerId))

            print('Returning customer details: {0}'.format(customerDetails))

            return customerDetails
        except Exception as e:
            print('Customer details not found: {0}'.format(e))
            return None

    def setCustomerDetails(self, customerId, customerDetails):
        try:
            print('Setting customer details: {0}'.format(customerDetails))

            self.service.set(customerId, json.dumps(customerDetails))
        except Exception as e:
            print('Customer details cound not be set: {0}'.format(e))
            return None