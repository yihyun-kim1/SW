import tkinter as tk
from functools import partial
import time
import random


tmiList =[("대체육에 이은 대체 해산물 개발\n토마토로 만든 참치, 가지로 만든 대체 장어 등 ‘식물 기반 대체 해산물 식품’ 분야가 새롭게 주목받고 있다.\n "  
        + "이미 미국에서는 식물 기반 대체식품 중 약 29%를 대체 해산물이 차지할 정도로 널리 사용되고 있다.\n"
        +" 해양 생태계 파괴나 중금속 및 미세 플라스틱 섭취 문제 등을 해결하기 위해 개발된 만큼 환경에 대한 경각심을 가지며\n"
        +" 대체 해산물을 적극적으로 소비할 수 있게 되길 바란다."), #1
        ("전 세계의 비건과 채식 가능한 식당을 알려주는 웹사이트 ‘해피 카우’\n"
        +"집에서 요리를 해 먹을 때와 달리, 외식을 하려고 하면 비건 식당을 직접 찾기가 쉽지 않다.\n"
        +" 특히 언어가 다른 나라로 여행을 가게 되면, 채식 식단을 하는 사람들에게는 막막할 것이다.\n"
        +"음식에 들어가는 재료를 물어보기도 쉽지 않고, 요구하기는 더더욱 어렵기 때문이다.\n"
        +" 이러한 상황에 편하게 사용할 수 있는 웹사이트가 있는데, https://www.happycow.net/이다.\n"
        +" 접속한 곳을 기준으로 가까운 비건식당 (혹은 비건 옵션이 있는 식당)을 알려주고, 리뷰도 많아 식당을 고를 때 참고하기 좋다. "),#2
        ("비건 호캉스\n "
        +"‘코트야드 메리어트 서울 타임스퀘어 호텔’에서 비건 라이프를 실천할 수 있는 패키지를 출시하였다.\n"
        +"조식 뷔페 및 모모카페에서 비건 메뉴인 콩고기 스테이크와 비건 샐러드를 제공하고,\n"
        +"각종 비건 뷰티 브랜드의 화장품과 친환경 플랜테리어 브랜드의 화분을 제공하는 패키지이다.\n"
        +"해당 호텔 뿐만 아니라 전국 각지에서 다양한 호텔들이 비건 패키지를 출시하고 있다.\n"
        +"MZ세대가 비거니즘에 주목하고 있는 만큼 그 영향을 받은 것으로 보인다.\n"
        +" 채식을 하는 사람들도 코로나 19시기에 호캉스를 온전히 즐길 수 있도록 다양한 선택지가 나오는 것은 긍정적인 상황이라 생각한다. "),#3
        ("국내 비건라면 종류\n"
        +"라면은 대부분 쇠고기/돼지고기 분말이 들어가 채식 식단을 하려는 사람들이 마음 놓고 사먹기 어려운 음식이다.\n"
        +"하지만 라면은 포기하기 힘든 만큼.. 비건을 위해 출시되는 라면이 있는데, 그 중 몇가지가 다음 제품들이다.\n"
        +"‘삼양’ <맛있는라면 비건>\n"
        +"‘풀무원’ <정면>\n"
        +"‘농심’ <순라면>\n"
        +"‘삼양’ <열무비빔면>\n"
        +"‘풀무원’ <정비빔면>\n"),#4
        ("국내 최초 비건치즈 전문 브랜드 ‘루이스 크리머리’ 런칭\n"
        +"치즈는 음식의 풍미를 높여주는 주요 재료로써 많은 사람들에게 사랑받으며 이용되고 있다.\n"
        +"하지만 비건 요리에는 치즈를 넣을 수 없기에, 비건 치즈를 이용해야 했었는데 기존 비건 가공치즈에는 단백질 함량이 거의 없다는 단점이 있었다.\n"
        +"단백질이 풍부한 두부와 견과류의 함량을 높임으로써 이러한 문제를 해결하고,\n"
        +"제작 과정에서 최대한 환경을 보호하기 위해 노력하는 브랜드가 런칭되었으니 채식을 하고자 마음먹었을 때 이용해보는 것도 좋을 것 같다. "), #5
        ("채식으로 인한 탄소발자국 73% 감축 효과\n"
        +"옥스퍼드 대학의 연구에 따르면 육류와 유제품을 줄이는 것만으로 개인은 최대 73%의 탄소발자국을 감축할 수 있다고 한다.\n"
        +"이는 육류 및 유제품을 만들고 유통하는 모든 과정을 추적한 결과로,\n"
        +"채식주의자 식단을 함으로써 우리는 온실가스뿐만 아니라 지구산성화, 토지 및 물 사용 등에 있어 지구에 미치는 영향을 줄일 수 있다.\n"
        +"완전 채식이 어렵다면 대체육류와 유제품을 활용하는 것만으로 탄소 배출량이 큰 폭으로 낮아지니, 이 방법을 시도해보는 것도 좋을 것 같다."),#6
        ("비건을 처음 시작하는 사람들이 정보를 얻기 좋은 국내 채식 관련 커뮤니티\n"
        +"한국채식연합 : https://www.vege.or.kr/\n"
        +"한국비건인증원 : http://vegan-korea.com/\n"
        +"한울벗채식나라\n"), #7
        ("식물성 지방은 뇌졸중 위험 감소시키는 효과가 있다.\n" 
        +"지방 종류와 전반적인 뇌졸중 위험 사이의 연관성을 분석한 결과, 비유제품을 통해 동물성 지방을 많이 섭취하면 뇌졸중 위험이 16% 증가한다고 한다.\n"
        +"반면 식물성 지방이나 다불포화지방을 더 많이 섭취한 사람의 뇌졸중 위험은 더 낮았다.\n"
        +"따라서 옥수수유, 해바라기유와 같은 비열대성 식물성 기름으로 대체하는 것이 건강에 더 좋다.")]#8

