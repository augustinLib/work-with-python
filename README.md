# work-with-python

## 프로젝트 소개
인턴으로 근무하면서 발생한 여러 업무적인 문제점들을 해결해주는 프로젝트입니다. <br/><br/>


## 제작 배경
2022년 7월부터 양재역 근방의 모 회사에서 인턴을 시작하게 되었습니다.
보안서약서로 인해 자세히 적을수는 없지만, 데이터를 수집하고, DB를 관리하고, 해당되는 사람들에게 안내문자 전송과 같은 업무를 주로 맡았습니다.

이러한 일련의 과정들은 프로젝트 참여 인원들의 열람 및 수정이 용이하게 가능하도록 구글 스프레드시트로 진행되었습니다.

그런데, 업무를 구글 스프레드시트로 진행하다보니, 여러 문제점들이 발생하게 되었습니다. 문제점들은 다음과 같습니다. <br/><br/>

- 데이터 개수가 너무 많다보니 스프레드시트를 이용한 관리 시 추가 및 수정 과정에서 실수 발생 
  
- 회사 내부 DB는 1차적으로 다른 DB에 저장된 정보를 통해 구성되어지는데, 이 과정을 수작업으로 한땀한땀 하는 과정에서 누락 및 왜곡 발생
  
- 안내문자 전송 과정에서 몇백명 단위의 사람들에게 안내문자 전송을 해야하는데, 내부 DB에 있는 번호를 일일히 핸드폰에 입력하기에는 한계가 있었음

<br/>
이러한 문제들을 해결하여 업무 효율성과 정확도를 높이기 위해 python 기반의 업무 helper를 제작했습니다. <br/><br/>

## 프로젝트 구성
- main.py : 프로그램을 실행시켜주는 파일

- send_notice : 단체문자 전송에 관련된 Directory
    * init.py
    * notice.py
        -  DB에서 전화번호를 받아와서 단체문자로 전송할 수 있게끔 전화번호 parsing  
        이후 parsing된 전화번호 개수 출력
        - 현 상황에 맞는 안내 문자 자동으로 출력
<br><br>

- check : DB관리에 관련된 Directory
    * init.py
    * check_db.py : 외부 DB에서 내부 DB로 정보 이동할 때, 누락되는 정보가 있었는지 확인


<b>(추후 Javascript 기반의 Google Apps Script 추가 예정)</b>