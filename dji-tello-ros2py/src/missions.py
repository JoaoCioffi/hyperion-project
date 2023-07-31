from wrapper import Tello

drone = Tello()

class Missions():

    @staticmethod
    def __init__(self):
        super(Missions, self).__init__()
    
    @classmethod
    def labDemo():
        drone.query_battery()
