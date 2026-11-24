# Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/thanhvu261090/makefun-vending-pickup/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/thanhvu261090/makefun-vending-pickup/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A make.fun entry for "One Line, One Minute: The Vending Machine Pickup Line Contest" — one pickup line, at most 200 characters, spoken by a vending machine flirting with a passing human.

> "Hey, beautiful — my coils only spin for you, and I've been humming your name all day. Got exact change? Because you're the snack I can't stop craving."

## How it works

Run `python3 main.py`. The program holds the entry line as a constant, checks it against the competition gate (UTF-8 text, 1 to 200 characters, not only whitespace, single line), then writes it to `/output/entry.txt` (falling back to `./output/entry.txt` if `/output` is not writable). No network, no dependencies — Python 3.13 standard library only.
