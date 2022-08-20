import argparse
from distutils.command.config import config

from send_notice.divive_num import DivideNum

def define_parser():
    p = argparse.ArgumentParser()

    # --mode : 필요한 기능에 따라 모드 설정(필수 입력)
    # --mode 1 : 단체문자 전송을 위한 전화번호 쪼개기
    p.add_argument('--mode', required=True)

    # --raw_data : 전화번호가 담겨있는 원본 파일 경로
    # --output : 전화번호를 단체문자로 돌릴 수 있게끔 변환한 파일을 내보낼 경로
    p.add_argument('--raw_data')
    p.add_argument('--output')

    config = p.parse_args()
    return config


def main():
    config = define_parser()
    # mode 1 : 단체문자 전송을 위한 전화번호 쪼개기
    if config.mode == "1":
        divide = DivideNum(config.raw_data, config.output)
        divide.convert_number()
        divide.export()
        return
        




if __name__ == "__main__":
    main()

