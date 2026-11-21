# TinyChess 4K — tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/DadayXz-code/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DadayXz-code/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original 0x88-board chess engine in one packed Python file
(`main.py`, 4,095 bytes — the 4,096-byte cap, 1 byte to spare).

## Design

Negamax alpha-beta + quiescence (captures/promotions, all evasions
when in check), transposition table, MVV-LVA ordering, iterative
deepening to a fixed node budget of 40,000 nodes/move —
deterministic (no clock, no unseeded randomness). Tapered PeSTO
(mg/eg) piece-square tables; endgame tables kept only for pawn
and king.

Perft verified on startpos, Kiwipete, pos3, pos4, pos5 (depth 1–3,
all exact); Zobrist keys consistent over 200 random move sequences;
mate-in-1 and win-the-queen tactics pass. Final packed engine:
trial 4W 1D 1L, Elo ~1,545.

## License

MIT — see `LICENSE`.
