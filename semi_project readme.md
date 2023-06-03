# Read.md

[img](https://www.notion.so/img-f8b7bc10bd32464a880d996bf6b569e0?pvs=21)

<예시>

# 목차

1. 프로젝트 소개 
    1. 프로젝트 배경 및 목적
    2. 분석 아키텍쳐( Data lab,NaverBlog, BIGKinds(결과 미포함),Naver News, AWS Cloud
2. 배경 : 국내 주요 관광지 대비 특이지역 선정 후 sns데이터 바탕으로 선정지역 분석
3. 데이터 분석개요 : 기존 국내여행 수요 지역에 대한 변화 존재 할것이라는 가정. 
4. 분석
    - 관광객 수 파악
    - 지역별 카드사용데이터 수집
    - 블로그 크롤링
    - 뉴스 크롤링()/ 사용하지 않음 (코드)
    - 정보 습득 경로
        - 관광데이터 랩, Naver Blog,
    - 특이지역 선정
- 데이터 종합

특이지역 선정

---

---

# 📑 멀티 캠퍼스 세미프로젝트

Title 국내 주요 관광지 대비 특이 지역 선정 및 분석

| DAYS | TODO | 제출자 | CONTENTS |
| :--- | :--- | :---: | :--- |
| 05.03-05.04 | ☑ | 👩‍💻조원 전체 | 주제 선정 |
| 05.04-05.06 | ☑ | 조원 전체 | 데이터 수집 |
| 05.08 | ☑ | 선헌석 | DB제작 |
| 05.08 - 05.09 | ☑ | 김상휘,서정식 | Crawler제작 |
| 05.03-05.09 | ☑ | 김효진 | WBS 기획안 작성 Upload |
| 05.08 - 05.10 | ☑ | 김상휘,서정식 | Crawl 전처리 및 벡터화  (BOW)모델 |
| 05.11 - 05.15 | ☑ | 조원 전체 | 토픽 모델링 기법 선정 및 적용 |
| 05.11- 05.17| ☑ | 조원 전체 | 지역선정을 위한 데이터셋 재설정,군집화 방법 선택 |
| 05.15-05.17 |☑ | 조원 전체 | 군집별 데이터 분석 |
| 05.18 - 05.20  | ☑ | 김단비,최하연,서정식 | 자연어처리 TF-IDF , Word Embedding |
| 05.20 | ☑ | 최하연 | PPT 초안작성  |
| 05.22 - 05.24 | ☑ | 서정식,김효진 | 최종 발표 준비 |
| 05.24 | ☑ | 김효진 | 최종 발표 |

- **🧑‍🤝‍🧑 멤버 구성** :  @khj98khj, @321danb, @sangdduki , @xodidxkq ,@sjsic30, @hayeon977

- 소속 : 멀티캠퍼스 데이터분석&엔지니어 24회차
- **🖥️  프로젝트** 목표 : 국내 주요 관광지 대비 특이 지역 선정 및 특성 분석
    - 소셜 미디어 데이터를 활용
    - 
- 프로젝트 소개
    - 최근 국내 여행의 수요가 증가하여 기존 국내 여행 수요 지역에 대한 변화가 존재 했을 것이라는 기대와 달리 데이터 분석 결과 기존의 인기 관광 지역의 언급량 변화가 없음을 확인 후 그렇다면 일반적인 관광지역과 달리 특이성을 갖는 지역에 대해 분석해보기로함
    - 6명의 팀원들이 각자 데이터수집과 분석, 모델링, DB구축 및 자연어 처리 등의 역할을 나누어 수행
    

- **🕰️ 프로젝트 기간** : 2023-05-03 ~ 2023-05-24

- **📌** 과정
    - pandas로 데이터 전처리 및 전처리 자동화
    - MySQL 을 이용하여 데이터 DB에 저장
    - DB 생성 및 DB에 데이터 입력, 데이터 전처리, 데이터 분석 모델 수립 및 실행까지 모듈화 진행
- **🛠** 참고 리스트
- 저작권 , 라이선스 정보
    - 상세한 라이선스 정보 확인>

외부 리소스 정보

# 구조 분석

![스크린샷 2023-06-03 오후 5.23.16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5d923ae-49ff-4bc1-886c-daec5abc74dd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-06-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.23.16.png)

**[ 기본 정보 ]  <**예시 위 이미지>
대표 이미지 (프로젝트명과 매칭되는 대표이미지를 최상단에 두어 어떤 플젝인지 빠르게 예상하며 문서를 접할 수 있게 함)
제목
구분줄
뱃지 (통계적 정보를 가독성 좋게 나타냄)
프로젝트 간략 설명

**[ 추가 정보 ]**
오퍼레이션 GIF
목차

**[ 상세 정보 ]**
제목
구분줄
간략 설명

# **Table of Contents**

- 1.Library
    - python : 3.9.7
    - sklearn : 1.0.1
    - lightgbm : 3.1.1
    - tensorflow : 2.7
    - pandas : 1.3.5
    - numpy : 1.21.4
    - matplotlib.pyplot : 3.5.0
- 2.DataFrame
    - 독립변수 : 거리별 방문자 수 / 내비게이션 검색량
    - 종속변수 : 방문자 소비액
- 3.Project
    - 프로젝트 프로세스
        1. 데이터 수집
            
            거리별 방문자 수 , 내비 검색 건수, 지출액, 블로그 크롤링
            
            (한국관광 데이터랩,  네이버 블로그, 네이버뉴스, 빅카인즈)
            
        2. 전처리
            
            Pandas, MinMax Scalar, One-Hot encoding, Okt, Mecab
            
            scikit-learn과 tensorflow로 예측모델 구축
            
            - 머신러닝 Scikit-Learning
                
                TF-IDF vectorizer, Countervectorizer, K-means, LDA
                
            - 딥러닝 Tensorflow
                
                Tokenizer
                
                MySQL을 활용하여 AWS Cloud에 저장
                
                (AWS : 팀 프로젝트로 완성한 서비스를 서버로 제공할 때 Amazon EC2의 웹 서비스 인터페이스를 사용하여 인스턴스(서버)를 쉽고 간단하게 구현할 수 있으며, 높은 안정성으로 유연하게 서비스 관리를 할 수 있기 때문에 aws를 선택)
                
        
        1. EDA 및 데이터 시각화
            
            Matplotlib, Seaborn
            
        2. 예측모델을 통한 지역 예측
    
- 4.Analysis
    - [정량적 분석]
    
    : 지역별 방문자 수, 검색량 증가 등의 지표를 분석하여 트렌드 도출
    
    [정성적 분석]
    
    : 여행자 리뷰, 소셜 미디어 게시물 등을 분석하여 인기 증가의 원인과 관련된 의견 수집
    
    [머신러닝(Machine Learning)]
    
    LightGBM(250개의 지역의 상위 10위 지역 추출)
    
    : 모델의 일반화를 보여주는 잔차를 통해 이상 지역 탐지 
    
    [군집화, 토픽모델링]
    
    : K-means
    
    : LDA
    
- 5.Module
    - 구성 : sql.py, encoding.py, XGBR.py, LSTM_Module.py
    - 순서 : sql.py -> encoding.py -> XGBR.py or LSTM_Module.py
        - sql.py : SQLite로 DB 파일 만들고 데이터를 저장한 후 데이터테이블을 파이썬에 재추출
        - encoding.py : DB에서 추출한 데이터를 분석에 적합하도록 조작
        - LSTM_Module.py : LSTM 시계열 예측 분석(구글 코랩에서 분석되도록 세팅)
        - LGBM
        - LDA 단어 빈도수를 기반하여 DTM 단어 행렬을 생성
            - 토큰화 한 단어들의 counterverctorizer 사용하여 벡터화
        
- 6.Stacks
    
    Environment : Visual Studio Code
    
    Communication : Slack, Notion, Google Meet
    
- 7.Prerequisite (작성한 코드를 실행하기 전에 설치해야할 pakage나 의존성이 걸리는 문제)
    
    from konlpy.tag import Okt
    
    import numpy as np
    
    import pandas as pd
    
    from tensorflow import keras
    
    from tensorflow.keras.preprocessing.text import Tokenizer
    
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    
    from sklearn.model_selection import train_test_split
    
- 8.Files (중요한 코드 파일들 몇 개를 대상으로 해당 파일이 어떠한 역할을 하는 파일인지를 간단히 설명해주면 전반적인 맥락을 파악하기에 좋을 것 같아 추가해봄)
- 9.Usage (작성한 코드를 어떻게 실행해야 하는지에 대한 가이드 라인)

당면한 문제 >>> 나중에 추가하고 싶은 기능

## 의의 및 한계

의의

- 기존의 인기지역과 대비되는 특이 지역들은 지역적 특색 부족으로 인해 방문객의 유입이 일정한 패턴을 띄지 않는다는 결과를 도출할 수 있음 따라서 이러한 특이 지역들도 인기 관광 지역처럼 성장하기 위하여 유휴 공간 활성화, 지역 고유 문화 컨텐츠 구축 등의 방법을 활용하는 것을 제안
    - 언제 어디서든 찾기 쉬운 지역 관광 정보 제공
    - 유휴 공간의 활성화
    - 지역 고유의 문화 콘텐츠 구축
    - 잠재 관광수요 촉진을 위한 부가혜택

 

## 한계
