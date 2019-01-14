from app.docs import parameter

MAIN_GET = {
    'tags': ['Main'],
    'description': '메인 페이지에서 bla|usu 에 대한 3가지 장소 정보 나타냄',
    'parameters': [
        parameter('area', 'bla|usu', 'url')
    ],
    'responses': {
        '200': {
            'description': 'bla|usu 정보 조회 성공',
            'examples': {
                '': [
                    {
                        "historicalSiteName": '신한촌',
                        "historicalSiteLocation": '러시아, 블라디보스톡',
                        "historicalSiteImagePath": 'localhost/image/1'
                    },
                    {
                        "historicalSiteName": '라즈돌리노예 역',
                        "historicalSiteLocation": '러시아, 블라디보스톡',
                        "historicalSiteImagePath": 'localhost/image/2'
                    },
                    {
                        "historicalSiteName": '개척리',
                        "historicalSiteLocation": '러시아, 블라디보스톡',
                        "historicalSiteImagePath": 'localhost/image/3'
                    }
                ]
            }
        },
        '401': {
            'description': 'bla|usu 이외의 장소 호출 불가'
        }
    }
}

AREA_GET = {
    'tags': ['Main'],
    'description': '한 장소에 대한 구체적인 데이터 확인',
    'parameters': [
        parameter('area', 'bla|usu', 'url'),
        parameter('history_site_name', '장소 이름', 'url')
    ],
    'responses': {
        '200': {
            'description': '장소 정보 조회 성공',
            'examples': {
                '': {
                    "imagePath": 'localhost/image/1',
                    "location": '러시아, 블라디보스톡',
                    "text": '블라디보스토크에는 1870년....',
                    "extra": [
                        {
                            "extraName": '한인이주150주년기념비',
                            "extraImagePath": 'localhost/image/한인이주150주년기념비',
                            "extraLocation": '러시아, 블라디보스톡'
                        },
                        {
                            "extraName": '개척리(2018)',
                            "extraImagePath": 'localhost/image/개척리(2018)',
                            "extraLocation": '러시아, 블라디보스톡'
                        }
                    ],
                    "extraText": '1911년대 이후 ...',
                    "explain": '1860년대 후반 이후에는...'
                }
            }
        },
        '204': {
            'description': '존재하지 않는 장소'
        }
    }
}
