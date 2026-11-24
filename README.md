# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/khaliefk/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/khaliefk/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for the [make.fun bounty](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4): the funniest one-line farewell a phone could say as its battery hits 1 percent.

## What it does

`main.py` writes a single line to `/output/entry.txt`: a phone at 1 percent battery, speaking in its own voice, telling its owner not to mourn the phone but the 4,000 photos it never backed up. The line is 107 characters, one line, no trailing newline issues, and the program checks its own output by reading the file back before it exits.

## Run it

```sh
python3 main.py
```

It prints the line and the character count, and writes the same text to `/output/entry.txt`.
