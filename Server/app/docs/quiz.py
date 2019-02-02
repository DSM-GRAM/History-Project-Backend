from app.docs import parameter

QUIZ_GET = {
    'tags': ['Quiz'],
    'description': '유적지에 해당하는 퀴즈 정보륿 불러옵니다.',
    'parameters': [
        parameter('history_site_code', '각 유적지의 코드', 'url')
    ],
    'responses': {
        '200': {
            'description': '퀴즈 조회 성공',
            'examples': {
                '': {
                    "questionOX": ['치킨 먹고 싶냐?'],
                    "questionMultiple": ['어디 치킨 먹을까'],
                    "answerOX": ['O'],
                    "answerMultiple": ['교촌', '~'],
                    'wordOfNumber': [3, 4],
                    "wordList": [['교촌', 'bbq', '굽네']]
                }
            }
        }
    }
}
