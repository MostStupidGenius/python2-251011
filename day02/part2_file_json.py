# part2_file_json.py
# json 파일 다루기
# json 파일은 웹 상에서 데이터를 주고받을 사용하는 표준규격 파일이다.
# 이러한 json 파일의 내용은 파이썬에서 배웠던 dictionary 자료구조와
# 완전히 동일하다.
import json

def write_json(data:dict, file_path:str, mode='w', encoding="utf-8", indent=4):
	with open(file_path, mode=mode, encoding=encoding) as f:
		json.dump(obj=data, fp=f, ensure_ascii=False, indent=indent)
		# obj: 저장하고자 하는 json 형태의 객체(dict 자료구조 형태)
		# fp: 열었던 파일 객체(저장할 파일)
		# ensure_ascii: 아스키코드로 작성할지 여부
		# indent: 들여쓰기 시 공백문자를 몇 번 사용할 것인지 설정
	return file_path

def read_json(file_path:str, mode='r', encoding="utf-8", do_print:bool=False):
	# 읽어온 데이터를 담아둘 변수 선언
	data = None
	with open(file_path, mode=mode, encoding=encoding) as f:
		data = json.load(f)
	# 옵션 do_print가 True이면 불러온 데이터 한번 출력하기
	if do_print: print(data)
	# 불러온 데이터 반환하기
	return data

if __name__ == "__main__":
	data = {
		'이름': "홍길동",
		"나이": 30,
		"직업": "학생",
		"취미": ["기타", "독서", "운동"]
	}
	# 파일을 쓰고 해당 파일 경로를 반환한다.
	file_path = write_json(data, "student.json")
	# 썼던 파일 경로를 이용해서 데이터 읽어오기
	data = read_json(file_path, do_print=True)
	print(f"읽어온 데이터:\n{data}")