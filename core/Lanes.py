class Lanes:
    def __init__(self, params):
        self.boxes = []  # x, y, w, h
        self.colors = []  # 'white', 'yellow'
        self.classes = []  # '1_line', '1_dot', '2_line', '2_dot'
        self.is_stop_lane = []  # True, False
        self.frame_no = 0

    def find_semantic_lane(self):
        pass

    def get_lane_color(self):
        pass

    def get_lane_type(self):
        pass

    def check_stop_lane(self):
        pass

