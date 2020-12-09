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

- Let's do some practical stuff now! Try to write a recursive factorial function.