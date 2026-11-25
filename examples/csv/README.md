# Claude Code → Codex: CSV 합계 / CSV total

한 세션은 합성 값 `17`과 `25`의 합계를 확인하고, 다음 세션은 빈 입력을 확인합니다. 두 세션이 공유할 것은 대화가 아니라 프로젝트의 `HANDOFF.md`입니다.

The first session checks the sum of `17` and `25`. A fresh session checks empty input. The only context passed from the first session to the second is the project's `HANDOFF.md`, not the chat history.

**준비 / Set up.** 저장소 루트에서 실행하세요. 실제 홈 설정은 바꾸지 않습니다. / From the repository root, run:

```sh
demo=$(mktemp -d)
cp examples/csv/total.py examples/csv/sample.csv "$demo/"
cp templates/minimal/HANDOFF.md "$demo/HANDOFF.md"
cd "$demo"
```

1. **Claude Code** — 이 폴더에서 새 세션을 열고 다음과 같이 요청하세요. / Open a new session here and ask:
   - 한국어: `python3 total.py < sample.csv`를 실행해 실제 출력을 `HANDOFF.md`의 `State`에 적어줘. `Next`에는 `python3 total.py < /dev/null`을 실행해 출력이 `0`인지 확인하라고 적고, 그 검사는 실행하지 마.
   - English: Run `python3 total.py < sample.csv` and record the observed output in `State` in `HANDOFF.md`. In `Next`, ask the next session to run `python3 total.py < /dev/null` and check for `0`. Leave that check unrun.
2. **Codex** — 같은 폴더에서 새 세션을 여세요. 앞 세션의 대화나 명령을 붙여넣지 마세요. / Start a fresh session in the same folder. Don't paste the previous chat or command.
   - 한국어: **`HANDOFF.md`를 읽고 `Next`부터 이어줘. 명령을 실행한 뒤 출력을 알려줘.**
   - English: **Read `HANDOFF.md` and continue from `Next`. Run the command and report its output.**

**확인 / What to look for:** `State`에는 `42`가 있어야 합니다. 새 세션이 파일을 읽고 빈 입력 명령을 실행하는지 확인하세요. 기대 출력은 `0`이고, 그 숫자를 말하는 것만으로는 실행 증거가 아닙니다. / Look for `42` in `State`, then watch the new session read the handoff and run the empty-input command. The expected output is `0`; quoting it without running the command doesn't count.
