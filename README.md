# Musinsa user churn prediction with review data


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

### 1. 자세 분석 및 경고 <br>
- 어깨의 각도가 지정한 각도 이하가 되면 경고음과 함께 자세를 바로하라는 경고창이 띄워집니다. <br>
확인 버튼을 사용자가 직접 클릭할 때까지 지속되어 자세를 바로잡을 수 있도록 합니다.
<img src="https://github.com/NaYeojung/Posture-analysis-program/assets/107746494/af75e580-34ab-4621-8b56-63febe18edf7" width="480px"><br>
- 화면 오른쪽 아래 record 버튼을 클릭하면 자세가 안좋았던 시간들의 기록을 볼 수 있습니다.
<img src="https://github.com/NaYeojung/Posture-analysis-program/assets/107746494/52d34a27-e9c4-4a23-8286-a5dbe0e51503" width="480px">

### 2. 스트레칭 알림 및 영상 제공 <br>
- 10분이 경과할 떄마다 화면에 스트레칭 권고글이 띄워집니다.<br>
사용자는 이를 보고 시간이 경과했음을 알고 스트레칭의 필요성을 꺠달을 수 있습니다.
<img src="https://github.com/NaYeojung/Posture-analysis-program/assets/107746494/1b2b7779-60bc-417b-b1d2-b401220a9529" width="480px"><br>
- 화면 오른쪽 아래 stretching 버튼을 클릭하면 다양한 스트레칭 영상 목록이 나옵니다.<br>
- 원하는 영상의 숫자 키보드를 통해 영상을 재생할 수 있습니다.<br>
 자세 분석 중간에 따로 인터넷으로 검색하지 않아도 스트레칭을 하고 분석을 다시 진행할 수 있습니다.from sklearn.preprocessing import LabelEncoder
<img src="https://github.com/NaYeojung/Posture-analysis-program/assets/107746494/aaa2d155-9da8-46d1-8597-086995c9416d" width="480px">

### 3. 자세 분석 그래프 생성
- 프로그램을 종료하면 처음 입력한 이름을 토대로 json 파일과 그래프 이미지를 생성합니다.
- json 파일에는 이름과 날짜, 분석을 진행한 시간, 경고받은 시간 등을 기록해둡니다.
- 그래프에는 자세 분석을 진행한 시간과 평균 어깨 각도를 계산해 보여주고, 시간 경과에 따른 어꺠 각도 변화 및 자세가 안좋았던 시기를 그래프에 표시해 한눈에 보여줍니다.
<img src="https://github.com/NaYeojung/Posture-analysis-program/assets/107746494/39372ba4-db43-44fe-8f8c-5b3f81bddbe3" width="550px">
