import pandas as pd
import argparse

p = argparse.ArgumentParser()

p.add_argument('--raw_data', required = True)
p.add_argument('--output', required = True)

config = p.parse_args()

class DivideNum:
    def __init__(self, raw_data, output):
        self.raw_data = raw_data
        self.output = output
        self.new_num = ""

    def convert_number(self):
        self.to_pandas = pd.read_excel(self.raw_data)
        num_list = self.raw_data["Q2"]

        for _, num in enumerate(num_list):
            temp = num.split("-")[0] + num.split("-")[1] + num.split("-")[2]
            self.new_num = self.new_num + "," + temp

    def export(self):
        with open(self.output, "w") as file:
            file.write(self.new_num[1:])
