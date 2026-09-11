# Chunking Comparison

Tried 2 ways of splitting text on my 10 docs.

**fixed-size** (what the app actually uses) - just cuts every 800 chars,
160 overlap. doesnt care about sentences or headings at all.

**recursive** (chunking_recursive.py, just for testing) - tries to split
on paragraph breaks first, then lines, then sentences, then words. taught
in my chunking lesson. no overlap this time.

run it: `uv run python compare_chunking.py`

## results

fixed-size made 42 chunks total, avg ~700-770 chars each
recursive made 185 chunks, avg only ~110-170 chars each

recursive made like 4x more chunks and way smaller than the 800 target.
thats because in my docs every "Step" heading has a blank line before and
after it, so recursive splits the heading away from its own body text
right away.

## step 3 problem

checked if the "Step 3" heading and its body text stay in the same chunk:
- fixed-size: yes
- recursive: no, split into 2 separate pieces

honestly i expected recursive to fix the step 3 issue but it made it
worse, it seperated the heading completely from the actual instructions.

fixed-size is simpler and keeps headings with their body most of the time.
recursive never cuts mid sentence but makes a ton of tiny disconnected
pieces instead. a better fix would prob be merging small pieces back
together but i didnt build that, just comparing the 2 methods like taught.

app still uses fixed-size by default, this was just for learning.
