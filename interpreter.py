from copy import deepcopy; import sys

environment = {
	"+": lambda x, y: x + y,
	"-": lambda x, y: x - y,
	"*": lambda x, y: x * y,
	"/": lambda x, y: x / y,
	"cons": lambda a, b: [a, b],
	"car": lambda l: l[0],
	"cdr": lambda l: l[1],
	"display": print,
	"define": lambda name, value: environment.update({name: value}),
	"atom?": lambda obj: not isinstance(obj, list),
	"eq?": lambda a, b: a == b,
	"null?": lambda l: l == []
}

class Procedure:
	def __init__(self, args, body):
		self.args = args
		self.body = body
	def __call__(self, *args):
		global environment
		before_call = deepcopy(environment)
		environment.update(dict(zip(self.args, args)))
		result = eval_(self.body)
		environment = before_call
		return result
	def __str__(self):
		return "#<procedure>"

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

def tokenize(expr):
	return expr.replace("(", " ( ").replace(")", " ) ").split()

def parse(tokens):
	if not tokens:
		return
	elif (curr := tokens.pop(0)) == "(":
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

def interpret(code):
	return eval_(parse(tokenize(code)))

if len(sys.argv) > 1:
	with open(sys.argv[1], "r") as script:
		expr, l, r = "", 0, 0

		for c in script.read():
			if c == "(": l += 1
			elif c == ")": r += 1
			expr += c

			if l == r and l != 0:
				interpret(expr)
				expr = ""
else:
	while True:
		if (result := interpret(input("> "))) is not None:
			print(result)