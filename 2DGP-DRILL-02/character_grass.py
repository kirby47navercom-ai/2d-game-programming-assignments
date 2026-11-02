from pico2d import *
# *로 쓰면 아무것도 안쓰고 바로 가능
# pico2d에 있는 함수를 그냥 써도 된다는 뜻
# using namespace std; c++에서 이거랑 비슷
#원래는 pico2d.open_canvas() 이렇게 써야함

#open_canvas()#캔버스 키기
#hide_lattice()#모눈종이 끄기
#show_lattice()#모눈종이 켜기
#캔버스 죄표계는 왼쪽아래에서 시작 윈플은 왼쪽 위에서 시작한 것을 생각하면 다름
#게임에서는 png를 더 많이씀
#png는 투명도 지원 때문에 많이 씀
#jpg는 화질에 손상이 있음 압축을 하면 할 수록 화질이 깨짐
#png도 압축은 있는데 손상이 없도록 함
# fill here


import os
#os.getcwd()#현재 경로 확인
#os.chdir('C:\\Users\\ASUS\\Desktop\\home\\2DGP-DRILL-02')#경로 변경
#경로 변경할 때 \ 두개 써야함
#print(os.listdir()) #현재 경로에서 무슨 파일 있는 지 확인 가능

#img = load_image('character.png')#이미지 불러오기
#프로그램이 돌아가는 경로에서 이미지를 불러올 수 있음
'''
img.draw_now(400,300)#이미지를 어디다가 그릴지
img.draw_now(200,300)
img.draw_now(200,400)#여러개도 가능
'''

# for x in range(0,9):
#     for y in range(0,7):
#         img.draw_now(x*100,y*100)

# delay(5) #5초 대기

# clear_canvas()#캔버스 지우기


# close_canvas()#캔버스 끄기


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

delay(2)

close_canvas()
