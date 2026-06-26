# Contributing

Thanks for improving this tiny ASCII terminal tool.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-diskmap.git
cd ascii-diskmap
python3 main.py .
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Prefer small readable functions over clever abstractions.
- Keep the TUI usable on small terminals.
- Avoid blocking operations inside the render loop when possible.
- Make filesystem errors non-fatal.

## Checks

Before opening a PR or committing changes, run:

```bash
python3 -m py_compile main.py
python3 main.py .
```

## Commit style

Use short imperative messages, for example:

- `Add size filter`
- `Fix terminal resize handling`
- `Document controls`
