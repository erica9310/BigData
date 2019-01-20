import sys
import argparse #argument 입력값 분석시키는거
import requests #인터넷 연결요청
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO #Byte 단위로 인식하는 거 실행하려고

API_URL = 'https://kapi.kakao.com/v1/vision/product/detect'
MYAPP_KEY = '517663c74dff0388ee5fede47f65d73b'


#상품추출 함수 호출(인증)
def detect_product(image_url):
    headers = {'Authrization': 'KakapAK {}' .format(MYAPP_KEY)}
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers = headers, data = data)
        resp.raise_for_status()
        return resp.json()

    except Exception as e:
        print(str(e))
        sys.exit(0)
        # 인식 및 호출할 수 있는 값이 없을 때 그냥 종료 시켜달라고...에러메세지
    
def show_products(image_url):
    try:
        image_resp = requests.get(image_url)
        image_resp.raise_for_status()
        file_open = BytesIO(image_resp.content)
        image = Image.open(file_open)
    except Exception as e:
        print(str(e))
        sys.exit(0)
    draw = ImageDraw(image)
    


#상품추출 함수를 통해서 리턴 받은 이미지 처리

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'detect products')  #여러개의 이미지들을 따로 분석하게 하는 거 - 많이 사용함
    parser.add_argument('image_url', type=str, nargs='?', 
                        default = "http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/06.jpg",
                        help = '' #메세지 띄워주고 싶은거 있을때?
                        )
    args = parser.parse_args()
    print("ok-----1")
    
    
    #상품추출 함수
    detect_result = detect_product(args.image_url)
    print("ok-----2...")
    #Json 파일 형태로 넘겨진 데이터를 처리
    
    image = show_products(args.image_url, detection_result)