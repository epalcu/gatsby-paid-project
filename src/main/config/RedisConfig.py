class RedisConfig():
    #
    # Constructor
    #
    def __init__(self):
        # Ideally, this would be pulled from an environment specific config file
        # in the repo; however, I'm cutting a corner here to save time
        self.host = 'localhost'
        self.port = 6379
        self.password = ''
        
        return

    #
    # Public Methods
    #
    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    # Ideally, the password would be stored in a secret remote location, like AWS Secrets Manager
    # However, I'm cutting another cornet to save time
    def getPassword(self):
        return self.password