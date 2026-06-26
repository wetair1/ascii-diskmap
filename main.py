#!/usr/bin/env python3
import curses, os, sys


def dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path, onerror=lambda e: None):
        for f in files:
            try: total += os.path.getsize(os.path.join(root, f))
            except OSError: pass
    return total


def human(n):
    for u in ['B','KB','MB','GB','TB']:
        if n < 1024: return f'{n:.1f}{u}'
        n /= 1024
    return f'{n:.1f}PB'


def scan(path):
    rows = []
    for name in os.listdir(path):
        p = os.path.join(path, name)
        try:
            size = dir_size(p) if os.path.isdir(p) else os.path.getsize(p)
            rows.append((name + ('/' if os.path.isdir(p) else ''), size))
        except OSError:
            pass
    return sorted(rows, key=lambda x: x[1], reverse=True)


def draw(stdscr):
    curses.curs_set(0)
    path = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    rows = scan(path)
    maxv = max([s for _, s in rows] or [1])
    top = 0
    while True:
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(0, 2, f'ASCII DISKMAP: {path}  q quit  j/k scroll')
        for y, (name, size) in enumerate(rows[top:top+h-3], 2):
            bw = max(5, w-34)
            fill = int(bw * size / maxv)
            stdscr.addstr(y, 2, f'{human(size):>9} |' + '#' * fill + '-' * (bw-fill) + f'| {name[:20]}')
        ch = stdscr.getch()
        if ch in (ord('q'), ord('Q')): break
        if ch in (ord('j'), curses.KEY_DOWN): top = min(max(0, len(rows)-1), top+1)
        if ch in (ord('k'), curses.KEY_UP): top = max(0, top-1)


if __name__ == '__main__':
    curses.wrapper(draw)
