from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import urllib.request
import json
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET

app = FastAPI()

origins = [
    "http://127.0.0.1:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-attractions")
def get_attractions(numOfRows: int = 3, pageNo: int = 3):
    api = 'http://apis.data.go.kr/6260000/FestivalService/getFestivalKr'
    key = unquote('Gg%2FHi0kpjUoJP9QXsLGog6VBlFhFUzNrEh4HsTR94EgqKCGltvfGO%2FzlAPiENmUYrtjNLCLn8b2OvqHnZOnejg%3D%3D')
    queryParams = '?' + urlencode({
        quote_plus('serviceKey'): key,
        quote_plus('returnType'): 'xml',
        quote_plus('numOfRows'): str(numOfRows),
        quote_plus('pageNo'): str(pageNo)
    })
    url = api + queryParams

    try:
        response = urllib.request.urlopen(url)
        text = response.read().decode('utf-8')

        # XML 응답 파싱
        root = ET.fromstring(text)

        # items 태그 안에 있는 항목들을 리스트로 변환
        items = []
        for item in root.findall('.//item'):
            item_dict = {child.tag: child.text for child in item}
            items.append(item_dict)

        return items

    except urllib.error.URLError as e:
        raise HTTPException(status_code=500, detail=f"서버에 연결할 수 없습니다: {e.reason}")

# FastAPI 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)