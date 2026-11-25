"""Install or check the standalone handoff kit."""
import argparse
import os
from pathlib import Path
import stat
import sys


FILES = {
    "rules.md": (".claude/CLAUDE.md", ".codex/AGENTS.md", ".omp/agent/AGENTS.md"),
    "HANDOFF.md": (".config/my-ai-memory/templates/HANDOFF.md",),
}

MESSAGES = {
    "ko": {
        "directory": "디렉터리가 아니거나 링크인 경로",
        "regular": "독립된 일반 파일이 아닌 경로",
        "missing_source": "원본 없음",
        "empty_source": "빈 원본",
        "conflict": "기존 내용이 다름 — 보존",
        "missing": "설치되지 않음",
        "created": "설치함",
        "ready": "작업 규칙과 HANDOFF 양식이 준비됐습니다.",
        "home": "HOME은 기존 디렉터리의 절대 경로여야 합니다.",
    },
    "en": {
        "directory": "Not a directory, or a symbolic link",
        "regular": "Not a regular file, or has multiple links",
        "missing_source": "Source file not found",
        "empty_source": "Source file is empty",
        "conflict": "Existing file differs; left unchanged",
        "missing": "Not installed",
        "created": "Installed",
        "ready": "Work rules and handoff template are ready.",
        "home": "HOME must be an absolute path to an existing directory.",
    },
}


def regular_file(base, relative, messages):
    """Return an existing ordinary file, or None for a missing path below base."""
    path = base
    for part in Path(relative).parts[:-1]:
        path = path / part
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            return None
        if not stat.S_ISDIR(mode):
            raise ValueError(f"{messages['directory']}: {path}")
    path = base / relative
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"{messages['regular']}: {path}")
    return path


def install(root, home, *, check, lang):
    messages = MESSAGES[lang]
    template_dir = Path("templates/minimal")
    if lang != "ko":
        template_dir /= lang
    pending = []
    for name, targets in FILES.items():
        relative = template_dir / name
        source = regular_file(root, relative, messages)
        if source is None:
            raise FileNotFoundError(f"{messages['missing_source']}: {root / relative}")
        data = source.read_bytes()
        if not data.strip():
            raise OSError(f"{messages['empty_source']}: {source}")
        for target in targets:
            installed = regular_file(home, target, messages)
            if installed is None:
                pending.append((home / target, data))
                continue
            with installed.open("rb") as stream:
                if stream.read(len(data) + 1) != data:
                    raise ValueError(f"{messages['conflict']}: {installed}")
    for path, data in pending:
        if check:
            print(f"[MISSING] {messages['missing']}: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(data)
            print(f"[CREATED] {messages['created']}: {path}")
    if check and pending:
        return 1
    print(f"[OK] {messages['ready']}")
    return 0


def main():
    parser = argparse.ArgumentParser(prog="sh install.sh", allow_abbrev=False)
    parser.add_argument("--lang", choices=MESSAGES, default="ko",
                        help="template and message language / 설치 언어 (default: ko)")
    parser.add_argument("--check", action="store_true",
                        help="check without writing files / 파일을 수정하지 않고 점검")
    args = parser.parse_args()
    try:
        home = Path(os.environ.get("HOME", ""))
        if not home.is_absolute() or not home.is_dir():
            raise OSError(MESSAGES[args.lang]["home"])
        return install(Path(__file__).resolve().parents[1], home, check=args.check, lang=args.lang)
    except ValueError as exc:
        print(f"[CONFLICT] {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
