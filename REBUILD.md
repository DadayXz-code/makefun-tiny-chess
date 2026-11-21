# Tiny-chess rebuild (v8)

## Size
- main.py: 4089 bytes (limit 4096). Tree: 4089 + 1343 (README) + 1104 (LICENSE) + 58 (owner.json) + this file <= 8192.
- Written directly as readable Python in this session. No minify/pack/compress, no base64/lzma/exec-blob. Every line is plain Python.

## Perft (exact, all pass)
- startpos d1-4: 20, 400, 8902, 197281
- kiwipete d1-3: 48, 2039, 97862
- pos3 d1-4: 14, 191, 2812, 43238
- pos4 d1-4: 6, 264, 9467, 422333
- pos5 d1-3: 44, 1486, 62379

## Engine
- 120-square string board; negamax alpha-beta + quiescence (stand-pat, captures only, full evasions in check); MVV ordering; iterative deepening to a fixed 40000 nodes/move (deterministic, no clock/random). Node-budget abort via StopIteration keeps the previous depth's best move.
- Eval: material + piece-square tables (Michniewski simplified tables, base-36, half-board).
- Full rules: castling, en passant, all 4 promotions, mate/stalemate detection.
- Tests: scholar's mate Qxf7, back-rank Ra8#, free-queen Rxh1 all found; startpos eval 0; up-a-queen eval +/-870; root always returns a legal move. Time/move 1.0-2.9 s at 40000 nodes.

## Cut vs old engine (~1545 Elo)
- Dropped: transposition table, Zobrist hashing, repetition detection, tapered PeSTO (now single-phase PSTs), king endgame table.
- PSTs: pawn table kept; knight table shared by N/B/R/Q; king table kept. So B/R/Q use the knight centralisation table.
- Strength estimate: ~1300 Elo (above the 1154 floor). Main loss is no TT (~1-2 plies shallower); PST sharing costs a little.
