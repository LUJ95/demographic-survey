# -*- coding: utf-8 -*-

API_key = 'API_KEY'
service = 'SearchFAQOfGUListService' 
gu_url = f'http://openapi.seoul.go.kr:8088/{API_key}/json/{service}/1/25'
gu_list = requests.get(gu_url).json()
print(gu_list)


{'SearchFAQOfGUListService': {'list_total_count': 25, 'RESULT': {'CODE': 'INFO-000', 'MESSAGE': '정상 처리되었습니다'}, 'row': [{'CODE': '300', 'CD_DESC': '종로구'}, {'CODE': '301', 'CD_DESC': '중구'}, {'CODE': '302', 'CD_DESC': '용산구'}, {'CODE': '303', 'CD_DESC': '성동구'}, {'CODE': '304', 'CD_DESC': '광진구'}, {'CODE': '305', 'CD_DESC': '동대문구'}, {'CODE': '306', 'CD_DESC': '중랑구'}, {'CODE': '307', 'CD_DESC': '성북구'}, {'CODE': '308', 'CD_DESC': '강북구'}, {'CODE': '309', 'CD_DESC': '도봉구'}, {'CODE': '310', 'CD_DESC': '노원구'}, {'CODE': '311', 'CD_DESC': '은평구'}, {'CODE': '312', 'CD_DESC': '서대문구'}, {'CODE': '313', 'CD_DESC': '마포구'}, {'CODE': '314', 'CD_DESC': '양천구'}, {'CODE': '315', 'CD_DESC': '강서구'}, {'CODE': '316', 'CD_DESC': '구로구'}, {'CODE': '317', 'CD_DESC': '금천구'}, {'CODE': '318', 'CD_DESC': '영등포구'}, {'CODE': '319', 'CD_DESC': '동작구'}, {'CODE': '320', 'CD_DESC': '관악구'}, {'CODE': '321', 'CD_DESC': '서초구'}, {'CODE': '322', 'CD_DESC': '강남구'}, {'CODE': '323', 'CD_DESC': '송파구'}, {'CODE': '324', 'CD_DESC': '강동구'}]}}

df_gu = pd.DataFrame(gu_list['SearchFAQOfGUListService']['row'])
df_gu

#%%

gu_json = []
vwolrd_key = 'AUTH KEY'
for gu in df_gu['CD_DESC']:
    url_vworld = f'https://api.vworld.kr/req/data?service=data&version=2.0&request=GetFeature&format=json&errorformat=json&size=10&page=1&data=LT_C_ADSIGG_INFO&attrfilter=sig_kor_nm:like:{gu}&columns=sig_cd,full_nm,sig_kor_nm,sig_eng_nm,ag_geom&geometry=true&attribute=true&key={vwolrd_key}&domain=https://localhost'
    result_dict = requests.get(url_vworld).json()
    gu_josn.append(result_dict)

gu_json

#%%

features = []
for gu_data in gu_json:  # gu_json 25개 구의 API 응답 데이터 리스트
   gu_name = gu_data['response']['result']['featureCollection']['features'][0]['properties']['sig_kor_nm']
   feature = {
       "type": "Feature",
       "id": gu_name,  # 구명을 id로 추가
       "geometry": gu_data['response']['result']['featureCollection']['features'][0]['geometry'],
       "properties": {
           "name": gu_name
       }
   }
   features.append(feature)

geojson_data = {
   "type": "FeatureCollection",
   "features": features
}

#%%

# GeoJSON 파일 저장
with open('../data/seoul_gu_boundaries.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson_data, f, ensure_ascii=False)

#%%

def style_function(feature):
    return {
        'opacity': 0.7,
        'weight': 1,
        'color': 'white',
        'fillOpacity': 0.2,
        'dashArray': '5, 5',
    }
# Folium 지도 객체 생성 및 GeoJson 레이어 추가
m = folium.Map(
    location=[37.5651, 126.98955], 
    zoom_start=11,
    tiles='cartodb dark_matter'
    )
folium.GeoJson(
    '../data/seoul_gu_boundaries.geojson',
    style_function=style_function
).add_to(m)