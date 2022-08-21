import argparse
from send_notice.divive_num import DivideNum
from check.check_db import CheckDB

# argparser보다 input으로 mode 설정하는것이 더 효율적이라고 판단하여 교체
def define_mode():
    print("사용할 기능을 입력하세요")
    print("1 : 단체문자 전송")
    print("2 : 내부 DB 검사")
    
    mode = input("")
    return mode


def main():
    mode = define_mode()
    # mode 1 : 단체문자 전송을 위한 전화번호 쪼개기
    if mode == "1":
        print("------------------------------")
        raw_data = input("원본 파일의 경로를 입력해주세요 : ")
        output = input("내보낼 파일의 경로와 이름을 지정해주세요 : ")
        divide_num = DivideNum(raw_data, output)
        divide_num.convert_number()
        divide_num.export()

        print("------------------------------")
        print("전화번호 추출 완료")
        return

    if mode == "2":
        print("------------------------------")
        inner_db = input("내부 DB 파일의 경로를 입력해주세요 : ")
        out_db = input("외부 DB 파일의 경로를 입력해주세요 : ")
        check_db = CheckDB(inner_db, out_db)
        check_db.return_result()

        print("------------------------------")
        print("내부 DB 검사 완료")

        return
        





if __name__ == "__main__":
    main()

