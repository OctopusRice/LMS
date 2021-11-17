import os
import cv2
from core import Lanes, TrafficLights, Objects


class DataLoader:
    def __init__(self, _source_name, _root='../../datasets'):
        self.source_name = _source_name
        self.root = _root
        self.objs = []
        self.lines = []

    # Load data from directiory
    def load_data(self):
        dir = f'{self.root}/{self.source_name}'

        lanes = []
        traffic_lights = []
        objects = []

        with open('filename'):
            lanes.append(Lanes())
            traffic_lights.append(TrafficLights())
            objects.append(Objects())

        return lanes, traffic_lights, objects


