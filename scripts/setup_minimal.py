"""Local-only minimal branch of setup_pc.sh. Nothing here discovers optional modules."""
import os
from pathlib import Path
import stat
import sys


FILES = {
    "templates/minimal/rules.md": (".claude/CLAUDE.md", ".codex/AGENTS.md", ".omp/agent/AGENTS.md"),
    "templates/minimal/HANDOFF.md": (".config/my-ai-memory/templates/HANDOFF.md",),
}


def regular_file(base, relative):
    """Return an existing ordinary file, or None for a missing path below base."""
    path = base
    for part in Path(relative).parts[:-1]:
        path = path / part
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            return None
        if not stat.S_ISDIR(mode):
            raise ValueError(f"디렉터리가 아니거나 링크인 경로: {path}")
    path = base / relative
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"독립된 일반 파일이 아닌 경로: {path}")
    return path


def install(root, home, *, check):
    pending = []
    for name, targets in FILES.items():
        source = regular_file(root, name)
        if source is None:
            raise FileNotFoundError(f"minimal 원본 없음: {root / name}")
        data = source.read_bytes()
        if not data.strip():
            raise OSError(f"빈 minimal 원본: {source}")
        for target in targets:
            installed = regular_file(home, target)
            if installed is None:
                pending.append((home / target, data))
                continue
            with installed.open("rb") as stream:
                if stream.read(len(data) + 1) != data:
                    raise ValueError(f"기존 내용이 다름 — 보존: {installed}")
    for path, data in pending:
        if check:
            print(f"[MISSING] {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(data)
            print(f"[CREATED] {path}")
    if check and pending:
        return 1
    print("[OK] minimal: 범용 작업 규칙과 HANDOFF 양식이 준비됐습니다.")
    return 0


def main():
    try:
        home = Path(os.environ.get("HOME", ""))
        if not home.is_absolute() or not home.is_dir():
            raise OSError("HOME은 기존 디렉터리의 절대 경로여야 합니다.")
        return install(Path(sys.argv[1]).resolve(strict=True), home, check=sys.argv[2] == "true")
    except ValueError as exc:
        print(f"[CONFLICT] {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
