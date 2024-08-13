# 리뷰데이터를 기반으로 한 고객 이탈 예측 모델링


## 설치 모듈

```sh
import pandas as pd
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import ADASYN
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import precision_recall_curve, f1_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

```

## 프로젝트 설명

<img src="https://github.com/NaYeojung/musinsa-churn-prediction/blob/88438f5918f60a79ecad3308bfe777b18ce321fd/asset/1.png">

### 1. 데이터셋 구성 <br>
1) 리뷰 데이터 크롤링 (1061만 건)
2) 계층적 샘플링 후 추가 리뷰 크롤링
3) 상품 상세 정보 크롤링
4) 패션톡 게시판 이용 크롤링
5) 리뷰 데이터와 상품, 게시판 데이터 결합
<img src="https://github.com/NaYeojung/musinsa-churn-prediction/blob/88438f5918f60a79ecad3308bfe777b18ce321fd/asset/2.png" width="480px">

### 2. 모델링 <br>
1) 모델 성능 평가
   - LightGBM 선정
2) 최적화
   - 오버생플링
   - 그리드서치
   - 하이퍼파라미터 조정
<img src="https://github.com/NaYeojung/musinsa-churn-prediction/blob/88438f5918f60a79ecad3308bfe777b18ce321fd/asset/3.png" width="480px">

### 3. 가설 검증 및 맞춤형 전략 기획 <br>
가설 1. 리뷰의 품질이 높을수록 고객의 이탈률이 낮을 것이다.<br>
가설 2. 패션톡을 사용하는 고객은 그렇지 않은 고객에 비해 이탈률이 낮을 것이다.
<img src="https://github.com/NaYeojung/musinsa-churn-prediction/blob/88438f5918f60a79ecad3308bfe777b18ce321fd/asset/4.png" width="480px">
