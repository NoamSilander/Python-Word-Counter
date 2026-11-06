## Word Counter
A word counter written in Python that lists word appearances in order of appearance.

Works by stripping all characters that aren't a letter by using `.isalpha()` method, then forming a dictionary out of them. I really tried making it sort them by frequency, but I'll leave that for a later date.

The repo includes a `text.txt` file I built the script off of. You can use whatever text file you'd like, as long as you pass its name into the `main()` function at the end of the script.

## How to Run
1. Paste your textfile into the **SAME WORKING DIRECTORY** as `word_counter.py`
2. Run `word_counter.py`

## Example
```
the: 8
cat: 4
sat: 2
on: 3
mat: 2
dog: 3
log: 1
a: 2
and: 2
met: 1
ran: 2
then: 1
too: 1
run: 1
said: 1
```