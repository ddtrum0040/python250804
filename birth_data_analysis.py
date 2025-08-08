import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 경로 (예시: 'birth_data.csv')
file_path = 'birth_data.csv'

# 데이터 읽기
df = pd.read_csv(file_path)

# 데이터 클랜징
# 1. 결측치 제거
df = df.dropna()

# 2. 숫자형 컬럼 타입 변환
df['출생아수'] = pd.to_numeric(df['출생아수'], errors='coerce')
df['합계출산율'] = pd.to_numeric(df['합계출산율'], errors='coerce')

# 3. 다시 결측치 제거 (변환 후)
df = df.dropna()

# 데이터 분석 예시
print("연도별 출생아수 통계:")
print(df['출생아수'].describe())

print("\n연도별 합계출산율 통계:")
print(df['합계출산율'].describe())

# 시각화
plt.figure(figsize=(10,5))
plt.plot(df['연도'], df['출생아수'], label='출생아수')
plt.plot(df['연도'], df['합계출산율']*100000, label='합계출산율(확대)')
plt.xlabel('연도')
plt.ylabel('값')
plt.title('대한민국 출생아수 및 합계출산율 추이')
plt.legend()
plt.grid(True)
plt.show()