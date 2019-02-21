from app.docs import parameter

IMAGE_GET = {
    'tags': ['Image'],
    'description': '이미지 조회',
    'parameters': [
        parameter('area', '지역 이름', in_='url'),
        parameter('image_name', '사진 이름', in_='url')
    ],
    'responses': {
        '200': {
            'description': '이미지 조회 성공',
        },
        '204': {
            'description': '없는 이미지'
        }
    }
}

VR_IMAGE_GET = {
    'tags': ['Image'],
    'description': 'vr 이미지 조회',
    'parameters': [
        parameter('history_site_code', '각 유적지의 코드', in_='url')
    ],
    'responses': {
        '200': {
            'description': '이미지 조회 성공',
        },
        '204': {
            'description': '없는 이미지'
        }
    }
}
