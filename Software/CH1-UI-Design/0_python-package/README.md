# Python 패키지와 가상환경

## Python 패키지
- **Python 패키지**: Python에서 특정 기능을 수행하는 코드의 묶음으로, 다양한 기능을 손쉽게 활용할 수 있도록 제공하는 라이브러리.
- 패키지는 때로 **라이브러리**, **프레임워크**라는 이름으로도 불린다.
- 예시:
  - **streamlit**: 웹 애플리케이션을 쉽게 만들 수 있는 프레임워크.
  - **pandas**: 데이터 분석과 조작을 위한 라이브러리.
  - **opencv**: 컴퓨터 비전과 이미지 처리를 위한 라이브러리.
  - **openai**: OpenAI의 API를 활용하기 위한 라이브러리.
- **Python 패키지 설치**:
  ```bash
  pip install 패키지이름
  ```

## 가상환경
- **가상환경**: Python 프로젝트마다 패키지 충돌을 방지하고 관리할 수 있도록 돕는 기능.
  > **생각해보기**  
  > 패키지 충돌이 발생하는 이유는 무엇일까?  

- **miniconda**: 가상환경과 패키지를 효율적으로 관리할 수 있도록 지원해주는 프로그램.
- **miniconda 설치법**:
  - **Windows**:
    1. [Miniconda 공식 사이트](https://docs.conda.io/en/latest/miniconda.html)에서 Windows용 Graphical Installer 다운로드.
    2. 다운로드한 설치 파일을 실행하고 안내에 따라 설치 진행.
    3. 설치 중 "Add Miniconda to PATH" 옵션을 선택하면 터미널에서 Conda를 쉽게 사용할 수 있음.
    4. 설치 완료 후, 시작 메뉴에서 "Anaconda Prompt"를 실행하고 `conda --version`을 입력하여 설치 확인.
  - **Mac**:
    1. [Miniconda 공식 사이트](https://docs.conda.io/en/latest/miniconda.html)에서 macOS용 Graphical Installer 다운로드.
    2. 다운로드한 `.pkg` 파일을 실행하고 안내에 따라 설치 진행.
    3. 설치 완료 후, 터미널을 열고 `conda --version`을 입력하여 설치 확인.