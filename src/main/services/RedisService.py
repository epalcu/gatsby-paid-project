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

            return json.dumps(customerDetails)
        except Exception as e:
            print('Customer details not found: {0}'.format(e))
            return None

    def incrementCustomerEndpointCounter(self, customerId, endpoint):
        try:
            customerDetails = json.loads(self.service.get(customerId))
            count = customerDetails['api'][endpoint]['count']
        
            print('incrementCustomerEndpointCounter() - customerId={0}, endpoint={1}, count={2}'.format(
                customerId, 
                endpoint, 
                count))

            count += 1

            print('Incrementing enpoint counter - customerId={0}, endpoint={1}, count={2}'.format(
                customerId, 
                endpoint, 
                count))

            customerDetails['api'][endpoint]['count'] = count
            customerDetails['api'][endpoint]['timestampOfLastRequest'] = time.time()
            self.service.set(customerId, json.dumps(customerDetails))

            return count
        except Exception as e:
            print('Customer counter could not be incremented: {0}'.format(e))
            return e