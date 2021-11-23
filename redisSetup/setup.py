#!/usr/bin/env python3

import json
import time
import redis

redisHost = 'localhost'
redisPort = 6379
redisPassword = ""

if __name__ == '__main__':
    try:
        redisObject = redis.StrictRedis(
            host=redisHost, 
            port=redisPort, 
            password=redisPassword, 
            decode_responses=True)
   
        customerIds = [1, 2, 3]
        for cid in customerIds:
            # NOTE: Setting unit just to demonstrate how a user's unit of measure
            # cna be configured to something other than minutes; however, not
            # using the unit value throughout the service just to save time
            value = json.dumps({
                        'api': {
                            'gatsby': {
                                'rate': 10*cid,
                                'unit': 'min', 
                                'count': 0,
                                'requests': []
                            }
                        }
                    })
            redisObject.set(str(cid), value)

        print('\r\nLocal Redis cluster populated with the following key-value pairs: ')
        for cid in customerIds:
            print('{0} -> {1}'.format(cid, json.loads(redisObject.get(str(cid)))))
    except Exception as e:
        print(e)