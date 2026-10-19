#!/bin/sh
# Decode the letter with decode.py under both keys and compare byte for byte with the files in
# data/: plaintext-<key>.txt (one stream) and plaintext-<key>-by-line.txt (one row per line).
cd "$(dirname "$0")/.." || exit 2
status=0
for k in whole-stream fit-only; do
    for mode in stream by-line; do
        if [ "$mode" = stream ]; then flag=""; want="data/plaintext-$k.txt"
        else flag="--by-line"; want="data/plaintext-$k-by-line.txt"; fi
        if python3 decode/decode.py "data/key-$k.json" data/signs.txt $flag | cmp -s - "$want"; then
            echo "$k $mode: identical to $want ($(wc -c < "$want") bytes)"
        else
            echo "$k $mode: DIFFERS from $want"
            status=1
        fi
    done
done
[ $status = 0 ] && echo "both keys reproduced exactly"
exit $status
