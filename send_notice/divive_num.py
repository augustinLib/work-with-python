import pandas as pd


class DivideNum:
    def __init__(self, raw_data, output):
        self.raw_data = raw_data
        self.output = output
        self.new_num = ""
        print("")


    def convert_number(self):
        self.to_pandas = pd.read_excel("./data/raw_data/" + self.raw_data)
        num_list = self.to_pandas["Q2"]

        for _, num in enumerate(num_list):
            temp = num.split("-")[0] + num.split("-")[1] + num.split("-")[2]
            self.new_num = self.new_num + "," + temp


    def export(self):
        with open("./data/result/" + self.output, "w") as file:
            file.write(self.new_num[1:])
