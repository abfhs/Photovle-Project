# Photovle
[22조] 충남/충북 1반 3조

## 프로젝트 소개
* **AI 모델을 활용해 학습데이터 수집과 전처리를 위한 레이블링을 한번에!**
  * 개발기간 : 2022/04/11 ~ 2022/05/11
  * 팀원 : 라효진, 김정빈, 김종호, 강준영, 유영재

## 개발 배경
 * 컴퓨터 비전이 많은 발전이 진행됨에 따라, 영상처리에 대한 관심이 날로가면 늘어나는 추세이다. 그동안 우리는 카메라를 단순 이미지, 동영상 출력 장치로 사용했지만 이제는 AI기술을 통해 출력 장치를 넘어 눈으로 보는 세상을 컴퓨터가 인식할 수 있게 되었다. 
이런 컴퓨터의 눈으로 보는 **‘인식’** 그 뒷 배경에는 방대한 양의 학습 데이터가 요구되며 학습 데이터는 레이블링을 통한 전처리 작업이 필수적이다. 하지만 방대한 양의 학습 데이터를 모으기 위해 일일이 수집하는 것에도 한계와 어려움이 있으며, 또 수집한 데이터에서 레이블링 작업을 수행하기 위해서 많은 시간과 돈이 지출되게 된다. 
그래서 우리는 이런 번거롭고 시간과 돈이 많이드는 작업을 AI 모델을 활용해 자동으로 **데이터 수집부터 레이블링 작업까지 한번에** 할 수 있으면 어떨까 라는 취지에서 본 프로젝트를 진행하게 되었다.

   * 모델링을 수행하기 위해 다량의 데이터와 레이블링을 통한 전처리가 요구됨
   * AI 모델을 활용해 영상 처리를 위한 데이터 수집부터 레이블링을 한번에 수행
   * 1000개의 클래스, 1400만장의 데이터셋으로 학습된 우수한 성능의 vgg16 모델 기반
   * Davis 2016 데이터셋으로 학습하여 AI모델 구성  
 
 ## 프로젝트 구성
  * Image Segmentation
  * 마이페이지
  * 게시판
  * 회원가입
  * 로그인
  <img src="https://user-images.githubusercontent.com/96154466/167673485-4acddd69-092d-480f-8c60-68693987524f.JPG" width="700" />

## Model Architecture

`2-TIER`

 <img src="https://user-images.githubusercontent.com/96154466/167673659-a8fdfac3-9af8-4f44-a510-57a1577da999.png" width="700" />

## UI/UX
 `[UI/UX]` https://xd.adobe.com/view/dd45f359-f2b2-4ed7-951a-3f72daa98b6c-8816/
 
* Login Page
  <p align="left">
   <img src="https://user-images.githubusercontent.com/96154466/167606249-fa7dfe30-db61-4a0f-8207-909f32737160.png" width="500" />
  </p>
 
* Labeling Page
  <p align="left">
   <img src="https://user-images.githubusercontent.com/96154466/167606385-7932bbf0-2eb8-415f-a5e8-8a90cfa0e956.png" width="450" />
  </p>

## DataBase
  * ERD
   
   <img src="https://user-images.githubusercontent.com/96154466/167610598-3399d9dc-e13d-4cab-be72-f3b9ef851b56.JPG" width="600" />
   
   
## 모델 사용절차
 * Sequence

 <img src="https://user-images.githubusercontent.com/96154466/167678738-b578d886-6ac8-4c60-9b85-5267570ccdd8.JPG" width="700" />
 
 * DEMO
 <p align="justify">
   <img src="https://user-images.githubusercontent.com/96154466/167675641-bfb41422-defd-448e-86c5-445b24004118.png" width="500" />
 
   https://user-images.githubusercontent.com/96154466/167680112-3dc76882-3950-4e44-a1c6-a4e4ba7abc47.mp4
 </p>

## 개발 환경   
* Front
<p align="left">
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/></a>&nbsp 
  <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>&nbsp
</p>

* Back End
<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/></a>&nbsp 
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/flask-green.svg?style=for-the-badge&logo=flask&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/ngrok-brown.svg?style=for-the-badge&logo=ngrok&logoColor=white"/></a>&nbsp
</p>

* Management tool & others
<p align="left">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/></a>&nbsp
  <img src="https://img.shields.io/badge/Notion-green.svg?style=for-the-badge&logo=notion&logoColor=white"/></a>&nbsp
</p>
