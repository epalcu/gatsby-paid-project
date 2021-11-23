import time 

class RateLimitService():
    #
    # Constructor
    #
    def __init__(self, redisService):
        self.redisService = redisService
        return

    #
    # Public Methods
    #
    def isWithinRateWindow(self, customerId, endpoint):
        customerDetails = self.redisService.getCustomerDetails(customerId)
        requests = self._getCustomerEndpointRequests(customerDetails, endpoint)
        rate = self._getCustomerEndpointRate(customerDetails, endpoint)
        count = self._getCustomerEndpointCount(customerDetails, endpoint)

        # NOTE: If new count is greater than customer's rate, we only check the first
        # request in the requests list. Maintaining a count key is much more efficent 
        # than running len(requests), especially if the rate is increased to 
        # something like 3000 requests/second
        if (count+1 > rate):
            firstRequest = requests[0]
            if (self._isWithinRateWindow(firstRequest)):
                return False
            else:
                count -= 1
                requests.remove(firstRequest)
        
        count += 1
        requests.append(time.time())

        customerDetails['api'][endpoint]['requests'] = requests
        customerDetails['api'][endpoint]['count'] = count
        self.redisService.setCustomerDetails(customerId, customerDetails)

        return True

    #
    # Private Methods
    #
    def _getCustomerEndpointRequests(self, customerDetails, endpoint):
        return customerDetails['api'][endpoint]['requests']

    def _getCustomerEndpointRate(self, customerDetails, endpoint):
        return customerDetails['api'][endpoint]['rate']

    def _getCustomerEndpointCount(self, customerDetails, endpoint):
        return customerDetails['api'][endpoint]['count']

    # NOTE: I'm defaulting the value to 60 secons (1 min); however,
    # the ideal solution would pass in the configured unit of measure
    # for this particular user
    def _isWithinRateWindow(self, requestTimestamp):
        currentTime = time.time()
        return currentTime - 60 < requestTimestamp