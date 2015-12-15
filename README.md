The first input line contains 1 &le; <i>n</i> &le; 10<sup>3</sup> items and 
capacity 0 &le; <i>W</i> &le; 2&times;10<sup>6</sup>.
Each of <i>n</i> successive input lines contains each item's cost (0 &le; <i>c<sub>i</sub></i> &le; 2&times;10<sup>6</sup>) and weight (0 &le; <i>w<sub>i</sub></i> &le; 2&times;10<sup>6</sup>). <i>n</i>,  <i>W</i>, <i>c<sub>i</sub></i>, and <i>w<sub>i</sub></i> are integers.
Output the maximum value of items' parts that fit into the knapsack (items can be cut into pieces, with their cost and weight diminishing proportionately) with 3 floating point precision.


Given a non-empty string <i>s</i> no longer than 10<sup>3</sup> symbols, build an optimal prefix-free code.
The first output line shows different <i>k</i> letters that are in the string, and the encoded string's length.
The next <i>k</i> lines show letters' codes in "letter: code" format. The last line shows the encoded string.


По данной непустой строке s длины не более 104, состоящей из строчных букв латинского алфавита, 
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке, 
и размер получившейся закодированной строки. 
В следующих k строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.


<b>Sample Input 1:</b>

a

<b>Sample Output 1:</b>

1 1

a: 0

0