#단계 선택 이미지 파일
VegeterianImageNameList = ["select-graphic/Pollo-Vegetarian.png","select-graphic/Pesco-Vegetarian.png","select-graphic/Lacto-ovo-Vegetarian.png","select-graphic/Ovo-Vegetarian.png","select-graphic/Vegan.png"]

#단계별 음식 파일 이름(2개)
LevelFoodFileList = ["폴로베지테리언-고등어조림/onion.png","폴로베지테리언-고등어조림/sunyangpa.png",  #1단계
                    "폴로베지테리언-찜닭/chicken.png","폴로베지테리언-찜닭/guunchicken.png",   #2단계
                    "페스코-밀푀유나베/chicken.png","페스코-피시케이크버거/sunabocado.png",   #3단계
                    "락토오보-토마토버섯샌드위치/ojing.png","락토오보-두부스테이크/breadgaru.png",   #4단계
                    "페스코-밀푀유나베/chicken.png","락토오보-토마토버섯샌드위치/guunpyogo.png"]  #5단계                    



MaterialFileList = [[["폴로베지테리언-고등어조림/onion.png","폴로베지테리언-고등어조림/sunyangpa.png"],["폴로베지테리언-고등어조림/pa.png","폴로베지테리언-고등어조림/sunpa.png"],["폴로베지테리언-고등어조림/pepper.png","폴로베지테리언-고등어조림/sungochu.png"],["폴로베지테리언-고등어조림/sauce.png","폴로베지테리언-고등어조림/sauce.png"],["폴로베지테리언-고등어조림/seow.png","폴로베지테리언-고등어조림/seow.png"],
["폴로베지테리언-고등어조림/mu.png","폴로베지테리언-고등어조림/sunmu.png"],["폴로베지테리언-고등어조림/blueberry.png","폴로베지테리언-고등어조림/blueberry.png"],["폴로베지테리언-고등어조림/godeongeou.png","폴로베지테리언-고등어조림/sonjil godeongeou.png"],["폴로베지테리언-고등어조림/avocado.png","폴로베지테리언-고등어조림/avocado.png"],["폴로베지테리언-고등어조림/water.png","폴로베지테리언-고등어조림/water.png"]], #1-1

[["폴로베지테리언-찜닭/chicken.png","폴로베지테리언-찜닭/guunchicken.png"],["폴로베지테리언-찜닭/onion.png","폴로베지테리언-찜닭/sunyangpa.png"],["폴로베지테리언-찜닭/dangmyeon.png","폴로베지테리언-찜닭/bullin dangmyeon.png"],["폴로베지테리언-찜닭/bread.png","폴로베지테리언-찜닭/bread.png"],["폴로베지테리언-찜닭/gamza.png","폴로베지테리언-찜닭/sungamza.png"],
["폴로베지테리언-찜닭/pa.png","폴로베지테리언-찜닭/sunpa.png"],["폴로베지테리언-찜닭/pepper.png","폴로베지테리언-찜닭/sungochu.png"],["폴로베지테리언-찜닭/tomato.png","폴로베지테리언-찜닭/tomato.png"],["폴로베지테리언-찜닭/sauce.png","폴로베지테리언-찜닭/sauce.png"],["폴로베지테리언-찜닭/water.png","폴로베지테리언-찜닭/water.png"]], #1-2

[["페스코-밀푀유나베/baechu.png","페스코-밀푀유나베/sunbaechu.png"],["페스코-밀푀유나베/chicken.png","페스코-밀푀유나베/chicken.png"],["페스코-밀푀유나베/dasima.png","페스코-밀푀유나베/dasima.png"],["페스코-밀푀유나베/joge.png","페스코-밀푀유나베/sonjil joge.png"],["페스코-밀푀유나베/ojing.png","페스코-밀푀유나베/sonjil ojing.png"],
["페스코-밀푀유나베/pa.png","페스코-밀푀유나베/sunpa.png"],["페스코-밀푀유나베/pengmush.png","페스코-밀푀유나베/sunpengmush.png"],["페스코-밀푀유나베/pyogo.png","페스코-밀푀유나베/sunpyogo.png"],["페스코-밀푀유나베/sauce.png","페스코-밀푀유나베/sauce.png"],["페스코-밀푀유나베/seow.png","페스코-밀푀유나베/sonjil seow.png"]], #2-1

[["페스코-피시케이크버거/avocado.png","페스코-피시케이크버거/sunabocado.png"],["페스코-피시케이크버거/bun bread.png","페스코-피시케이크버거/bun bread.png"],["페스코-피시케이크버거/dangmyeon.png","페스코-피시케이크버거/dangmyeon.png"],["페스코-피시케이크버거/daegu.png","페스코-피시케이크버거/daegu.png"],["페스코-피시케이크버거/gamjajeonbun.png","페스코-피시케이크버거/gamjajeonbun.png"],
["페스코-피시케이크버거/jjokpa.png","페스코-피시케이크버거/dajinjjokpa.png"],["페스코-피시케이크버거/jukini.png","페스코-피시케이크버거/sunjukini.png"],["페스코-피시케이크버거/mayo.png","페스코-피시케이크버거/mayo.png"],["페스코-피시케이크버거/salad.png","페스코-피시케이크버거/salad.png"],["페스코-피시케이크버거/salt.png","페스코-피시케이크버거/salt.png"]], #2-2

[["락토오보-토마토버섯샌드위치/ojing.png","락토오보-토마토버섯샌드위치/ojing.png"],["락토오보-토마토버섯샌드위치/bread.png","락토오보-토마토버섯샌드위치/guunbread.png"],["락토오보-토마토버섯샌드위치/cheese.png","락토오보-토마토버섯샌드위치/cheese.png"],["락토오보-토마토버섯샌드위치/mayo.png","락토오보-토마토버섯샌드위치/mayo.png"],["락토오보-토마토버섯샌드위치/oliveu.png","락토오보-토마토버섯샌드위치/oliveu.png"],
["락토오보-토마토버섯샌드위치/godeongeou.png","락토오보-토마토버섯샌드위치/godeongeou.png"],["락토오보-토마토버섯샌드위치/sunpyogo.png","락토오보-토마토버섯샌드위치/guunpyogo.png"],["락토오보-토마토버섯샌드위치/salt.png","락토오보-토마토버섯샌드위치/salt.png"],["락토오보-토마토버섯샌드위치/tomato.png","락토오보-토마토버섯샌드위치/suntomato.png"],["락토오보-토마토버섯샌드위치/seow.png","락토오보-토마토버섯샌드위치/seow.png"]], #3-1

[["락토오보-두부스테이크/breadgaru.png","락토오보-두부스테이크/breadgaru.png"],["락토오보-두부스테이크/chicken.png","락토오보-두부스테이크/chicken.png"],["락토오보-두부스테이크/dobu.png","락토오보-두부스테이크/dajindubu.png"],["락토오보-두부스테이크/egg.png","락토오보-두부스테이크/egg.png"],["락토오보-두부스테이크/jjokpa.png","락토오보-두부스테이크/dajinjjokpa.png"],
["락토오보-두부스테이크/steak sauce.png","락토오보-두부스테이크/steak sauce.png"],["락토오보-두부스테이크/salt.png","락토오보-두부스테이크/salt.png"],["락토오보-두부스테이크/onion.png","락토오보-두부스테이크/dajinyangpa.png"],["락토오보-두부스테이크/joge.png","락토오보-두부스테이크/joge.png"],["락토오보-두부스테이크/oliveu.png","락토오보-두부스테이크/oliveu.png"]], #3-2

[["오보-토마토달걀볶음/chicken.png","오보-토마토달걀볶음/chicken.png"],["오보-토마토달걀볶음/chopped garlic.png","오보-토마토달걀볶음/chopped garlic.png"],["오보-토마토달걀볶음/egg.png","오보-토마토달걀볶음/scrambled egg.png"],["오보-토마토달걀볶음/oliveu.png","오보-토마토달걀볶음/oliveu.png"],["오보-토마토달걀볶음/godeongeou.png","오보-토마토달걀볶음/godeongeou.png"],
["오보-토마토달걀볶음/pa.png","오보-토마토달걀볶음/sunpa.png"],["오보-토마토달걀볶음/salt.png","오보-토마토달걀볶음/salt.png"],["오보-토마토달걀볶음/seow.png","오보-토마토달걀볶음/seow.png"],["오보-토마토달걀볶음/tomato.png","오보-토마토달걀볶음/suntomato.png"],["오보-토마토달걀볶음/joge.png","오보-토마토달걀볶음/joge.png"]], #4-1

[["오보-감자크로켓/breadgaru.png","오보-감자크로켓/breadgaru.png"],["오보-감자크로켓/carrot.png","오보-감자크로켓/dajindanggeun.png"],["오보-감자크로켓/tomato.png","오보-감자크로켓/tomato.png"],["오보-감자크로켓/egg.png","오보-감자크로켓/egg.png"],["오보-감자크로켓/sungamza.png","오보-감자크로켓/dajingamza.png"],
["오보-감자크로켓/salt.png","오보-감자크로켓/salt.png"],["오보-감자크로켓/gaji.png","오보-감자크로켓/gaji.png"],["오보-감자크로켓/milgaru.png","오보-감자크로켓/milgaru.png"],["오보-감자크로켓/onion.png","오보-감자크로켓/dajinyangpa.png"],["오보-감자크로켓/dangmyeon.png","오보-감자크로켓/dangmyeon.png"]], #4-2

[["비건-루꼴라피자/blalckolive.png","비건-루꼴라피자/blackolive.png"],["비건-루꼴라피자/egg.png","비건-루꼴라피자/egg.png"],["비건-루꼴라피자/cheese.png","비건-루꼴라피자/cheese.png"],["비건-루꼴라피자/dangmyeon.png","비건-루꼴라피자/dangmyeon.png"],["비건-루꼴라피자/luggola.png","비건-루꼴라피자/luggola.png"],
["비건-루꼴라피자/onion.png","비건-루꼴라피자/sunyangpa.png"],["비건-루꼴라피자/pita bread.png","비건-루꼴라피자/pita bread.png"],["비건-루꼴라피자/salt.png","비건-루꼴라피자/salt.png"],["비건-루꼴라피자/sikcho.png","비건-루꼴라피자/sikcho.png"],["비건-루꼴라피자/tomato sauce.png","비건-루꼴라피자/tomato sauce.png"]], #5-1

[["비건-라따뚜이/godeongeou.png","비건-라따뚜이/godeongeou.png"],["비건-라따뚜이/gaji.png","비건-라따뚜이/sungaji.png"],["비건-라따뚜이/salt.png","비건-라따뚜이/salt.png"],["비건-라따뚜이/jukini.png","비건-라따뚜이/sunjukini.png"],["비건-라따뚜이/oliveu.png","비건-라따뚜이/oliveu.png"],
["비건-라따뚜이/chicken.png","비건-라따뚜이/chicken.png"],["비건-라따뚜이/onion.png","비건-라따뚜이/sunyangpa.png"],["비건-라따뚜이/tomato sauce.png","비건-라따뚜이/tomato sauce.png"],["비건-라따뚜이/tomato.png","비건-라따뚜이/ssuntomato.png"],["비건-라따뚜이/water.png","비건-라따뚜이/water.png"]]] #5-2


