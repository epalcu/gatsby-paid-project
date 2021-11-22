from controllers.GatsbyController import GatsbyController

class ControllerService():
    #
    # Constructor
    #
    def __init__(self, app):
        self.app = app
        self.gatsbyController = GatsbyController()
        
    #
    # Public Methods
    #
    def registerControllers(self):
        self.gatsbyController.register(
            self.app, 
            route_base='/')