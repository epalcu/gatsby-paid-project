docker pull redis

docker run -d -p 6379:6379 --name redis-server redis

source bin/activate

pip3 install -r requirements.txt

python3 redisSetup/setup.py

deactivate