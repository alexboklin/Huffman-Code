Given a non-empty string <i>s</i> no longer than 10<sup>4</sup> symbols, <b>encode.py</b> builds an optimal prefix-free code.
The first output line shows how many different <i>k</i> letters are in the string and the encoded string's length.
The next <i>k</i> lines show letters' codes in "letter: code" format. The last line shows the encoded string.

<b>Sample Input 1:</b>

a

<b>Sample Output 1:</b>

1 1

a: 0

0

<b>Sample Input 2:</b>

abacabad

<b>Sample Output 2:</b>

4 14

a: 0

b: 10

c: 110

d: 111

01001100100111

<b>decode.py</b>, in turn, restores the string by its prefix-free code. The first input line provides <i>k</i> difrerent letters that are in the string and <i>l</i>, the encoded string's length. The next <i>k</i> lines provide letters' prefix-free codes in "letter: code" format (the letters can go in arbitrary order). 
The output line shows string <i>s</i>.

<b>Sample Input 1:</b>

1 1

a: 0

0

<b>Sample Output 1:</b>

a

<b>Sample Input 2:</b>

4 14

a: 0

b: 10

c: 110

d: 111

01001100100111

<b>Sample Output 2:</b>

abacabad
