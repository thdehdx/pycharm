#입력받는 부분
n,m,k=map(int,input().split())
raw_map = [list(map(int,input().split())) for _ in range(N)]#N*N
#초기화 부분
dy=[-1,1,0,0]#12,6,9,3시 방향
dx=[0,0,-1,1]
shark_map=[[0]*N for _ in range(N)]#N*N#[상어번호,유효기간,방향]
#종료
import sys
sys.exit()
#
from itertools import combinations
#
map=[[0] * N for _ in range(N)]
