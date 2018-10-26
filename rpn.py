#!/usr/bin/env python3

def calculate(arg):
	# stack for calculator
	stack = []

	# tokenize input
	tokens = arg.split()

	# process tokens
	for token in tokens:
		try: 
			value = int(token)
			stack.append(value)

def main():
	while True:
		calculate(input('rpn calc> '))

if __name__ == '__main__':
	main()
