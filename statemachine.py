class StateMachine:
    def __init__(self, start_state):
        self.cur_state = start_state #시작 생태를 설정
        self.cur_state.enter() #시작 상태로
    def update(self):
        self.cur_state.do()#현재 상태의 동작 수행
    def draw(self):
        self.cur_state.draw()#현재 상태의 그리기 수행