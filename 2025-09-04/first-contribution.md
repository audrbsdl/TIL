## Github 오픈소스에 기여하기

[여기](https://github.com/firstcontributions/first-contributions) 링크되어있는 Github 리포지토리를 통해 Github 오픈소스에 기여하는 전반적인 과정에 대해 학습해봅시다.

1. 리포지토리 포크(Fork)하기

Github 리포지토리 상단 메뉴에 Fork 버튼을 통하여 기여하고자 하는 리포지토리의 복사본을 내 계정 아래에 생성합니다.

2. 작업 환경에 클론(Clone)하기

이제 포크된 리포지토리를 내 컴퓨터에 복제합니다. `git clone 리포지토리-주소` 명령어를 사용하여 내 컴퓨터의 개발 환경에 리포지토리를 복제할 수 있습니다.

3. 브랜치(branch) 만들기

`git switch -c new-branch-name`을 통해 새로운 브랜치를 만들 수 있습니다.

4. 원하는 작업 후 커밋(Commit), 푸쉬(Push)하기

원하는 작업을 마쳤으면 커밋을 해야 합니다. 커밋을 하기 전에는 커밋할 변경사항들을 모두 스테이징 영역(Staging Area)에 추가(Add)해야 합니다. 이는 `git add 변경한-파일명.md`를 통해 추가할 수 있습니다.

이 후 `git commit -m "커밋 메시지"`를 실행하여 커밋을 마무리 합니다. 커밋된 변경사항은 로컬 리포지토리에는 반영되어 있으나, 원격 리포지토리에는 반영되어 있지 않습니다. 따라서 푸쉬(Push) 과정을 통해 변경사항을 공유하도록 합니다.

`git push -u origin current-branch-name`을 사용하면 현재 브랜치의 내용을 원격의 `origin` 브랜치에 반영하게 됩니다.

5. 풀 리퀘스트(Pull Request)

원격 리포지토리에 저장되어있는 서로 다른 브랜치를 병합하기 위해 풀 리퀘스트 과정을 거칩니다.

이는 Github의 "Compare & pull request"를 통해 진행할 수 있습니다.

풀 리퀘스트가 끝나면 권한이 있는 사용자가 변경사항을 병합할지 여부를 정하게 됩니다.

[실습 리포지토리](https://github.com/audrbsdl/first-contributions)