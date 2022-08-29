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

        count = 0
        for _, num in enumerate(num_list):
            temp = num.split("-")[0] + num.split("-")[1] + num.split("-")[2]
            self.new_num = self.new_num + "," + temp
            count += 1

        print("총 %d명 추출 완료" %count)
        


    def export(self):
        with open("./data/result/" + self.output, "w") as file:
            file.write(self.new_num[1:])


class SelectMessage:
    def __init__(self):
        print("---------------------------------")
        print("공지의 종류를 고르세요")
        print("1 : 신규 신청자 안내 공지")
        print("2 : 약한 강우 시 안내 공지")
        print("3 : 우천 취소 시 안내 공지")
        print("---------------------------------")

        self.notice_type = int(input("공지 종류 번호 : "))

    def print_notice(self):
        if self.notice_type == 1:
            with open("./data/new_notice.txt", "r") as notice:
                result = notice.read()
                print(result)

        elif self.notice_type == 2:
            with open("./data/weak_rain_notice.txt", "r") as notice:
                result = notice.read()
                print(result)

        elif self.notice_type == 3:
            with open("./data/strong_rain_notice.txt", "r") as notice:
                result = notice.read()
                print(result)

        print()
        print("공지 출력 완료")
        
