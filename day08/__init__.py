# day08/__init__.py
import sys
import os

# 현재 파일의 경로를 추출 -> __file__
# 부모폴더의 경로를 추출 -> os.path.dirname(경로)
workspace_path = os.path.dirname(os.path.dirname(__file__))
print(workspace_path) # d:\python2_0930_ljs_2510\workspace

# sys 모듈을 이용하여 시스템 환경변수에 등록한다.
sys.path.append(workspace_path)

# d:\python2_0930_ljs_2510\workspace 안의 day05에 접근할 수 있게 된다.
from day03.part3_basic_bubble import clock