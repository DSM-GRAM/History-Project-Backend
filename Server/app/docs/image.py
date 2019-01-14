from app.docs import parameter

IMAGE_GET = {
    'tags': ['Image'],
    'description': '이미지 조회',
    'parameters': [
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
