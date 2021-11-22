#!/usr/bin/env python3

import json
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
   
        print('Populating local Redis cluster with the following key-value pairs: ')

        customerIds = [1, 2, 3]
        for cid in customerIds:
            value = json.dumps({
                        'api': {
                            'gatsby': {
                                'rate': 10*cid,
                                'unit': 'min'
                            }
                        }
                    })
            print('{0} -> {1}'.format(cid, value))
            redisObject.set(str(cid), value)

        print('\r\nLocal Redis cluster populated with the following key-value pairs: ')
        for cid in customerIds:
            print('{0} -> {1}'.format(cid, json.loads(redisObject.get(str(cid)))))
    except Exception as e:
        print(e)