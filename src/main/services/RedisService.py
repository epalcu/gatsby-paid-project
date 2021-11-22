import json
import redis
from config.RedisConfig import RedisConfig

class RedisService():
    #
    # Constructor
    #
    def __init__(self):
        redisConfig = RedisConfig()
        self.service = redis.StrictRedis(
            host=redisConfig.getHost(), 
            port=redisConfig.getPort(), 
            password=redisConfig.getPassword(), 
            decode_responses=True)
        return

    #
    # Public Methods
    #
    def getCustomerRateForEndpoint(self, customerId, endpoint):
        rate = json.loads(self.service.get(customerId))['api'][endpoint]['rate']
        
        print('getCustomerRateForEndpoint() - customerId={0}, endpoint={1}, rate={2}'.format(
            customerId, 
            endpoint, 
            rate))

        return rate

    def getCustomerUnitForEndpoint(self, customerId, endpoint):
        unit = json.loads(self.service.get(customerId))['api'][endpoint]['unit']

        print('getCustomerUnitForEndpoint() - customerId={0}, endpoint={1}, unit={2}'.format(
            customerId, 
            endpoint, 
            unit))

        return unit