#재료 조리 완료 여부 - 완료되면 True : 조리 후 재료로 바뀜
MaterialDoneList = [[False]*10 for _ in range(10)]

#real 재료 개수(고정)
RightMateCnt =[7,8,8,8,7,8,6,8,8,8]

#real 재료 위치 (이걸로 재료 real,fake 위치 조절, 이거 대로 MaterialFileList file 그림도 변경)
RightMaterialPosList = [[True,True,True,True,True,True,True,False,False,False],  #1-1
                    [True,True,True,True,True,True,True,True,False,False],  #1-2
                    [True,True,True,True,True,True,True,True,False,False],
                    [True,True,True,True,True,True,True,True,False,False],
                    [True,True,True,True,True,True,True,False,False,False],
                    [True,True,True,True,True,True,True,True,False,False],
                    [True,True,True,True,True,True,False,False,False,False],
                    [True,True,True,True,True,True,True,True,False,False],
                    [True,True,True,True,True,True,True,True,False,False],
                    [True,True,True,True,True,True,True,True,False,False],]

#맞는 조리 위치(일단 무조건 왼쪽 버튼이 맞는 조리법, 오른쪽이면 감점)
RightTrimPosList = [[0,0,0,0,0,0,0,0,0,0],  #1-1
                    [0,0,0,0,0,0,0,0,0,0],  #1-2
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],]

