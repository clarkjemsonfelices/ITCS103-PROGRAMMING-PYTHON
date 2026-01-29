def average(list):
	total = 0
	
	for number in list:
		total += number
	average = total / len(list)
	return average

def compare(word, average):
	length = len(word)
	
	if length == average:
		print(f"The length of the word '{word}' is equal to the average")
	elif length > average:
		print(f"The length of the word '{word}' is greater than the average")
	elif length < average:
		print(f"The length of the word '{word}' is less than the average")
	
nums = []

word = input("Enter a word: ")

for n in range(1, len(word) + 1, 1):
	num = int(input(f"Enter number ({n}): "))
	nums.append(num)

print(nums)
print(f"The length of the word is {len(word)}")
print(f"The average of the numbers is {average(nums)}")
compare(word, average(nums))