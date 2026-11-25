# agent-handoff-kit

**English** · [한국어](README.ko.md)

Stop in Claude Code today and pick up in Codex or OMP (oh-my-pi) tomorrow. The kit gives all three tools the same work rules and a blank `HANDOFF.md` for your project. You or your agent write down what happened and what to do next. No chat collection or memory server is involved.

## Try it without changing your settings

From the repository root on macOS or Linux, run the installer with `sh` and Python 3 in a temporary home:

```sh
demo_home=$(mktemp -d)
HOME="$demo_home" sh install.sh --lang en
HOME="$demo_home" sh install.sh --lang en --check
```

It installs four files:

- `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, and `~/.omp/agent/AGENTS.md`: copies of the [English work rules](templates/minimal/en/rules.md).
- `~/.config/my-ai-memory/templates/HANDOFF.md`: the blank [handoff template](templates/minimal/en/HANDOFF.md).

To install in your own home, run `sh install.sh --lang en`. For Korean, use `--lang ko`. **Omitting `--lang` still selects Korean**, as in earlier versions. Use the same language for `--check`: it reports missing or different files without creating or changing anything.

Changing the language flag does not replace your existing files. Installation stops if a target differs or is a link. To keep custom settings, skip the installer and copy only the rules you want from the [English](templates/minimal/en/rules.md) or [Korean](templates/minimal/rules.md) version. The installer does not install the coding tools or any packages.

## Hand off a task

1. From your project root, if `HANDOFF.md` does not exist, run `cp -n ~/.config/my-ai-memory/templates/HANDOFF.md ./HANDOFF.md`. If it exists, use it as is.
2. Before stopping, write what you verified in `State` and a concrete first step in `Next`. For example: **State:** the sample CSV sums to 42. **Next:** check that empty input sums to 0.
3. Open a fresh session in the same project and ask: **“Read `HANDOFF.md` and continue from `Next`.”**

Try the [Claude Code → Codex CSV walkthrough (English / 한국어)](examples/csv/README.md) without using a real project or personal data. Keep account details and customer data out of your handoffs: the kit does not write the notes or scan them for secrets.

## License

The scripts, work rules, templates, and documentation are [MIT licensed](LICENSE). Keep the copyright and license notice when redistributing them.