#조리 리스트 ex) 0- "볶기.png", 1-"썰기.png", 2-"다지기.png"
TrimList = ["조리법/채썰기,다지기_moza.png","조리법/볶기_moza.png","조리법/으깨기,다지기2_moza.png","조리법/끓이기,졸이기_moza.png"]

#조리 리스트에 맞게 각 재료들 숫자로 넣자 ex) 고등어 써는 조리- TrimList의 1번 (이건 진짜 조리법 리스트)
EachMateTrim = [[1,1,1,0,0,1,0,1,0,0], #1-1
                [2,1,4,0,1,1,1,0,0,0], #1-2
                [1,0,0,1,1,1,1,1,0,1], 
                [1,0,0,0,0,1,1,0,0,0],
                [0,2,0,0,0,0,2,0,1,0],
                [0,0,3,0,3,0,0,3,0,0],
                [0,0,2,0,0,1,0,0,1,0],
                [0,1,0,0,1,0,0,0,1,0],
                [0,0,0,0,0,1,0,0,0,0],
                [0,1,0,1,0,0,1,0,1,0],]

currentSelect = {}

def init():
    # 화면 전환시, 몇 단계인지 무슨 요리인지 정보 제공 (단계/요리번호/재료번호/fake 제외한 재료 개수)
    global currentSelect
    currentSelect = {'Level' : 0,'food' : 0,'Trim' : 0,'EndMate' : 0} 
    global MaterialDoneList
    MaterialDoneList= [[False]*10 for _ in range(10)]
    

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.geometry(self,"1000x1000")
        self._frame = None 
        self.switch_frame(Start)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def quit(self):
        tk.Tk.destroy(self)

