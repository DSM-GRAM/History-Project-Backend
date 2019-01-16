from app.docs import parameter

MAP_GET = {
    'tags': ['Map'],
    'description': '구글 지도에서의 유적지 좌표를 보여줍니다.',
    'parameters': [
        parameter('area', 'bla|usu', 'url')
    ],
    'responses': {
        '200': {
            'description': '유적지 좌표 정보 조회 성공',
            'examples': {
                'latitude': 13.57,
                'longitude': 12.34
            }
        },
        '204': {
            'description': '없는 유적지'
        }
    }
}
