letters, string_length = map(int, input().split())
codes = {code:letter for (letter,code) in [(x for x in input().split(": ")) for i in range(letters)] } 
code_to_parse = input()

answer = ""
temp = ""

for i in range(len(code_to_parse)):
	temp += code_to_parse[i]
	if temp in codes:
		answer += codes[temp]
		temp = ""
	else:
		continue

print(answer)
