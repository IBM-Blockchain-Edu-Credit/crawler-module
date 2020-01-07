# Crawler Module

> Kids A-Z Crawler Module

## 1. Prerequisite

1. Python 3.7 이상
2. 아래 코드 실행

```shell
python --version // 3.7 이상인지 확인
pip install requests pandas bs4 // 필요 라이브러리 설치
```

## 2. Getting Started

1. crawler.py 에서 다음 사항 수정
```python
st_date = "2019-11-01"
ed_date = "2020-01-01"
```

2. 실행
```
python crawler.py
```


3. JSON 구조

```json
{
'student_id': '241614401', 
'is_transferred': False, 
'is_shared': False, 
'current_writing_level_info': [],
'removed_at': None, 
'full_name': '전체 이름', 
'level': 'A', 
'earned_stars': '17080', 
'available_stars': '2805',
'most_recent': '65',
'homeroom_member_id': '5850109',
'homeroom_member_username': 'dodreamlibrary',
'homeroom_member_first_name': '이름', 
'homeroom_member_last_name': '성',
'activity_rollups_by_subject': 
    {
    'overview': 
        {
            'logins': 3, 
            'stars_earned': 1890, 
            'rocket_visits': 2,
            'timeInRocket': 5,
            'avatar_visits': 1,
            'timeInAvatar': 5,
            'timeLoggedIn': 31,
            'timeInIncentives': 9
        }, 
    'reading': 
        {'listen': 17, 'read': 14, 'worksheet': 0, 'quiz': 7, 'passed_quiz_count': 7, 'practice_recording': 0},
    'science': 
        {'quiz': 0, 'listen': 0, 'read': 0, 'passed_quiz_count': 0, 'practice_recording': 0, 'watch': 0, 'interactive_lesson': 0}, 
    'phonics': 
        {'read': 0, 'headsprout_episode': 0, 'benchmark_count': 0},
    'test':
        {'testlet': 0},
    'writing': 
        {'build_a_book': 0, 'process_writing': 0, 'write_your_way': 0},
    'vocabulary':
        {'vsc_game_practice': 0, 'vsc_game_assessment': 0}
    }
}
```