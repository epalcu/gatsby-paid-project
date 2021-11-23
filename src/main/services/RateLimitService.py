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

        # If new count is greater than customer's rate, we now have to evaluate
        # the requests list and check timestamps to see if we can start discarding
        # requests
        if (count+1 > rate):
            # Don't even traverse requests list if first request is within rate window
            if (self._isWithinRateWindow(requests[0])):
                return False

            # Start traversing requests list and discard requests that are greater than 1 min
            for request in requests[:]:
                if (not self._isWithinRateWindow(request)):
                    count -= 1
                    requests.remove(request)
        
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