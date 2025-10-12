# part1_file_csv.py
# 파일 입출력 - csv
# csv란, comma seperated values의 약자로 반점으로 구분된 값들의 나열을
# 표 형태로 나타내기 위해 사용되는 파일 형식이다.
# 대표적인 데이터 전달 포맷(파일 형식) 중 하나로, 다른 형식으로는
# csv, json, xml 등이 있다.
import csv # csv 파일을 다루려면 임포트를 해주어야 한다.
# 기본 내장 라이브러리로 설치가 필요없다.

# csv파일은 utf-8로는 읽는 것이 제한된다.(엑셀 프로그램 기준)
# 때문에 인코딩 방식을 utf-8-sig로 설정해주어야 엑셀 프로그램에서도 읽을 수 있다.
# csv 쓰기
def write_csv(file_path:str, mode='w', encoding='utf-8-sig'):
	with open(file_path, mode, encoding=encoding, newline="") as f:
		# newline: 한 행을 작성할 때마다 마지막 부분에 추가할 문자를 지정하는 매개변수
		# 빈문자열"" 혹은 None만 가능하다.
		# csv를 읽으려면 읽기 객체를 생성해주어야 한다.
		writer = csv.writer(f,)
		writer.writerow(["이름", "나이", "직업"]) # 1행에 내용 작성
		writer.writerow(["홍길동", "30", "교사"])
		# writer.writerows() # 이중 리스트(튜플)로 데이터를 작성하여 전달하면
		# 각 리스트요소가 한 행이 되어 파일로 출력된다. 
	return file_path

# csv 읽기
def read_csv(file_path:str, mode='r', encoding='utf-8-sig'):
	rows = [] # 행들의 데이터를 담을 변수 선언
	with open(file_path, mode, encoding=encoding, newline="") as f:
		reader = csv.reader(f) # 데이터 읽어오기
		rows = list(reader) # 다루기 쉬운 자료구조로 변환
		for row in reader: # 한 행씩 차례대로 읽기
			print(row) # 프린트
	return rows # 반환

if __name__ == "__main__":
	# 쓰기 동작 수행
	file_path = write_csv("people.csv")
	# 읽기 동작 수행
	rows = read_csv(file_path)
	print(rows[1])