class TrafficLights:
    def __init__(self, params):
        self.boxes = []  # x, y, w, h
        self.classes = []  # '3 normal', '4 normal'
        self.signal = []  # 'forward', 'stop', 'stop-left', 'forward-left', 'changing'
        self.frame_no = 0

    def find_main_traffic_light(self, lanes):
        pass

    def get_traffic_light_type(self):
        pass

    def get_traffic_light_sign(self):
        pass


