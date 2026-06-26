# Architecture

ascii-diskmap is a small curses disk usage mapper built with only the Python standard library.

## Runtime flow

1. The app resolves the target directory from the CLI argument.
2. `scan()` lists direct children of the directory.
3. `dir_size()` recursively calculates sizes for folders.
4. Entries are sorted from largest to smallest.
5. The curses UI renders size bars and supports scrolling.

## Main parts

- `dir_size()` walks a directory and sums file sizes while ignoring inaccessible files.
- `human()` formats byte counts into readable units.
- `scan()` creates the sorted list of display rows.
- `draw()` owns keyboard input, scrolling and rendering.

## Design rules

- Keep dependencies at zero.
- Never crash on permission errors.
- Keep scanning logic separate from rendering.
- Use simple ASCII bars instead of heavy UI widgets.
- Prefer predictable output over background scanning complexity.