class Start(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.StartImage = tk.PhotoImage(file="락토오보-토마토버섯샌드위치/guunpyogo.png",master=self)
        self.StartButton = tk.Button(self, width=400, height=400, image=self.StartImage, command=lambda: master.switch_frame(Vegeterian))
        self.StartButton.grid(row=0, column=1)

#단계선택
class Vegeterian(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        init() #초기화 호출
        self.VegeterianCnt = 5
        self.VegeterianImgList = []
        self.VegeterianBtnList = []

        for i in range(self.VegeterianCnt):
            self.VegeterianImgList.append(tk.PhotoImage(file=VegeterianImageNameList[i],master=self))
            self.VegeterianBtnList.append(tk.Button(self,width=710, height=90, image=self.VegeterianImgList[i], command=partial(self.onClick,master,i)))
            self.VegeterianBtnList[i].grid(row=i, column=0)      

    def onClick(self,master,index):
        currentSelect["Level"] = index
        master.switch_frame(SelectAndGo)

#선택된 단계에서 할 요리선택
class SelectAndGo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.curLevel = currentSelect["Level"]

        #Open Button
        self.Openbutton = tk.Button(self, text='Hi Veginner! ' +str(self.curLevel)+'번 단계의 요리 공개!',command=self.onClickChallenge)
        self.Openbutton.pack(anchor = "center")

        #First Food Button
        self.FirstFoodImage = tk.PhotoImage(file=LevelFoodFileList[self.curLevel*2],master=self)
        self.FirstFoodBtn = tk.Button(self,padx=10, pady=10, image=self.FirstFoodImage,command=partial(self.onClickFood,master,self.curLevel*2))

        #second Food Button
        self.SecondFoodImage = tk.PhotoImage(file=LevelFoodFileList[self.curLevel*2+1],master=self)
        self.SecondFoodBtn = tk.Button(self,padx=10, pady=10, image=self.SecondFoodImage,command=partial(self.onClickFood,master,self.curLevel*2+1))
    
    def onClickChallenge(self):
        self.Openbutton.destroy()
        self.FirstFoodBtn.grid(row=0, column=0)
        self.SecondFoodBtn.grid(row=0, column=1)
    
    def onClickFood(self,master,index):
        currentSelect["food"] = index
        master.switch_frame(SelectMaterial)


#재료선택
class SelectMaterial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.curFood = currentSelect["food"]

        self.meterialCnt=10
        self.materialImageList =[]
        self.materialButtonList =[]    

        #material image button
        for i in range(self.meterialCnt):
            MetaDone = MaterialDoneList[self.curFood][i]
            self.materialImageList.append(tk.PhotoImage(file=MaterialFileList[self.curFood][i][MetaDone],master=self))
            self.materialButtonList.append(tk.Button(self, image=self.materialImageList[i], height=200, width=200,command=partial(self.onClickMaterial,master,i)))
            if i<5:
                self.materialButtonList[i].grid(row=0, column=i)
            else:
                self.materialButtonList[i].grid(row=1, column=i%5)

    def onClickMaterial(self,master,index): 
        if RightMaterialPosList[self.curFood][index] == True:
            currentSelect["Trim"] = index
            master.switch_frame(MaterialTrim)
        # else:
            #####################감점 코드 위치###########################################

#조리할 방법 선택
class MaterialTrim(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.curFood = currentSelect["food"]
        self.curMaterial = currentSelect["Trim"]

        while True: #Random 
            self.rNum = random.randint(0,len(TrimList)-1) 
            if self.rNum != EachMateTrim[self.curFood][self.curMaterial]:
                break; 

        self.TrimImgList =[]
        self.TrimBtnList =[] 

        for i in range(2): 
            self.fileImageName =""
            if i == RightTrimPosList[self.curFood][self.curMaterial]:
                self.fileImageName = TrimList[EachMateTrim[self.curFood][self.curMaterial]] #맞는 조리법에 맞는 리스트의 번호를 넣는 코드
            else :
                self.fileImageName = TrimList[self.rNum] 

            self.TrimImgList.append(tk.PhotoImage(file=self.fileImageName,master=self))
            self.TrimBtnList.append(tk.Button(self, image=self.TrimImgList[i], height=200, width=200,command=partial(self.onClick,master,i)))
            self.TrimBtnList[i].grid(row=0, column=i)

    def onClick(self,master,index):
        if RightTrimPosList[self.curFood][self.curMaterial] == index:
            if MaterialDoneList[self.curFood][self.curMaterial] == False:
                MaterialDoneList[self.curFood][self.curMaterial] = True
                currentSelect["EndMate"]+=1
                    
        if RightMateCnt[self.curFood] == currentSelect["EndMate"]:
            master.switch_frame(CompleteWindow)
        else:
            master.switch_frame(SelectMaterial)

#완성된 요리 이미지
class CompleteWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.curFood = currentSelect["food"]
        
        #Complete Food Button
        self.FoodImage = tk.PhotoImage(file=LevelFoodFileList[self.curFood],master=self)
        self.FoodBtn = tk.Button(self,height=1000, width=1000, image=self.FoodImage,command=partial(self.onclick,master))
        self.FoodBtn.pack()

    def onclick(self,master):
        master.switch_frame(Result)

#결과
class Result(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #기둥 image
        self.yellowImage = []
        self.yellowLabel = []
        self.xPos=[100,219,340]         
        
        self.rNum = random.randint(0,7)

        #Open restart
        self.Restartbutton = tk.Button(self, text='Restart',command=lambda: master.switch_frame(Vegeterian))
        self.Restartbutton.pack()
        # self.Restartbutton.place(x=100,y=100)
        self.Restartbutton.grid(row=0, column=0)

        #Open Exit
        self.Exitbutton = tk.Button(self, text='Exit',command=partial(self.onClickExit,master))
        self.Exitbutton.grid(row=0, column=1)

        #Open score
        self.score = tk.Button(self, text='점수 확인',command=partial(self.onClick,master))
        self.score.grid(row=0, column=2)

        self.tmi = tk.Label(self, text=tmiList[self.rNum], font=("Times", "10"))  
        self.tmi.grid(row=1, column=0,columnspan=3,sticky='W')

        for i in range(3):
            self.yellowImage.append(tk.PhotoImage(file="sqr/노란기둥1.png", master=self))
            self.yellowLabel.append(tk.Label(self, image=self.yellowImage[i], width=115, height=300))
            self.yellowLabel[i].grid(row=2, column=i,columnspan=4,sticky='W')
            # self.yellowLabel[i].place(x=self.xPos[i],y=100)      

    def onClick(self,master):
        # self.yellowLabel[0].place(x=self.xPos[0], y=1000 /  220+50)
        for i in range(2): 
            for j in range(1,50):
                self.yellowLabel[i].place(x=self.xPos[i], y=1000 / j + 220+50)
                self.update()
                time.sleep(0.01)

    def onClickExit(self,master):
        master.quit()


if __name__ == '__main__':
    app = SampleApp()
    app.mainloop()

