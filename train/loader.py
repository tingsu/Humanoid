#coding=utf-8

import os
import pickle

import numpy as np
import tensorflow as tf

class Loader():
    """Basic data loader
    """
    def __init__(self, config_json):
        self.x_dim, self.y_dim = config_json["downscale_dim"]
        self.training_dim = config_json["training_dim"]
        self.predicting_dim = config_json["predicting_dim"]
        self.total_interacts = config_json["total_interacts"]
        self.training_data_dir = config_json["training_data_dir"]

    def next_batch(self):
        pass

class DebugLoader(Loader):
    def __init__(self, config_json):
        super().__init__(config_json)
        self.data_file = "jp.naver.linecard.android.pickle"
        self.data_path = os.path.join(self.training_data_dir, self.data_file)

    def next_batch(self):
        with open(self.data_path, "rb") as f:
            input_data = pickle.load(f)
        images = np.stack([x[0][:,:,:self.training_dim]
                           for x in input_data["trace_0"]], axis=0)
        heatmaps = np.stack([x[0][:,:,-self.predicting_dim:]
                             for x in input_data["trace_0"]], axis=0)
        interacts = np.eye(self.total_interacts)[[x[1]["interact_type"] for x in input_data["trace_0"]]]
        return images, heatmaps, interacts