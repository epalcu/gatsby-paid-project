import json
import redis
from flask import Flask
from services.RedisService import RedisService
from services.ControllerService import ControllerService

###################################
# Main function where app is run. #
###################################
if __name__ == '__main__':
    public = '0.0.0.0'
    local = '127.0.0.1'

    app = Flask(__name__)

    redisService = RedisService()

    for cid in [1, 2, 3]:
        redisService.getCustomerRateForEndpoint(str(cid), 'gatsby')

    controllerService = ControllerService(app)
    controllerService.registerControllers()
        
    app.run(debug=True, host=local)#, threaded=True)