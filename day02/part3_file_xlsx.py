# part3_file_xlsx.py
# 엑셀 파일 다루기
# 엑셀 파일, 즉 xlsx 파일은 MS에서 사용하는 엑셀 프로그램의 대표적인 파일 형식이다.
# 이런 엑셀 파일을 파이썬을 이용하여 자동입력, 출력 등을 할 수가 있다.
# 엑셀 파일을 파이썬으로 다루려면 openpyxl 패키지 설치가 필요하다.
# pip install openpyxl pandas matplotlib
# openpyxl: 엑셀 파일을 파이썬 객체로 다루기 위한 라이브러리
# pandas: 데이터처리를 원활하게 하기 위해 만들어진 데이터 처리 특화 라이브러리
# matplotlib: 데이터 시각화에 특화된 라이브러리
import openpyxl

# 엑셀의 구조
# 엑셀은 워크북이라는 큰 틀 안에 시트라는 단위로 표가 생성되는 방식이다.
# 그래서 파이썬으로 엑셀을 다룰 때에도 워크북을 먼저 열고 그 안에의 시트를 다루어야 한다.

# 엑셀 파일 생성
def create_xlsx(file_path:str):
	# 엑셀의 새 워크북 생성
	wb = openpyxl.Workbook()
	# 해당 워크북에서 활성화된 시트를 객체로 가져옴
	sheet = wb.active
	# 해당 시트에 대해서 A1 방식의 좌표를 키값으로 하여 dict처럼 접근할 수 있다.
	sheet["A1"] = "이름"
	sheet["A2"] = "홍길동"
	sheet["B1"] = "나이"
	sheet["B2"] = 30
	print(sheet["B2"].value, "age")
	# 해당 워크북을 파일로 내보내기
	wb.save(file_path)
	return file_path

def read_xlsx(file_path):
	# 워크북 객체 읽어오기
	wb = openpyxl.load_workbook(file_path)
	sheet = wb.active
	# 시트에서 값을 읽어올 때에는 .value를 붙이면 된다.
	name = sheet["A2"].value
	print(f"이름: {name}")

if __name__ == "__main__":
	file_path = create_xlsx("person.xlsx")
	read_xlsx(file_path)