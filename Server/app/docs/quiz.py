from app.docs import parameter

OX_QUIZ_GET = {
    'tags': ['Quiz'],
    'description': '유적지에 해당하는 ox 퀴즈 정보륿 불러옵니다.',
    'parameters': [
        parameter('area', '유적지 이름', 'url')
    ],
    'responses': {
        '200': {
            'description': 'OX Quiz 조회 성공',
            'examples': {
                '': {
                    'question': '구 개척리에서 강제로 후에...',
                    'OXAnswer': 'X'
                }
            }
        }
    }
}

MULTIPLE_QUIZ_GET = {
    'tags': ['Quiz'],
    'description': '유적지에 해당하는 multiple choice question 퀴즈 정보를 불러옵니다.',
    'parameters': [
        parameter('area', '유적지 이름', 'url')
    ],
    'responses': {
        '200': {
            'description': '유적지 좌표 정보 조회 성공',
            'examples': {
                '': {
                    "question": '신한촌 내 한인들의 자체 단체인 ( ) 은/는 일제와 러시아의 탄압을 피해...',
                    "answer_word": '권업회',
                    "NumberOfAnswer": '1',
                    "WordList": '신민회, 의열단, 권업회, 광복회'
                }
            }
        },
    }
}