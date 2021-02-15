# keypress
키보드에 있는 키 자동 입력을 위한 모듈입니다. 키 입력부터 ctrl+c,v,a 등 간단한 기능 몇가지를 구현해놓았으며, 자동 복붙 및 화면전환 기능을 이용하여 업무 자동화 스크립트를 만드는데에 도움이 될 것입니다.
  
## 1. 모듈 정보
파이썬 표준 라이브러리를 이용하기때문에 따로 설치할 라이브러리는 없습니다.
  
## 2. 사용방법
해당 모듈을 사용할 파이썬 파일에서 import 합니다. 
  
```py
import keypress
```
모듈 내 KEY 딕셔너리에 있는 값들만 사용이 가능합니다.
  
* key_up, key_down
```py
keypress.key_down('window')
keypress.key_up('window')
```
window 키를 눌렀다가 떼는 기능
  
* key_press
```py
keypress.key_press('window')
```
window 키를 눌렀다가 떼는 기능으로 위의 key_up, key_down 예시와 동일한 기능
  
* twice_key_up, twice_key_down
```py
keypress.twice_key_down('control','f')
keypress.key_up('control')
keypress.key_up('f')
```
twice 함수는 키 두개를 입력할 때 사용합니다.
위의 예시는 ctrl + f 기능을 이용할때 사용하며 키를 누른(down) 후에는 떼어줘야(up)합니다.
  
* 그외 함수 (ctrl+c, alt+f4 등)
```py
keypress.ctrl_c()
keypress.alt_tab()
```
위의 예시처럼 사용하면 됩니다.
