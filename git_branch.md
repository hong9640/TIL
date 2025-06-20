# Git Branch
- 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
- branch 장점:  
  - 독립된 개발 환경을 형성하기에 원본에 대한 안전
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능
  - 손쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있음
- 만약 상용 중인 서비스에 발생한 에러를 해결하려면?  
  - 브랜치를 통해 별도의 작업 공간을 만든다.
  - 브랜치에서 에러가 발생한 버전을 이전 버전으로 되돌리거나 삭제한다.
  - 해결되면 master에 전송한다.
- 기본 브랜치: 저장소의 초기상태, 배포 가능한 안정적인 코드
- 기준점: 다른 브랜치가 파생되는 기준점으로 사용됨
- 변경사항 통합: 코드리뷰와 테스트를 거쳐 master브랜치에 병합
- 명령어:  
  - git branch
  - git branch -r
  - git branch 브랜치 이름
  - git swich: 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어
- HEAD: 현재 브랜치나 commit을 가리키는 포인터(현재 내가 바라보는 위치)
- git switch 주의사항:  
  - 1. master브랜치와 feature브랜치가 존재.
  - 2. feature브랜치에서 생성한 article.txt가 master브랜치에도 존재하게 된다.
  - 3. git 브랜치는 독립적인 작업 공간을 갖지만 git이 관리하는 파일 트리에 제한됨
  - 4. git switch하기 전에 working directory의 모든 파일이 버전 관리 중인지 확인이 필요
- 깃 애드하고 switch하면 전거로 바뀜
- git log --oneline --all 전체 확인 가능
## git merge
-  두 브랜치를 하나로 병합
-  git branch -d hotfix 브랜치 지우기
-  git switch -c hotfix 바로 hotfix 생성하고 이동
-  git commit 하고 wq 하면 충돌 해결. 최종본으로 덮어씌어짐