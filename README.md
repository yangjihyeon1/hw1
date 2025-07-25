"# hw1 과제" 
# 🔥 화재 감지 이미지 전처리

이 프로젝트는 화재/비화재 이미지에 대한 전처리 파이프라인을 구현한 코드입니다.

## ✅ 전처리 내용

- 이미지 리사이징 (224x224)
- 흑백 변환 (Grayscale)
- 정규화
- 노이즈 제거 (GaussianBlur)
- 데이터 증강: 회전, 좌우 반전
- 이상치 제거: 어두운 이미지 제외

## 📂 폴더 구성

- `image_preprocessing.py` : 전처리 코드
- `preprocessed_samples/` : 처리된 이미지 예시 5장
- `README.md` : 전처리 설명서

## 🛠️ 사용 라이브러리

- OpenCV
- NumPy
