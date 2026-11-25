# agent-handoff-kit

[English](README.md) · **한국어**

Claude Code에서 멈춘 작업을 다음 날 Codex나 OMP(oh-my-pi)에서 이어갈 때, 세션 대화 대신 프로젝트의 `HANDOFF.md`를 읽는 방법입니다. 세 도구에 같은 작업 규칙을 설치하고, 프로젝트에는 직접 채울 인계 양식 하나를 둡니다. 대화를 수집하거나 기억 서버를 실행하지 않습니다.

## 설치 전에 써보기

macOS 또는 Linux에서 `sh`와 Python 3가 필요합니다. 이 폴더에서 다음을 실행하면 실제 홈을 바꾸지 않고 설치 결과를 볼 수 있습니다.

```sh
demo_home=$(mktemp -d)
HOME="$demo_home" sh install.sh --lang ko
HOME="$demo_home" sh install.sh --lang ko --check
```

설치되는 파일은 네 개입니다.

- `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.omp/agent/AGENTS.md`: `templates/minimal/rules.md`의 복사본
- `~/.config/my-ai-memory/templates/HANDOFF.md`: 빈 프로젝트 인계 양식

실제 홈에 적용하려면 `sh install.sh --lang ko`를 실행하세요. `--lang ko`를 생략해도 이전 버전처럼 한국어가 설치됩니다. 영어는 `--lang en`을 지정하세요. 점검할 때도 설치한 언어를 지정합니다. `--check`는 네 파일을 원본과 대조하고, 누락되거나 내용이 다르면 실패합니다. 파일을 만들거나 수정하지는 않습니다.

다른 언어로 다시 실행해도 기존 규칙이나 양식을 덮어쓰지 않습니다. 내용이 다르거나 대상이 링크면 설치를 중단합니다. 개인 설정을 유지하려면 설치 대신 [한국어 규칙](templates/minimal/rules.md) 또는 [영어 규칙](templates/minimal/en/rules.md)에서 필요한 항목만 직접 옮기세요. 이 키트는 도구 자체나 추가 패키지를 설치하지 않습니다.

## 작업 이어가기

1. 프로젝트 루트에 `HANDOFF.md`가 없다면 `cp -n ~/.config/my-ai-memory/templates/HANDOFF.md ./HANDOFF.md`로 만듭니다. 이미 있다면 복사를 건너뛰고 그 파일을 사용하세요.
2. 작업을 멈출 때 `State`에 직접 확인한 결과를, `Next`에 다음 사람이 열 파일이나 실행할 명령을 적습니다. 예: `State: CSV 예제에서 합계 42 확인`, `Next: 빈 CSV의 합계도 0인지 확인`.
3. 다음 세션을 같은 프로젝트에서 열고 **“HANDOFF.md를 읽고 Next부터 이어줘”**라고 요청합니다.

처음이라면 [Claude Code → Codex CSV 실습 (한국어 / English)](examples/csv/README.md)으로 같은 인계를 따라 해보세요. 실제 프로젝트나 개인 데이터는 필요하지 않습니다.

계정 정보나 고객 자료는 인계에 넣지 마세요. 이 키트는 인계 내용을 자동 작성하거나 비밀을 검사하지 않습니다.

## 라이선스

이 키트의 설치 스크립트, 작업 규칙, 인계 양식과 문서는 [MIT 라이선스](LICENSE)로 제공합니다. 복사하거나 재배포할 때는 저작권 표시와 라이선스 고지를 함께 보존하세요.
