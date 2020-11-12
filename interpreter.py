environment = {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
			"define": lambda name, value: environment.update({name: value})}

def find_val(value):
	if value in environment:
		return environment[value]
	else:
		return value

def eval_(code):
	if isinstance(code, list):
		return find_val(code[0])(*[eval_(arg) for arg in code[1:]])
	else:
		return find_val(code)

def parse(tokens):
	if tokens == []:
		return
	curr = tokens.pop(0)
	if curr == "(":
		ast = []
		while tokens[0] != ")":
			ast.append(parse(tokens))
		tokens.pop(0); return ast
	elif curr == ")":
		print("SyntaxError: Unexpected \")\"")
	else:
		try: return int(curr)
		except ValueError:
			try: return float(curr)
			except ValueError: return str(curr)

while True:
	response = input("> ").replace("(", " ( ").replace(")", " ) ")
	tokens = response.split()
	as_a_tree = parse(tokens)
	if (result := eval_(as_a_tree)) is not None:
		print(result)