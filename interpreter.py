from copy import deepcopy

environment = {
			"+": lambda x, y: x + y,
			"-": lambda x, y: x - y,
			"*": lambda x, y: x * y,
			"/": lambda x, y: x / y,
			"display": print,
			"define": lambda name, value: environment.update({name: value}),
			"cons": lambda a, b: [a, b],
			"car": lambda pair: pair[0],
			"cdr": lambda pair: pair[1],
			"atom?": lambda obj: not isinstance(obj, list),
			"eq?": lambda a, b: a == b
}

class Procedure:
	def __init__(self, args, body):
		self.args = args
		self.body = body
	def __call__(self, *args):
		global environment
		before_call = deepcopy(environment)
		for name, val in dict(zip(self.args, args)).items():
			environment[name] = val
		result = eval_(self.body)
		environment = before_call
		return result

find_val = lambda value: environment.get(value, value)

def eval_(code):
	if isinstance(code, list):
		if code[0] == "lambda":
			return Procedure(code[1], code[2])
		elif code[0] == "if":
			return eval_(code[2]) if eval_(code[1]) else eval_(code[3])
		elif code[0] == "quote":
			return code[1]
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