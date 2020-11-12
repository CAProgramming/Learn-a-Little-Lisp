## Get ready for some more Lisp:

### Overview:
- `define`, `car`, `cdr`, and `cons`

`define` 

For variables:

```scheme
(define x 5)
(define y (+ 2 3 (* 4 5)))
```

For functions:

```scheme
(define (f x) (+ x 1))
(define (second-elem lst) (car (cdr lst)))
```

- `car`, `cdr`, and `cons`

### Today you'll learn these things:
- `lambda`, `quote` and `'`, `eval`, `cond`
- `atom?`, `null?`, `eq?`, `equal?`

`lambda`

- This constructs an anonymous function. What is an anonymous function, you ask?
- You're probably used to most functions in most programming languages being bound to names.
- For example, in Python:

```python
def f(x):
	return x + 1
```

- But what if a function didn't have to have a name?
- Anonymous functions are very useful because if you ever ha ve a function that you'll only use once or twice, and doesn't need a name, they can save you a lot of space. Here's an example in Lisp of a function that takes another function as input:

```scheme
(define (higher-order f) (f 1 2 3))
```

- This function is called higher_order because functions that can take other functions as inputs and return other functions are called higher-order functions. First-order functions would be functions that can't do this.
- Here's how you would use that function with `lambda`:

```scheme
> (higher-order (lambda (x y z) (* x y z)))
6
```

- Feel free to try this out! It can be a little tricky to grok at first but you'll get the hang of it.

`quote`

- Lisp interpreters read data objects one-by-one. For example, in the s-expression `(+ x 3)`, a Lisp interpreter would know that the variable x and 3 are summed. But what if I wanted to avoid evaluation of something? That's where `quote` comes in.

- If I wrote `(+ (quote x) 3)`, that wouldn't work. X is no longer a variable. It is another datatype called a symbol.
- Symbols are a little tricky to understand! Think of a symbol like this: a symbol is a data object that has two properties: a print name and a numerical constant associated with that string. Since there is an unique number for each symbol, symbols can be compared very effeciently with `eq?`. You can print it out with `display`.
- If you run `quote` on anything it will be treated as a symbol and it will bypass normal evaluation.
- If you want to save even more space you can use a single tickmark to indicate `quote`, like this: `'x`, instead of `quote x`.

`eval`

- This one is super cool but very unsafe!
- What if you wanted to take some symbols and evaluate them as Lisp code?
- This is like the opposite of `quote`. `quote` skips evaluation and `eval` forces evaluation.
- Here's an example:

```scheme
> (eval '(define x 5))
> x
5
```

- Try this out and have fun with it!

- Let's do some practical stuff now! Try to write a recursive factorial function.