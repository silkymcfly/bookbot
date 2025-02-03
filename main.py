def main():
	with open("books/frankenstein.txt") as f:
		contents = f.read()

	list = sort_list(char_count(contents))
	

	print("Begin report")
	print(f"Word count is {word_count(contents)}.")
	for i in list: 
		if i["letter"].isalpha() == True:
			print(f"The letter '{i["letter"]}' is found {i["count"]} times")
	print("End Report")

def word_count(document):
	words = document.split()
	return len(words)

def char_count(contents):
	count_dict = {}
	low_case_contents = contents.lower()
	for i in low_case_contents:
		if  i in count_dict:
			count_dict[i] += 1
		else:
			count_dict[i] = 1
	return count_dict

def sort_on(dict):
	return dict["count"]

def sort_list(count_dict):
	char_list = []
	for c, n in count_dict.items():
		char_list.append({"letter": c, "count": n})
	char_list.sort(reverse=True, key=sort_on)
	return char_list
	
main()
