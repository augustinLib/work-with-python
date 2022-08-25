import pandas as pd


class CheckDB:
    def __init__(self, inner_db, surveybox):
        self.exception_list = []
        self.inner_list = []
        self.surveybox_list = []
        self.exception_table = pd.read_excel("./data/exception_list.xlsx")

        # exception_list 생성
        for i in range(len(self.exception_table)):
            inner_name_number = (self.exception_table.iloc[i,0], self.exception_table.iloc[i,1])
            self.exception_list.append(inner_name_number)

        # 각 DB별 list 생성
        self.inner_db =  pd.read_excel("./data/raw_data/" + inner_db)
        self.surveybox = pd.read_excel("./data/raw_data/" + surveybox)

        self.inner_db = self.inner_db.iloc[:, [1,2]]
        self.inner_db.columns = ["Q1", "Q2"]
        self.inner_db.dropna(axis=0, inplace=True)
        self.inner_db.reset_index(inplace=True, drop=True)

        self.surveybox_person = self.surveybox[["Q1", "Q2"]]

        for i in range(len(self.inner_db)):
            inner_name_number = (self.inner_db.iloc[i,0], self.inner_db.iloc[i,1])
            self.inner_list.append(inner_name_number)

        for i in range(len(self.surveybox_person)):
            survey_name_number = (self.surveybox_person.iloc[i,0], self.surveybox_person.iloc[i,1])
            self.surveybox_list.append(survey_name_number)    

    # 외부 DB에 있는데 내부 DB에 없는 사람 조회 후 결과값 반환
    def return_result(self):
        count = 0
        missing_list = []
        print("검사 시작 : 아래 목록의 사람들이 내부 DB에 없습니다")
        for i, person in enumerate(self.surveybox_list):
            if person not in self.inner_list:
                if person not in self.exception_list:
                    print(person)
                    missing_list.append(person)

                    count += 1

            
        print("총 %d명 누락됨" %count)
        return missing_list



