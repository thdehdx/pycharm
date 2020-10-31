import sys


def move(chess_num):
    x, y, z = chess[chess_num]  # 현재 번호 체스말 정보 소환
    nx = x + dx[z]  # 방향에 의한 다음 좌표
    ny = y + dy[z]
    chess_set = []  # 움직일 체스말 덩어리들 저장

    if not 0 <= nx < n or not 0 <= ny < n or raw_map[nx][ny] == 2:  # 범위 밖이거나 파란색일 경우
        if z % 2 == 1:  # z가 1or3이면
            nz = z - 1
        else:
            nz = z + 1
        chess[chess_num][2] = nz  # 체스말정보 수정
        nx = x + dx[nz]  # 다음 좌표 수정
        ny = y + dy[nz]
        if not 0 <= nx < n or not 0 <= ny < n or raw_map[nx][ny] == 2:  # 방향 수정 후에도 범위밖이거나 파란색일 경우
            return 0  # 움직이지 않는다

    for i, key in enumerate(chess_map[x][y]):
        if key == chess_num:
            chess_set.extend(chess_map[x][y][i:])  # chess_num이 엎고 있는 체스말 입력#append와의 차이-> 원소를 넣는다
            chess_map[x][y] = chess_map[x][y][:i]  # [x][y]위치에서 i윗부분 제거
            break
    if raw_map[nx][ny] == 1:
        chess_set = chess_set[-1::-1]  # 빨간 벽일 경우 이동할 체스말 순서 뒤집기
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]  # 해당체스말 위치 정보 변경
    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0


n, k = map(int, input().split())
raw_map = [list(map(int, input().split())) for _ in range(n)]  # N*N#체스보드정보
chess_map = [[[] for _ in range(n)] for _ in range(n)]  # N*N#보드위 체스말정보
chess = [0 for _ in range(k)]  # 3*k#체스말정보

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x - 1][y - 1].append(i)  # 보드위에 체스말 올려 놓기#append쓴이유->쌓기위해서
    chess[i] = [x - 1, y - 1, z - 1]  # 체스말 정보 저장

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]  # 3,9,12,6

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()  # 프로그램 종료
    cnt += 1
print(-1)