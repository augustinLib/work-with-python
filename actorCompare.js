/** @OnlyCurrentDoc */

// 속성 입력값은 2씩 커짐
// 따라서 30부터 시작한다고 하면, 30, 32 한 세트로 묶어서 비교 후 값 return


function actorNum(range) {
    var doc = SpreadsheetApp.getActive();
    var sheet = doc.getSheetByName("데이터 수집 관리 파일(수정)");
    var scope = sheet.getRange(range).activate();
    var readData = scope.getValues()
    var result = 0;
    var tempList = [];
  
  
    for (var i = 0; i < readData.length; i++) {
      tempList.push(readData[i][0])
    }
    for (var index = 0; index <= tempList.length - 4; index += 4) {
      if (tempList[index] == 1 && tempList[index+2] == 1) {
        result += 1;
      }
  
      else if (tempList[index] == 1 && tempList[index+2] == 0) {
        result += 1;
      }
  
      else if (tempList[index] == 0 && tempList[index+2] == 1) {
        result += 1;
      }
      
    }
    
    return result;
  }