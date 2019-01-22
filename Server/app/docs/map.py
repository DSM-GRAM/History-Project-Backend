from app.docs import parameter

MAP_GET = {
    'tags': ['Map'],
    'description': '구글 지도에서의 유적지 좌표를 보여줍니다.',
    'parameters': [
        parameter('history_site_code', '각 유적지의 코드', 'url'),
    ],
    'responses': {
        '200': {
            'description': '유적지 좌표 정보 조회 성공',
            'examples': {
                '': {
                    'lat': 13.57,
                    'lng': 12.34
                }
            }
        },
        '204': {
            'description': '없는 유적지'
        }
    }
}
