![Image 1](https://toggl.com/blog/wp-content/uploads/2019/07/programming-explained-with-music-toggl.jpg)

## Code -> Data, or Data -> Code

`quote`

- Lisp interpreters read data objects one-by-one. For example, in the s-expression `(+ x 3)`, a Lisp interpreter would know that the variable x and the number 3 are summed. But what if I wanted to avoid evaluation of something? That's where `quote` comes in.

- If I wrote `(+ (quote x) 3)`, that wouldn't work. X is no longer a variable. It is another datatype called a symbol.
- Symbols are a little tricky to understand! Think of a symbol like this: a symbol is a data object that has two properties: a print name and a numerical constant associated with that string. Since there is an unique number for each symbol, symbols can be compared very effeciently with `eq?`. You can print it out with `display`.
- If you run `quote` on anything it will be treated as a symbol and it will bypass normal evaluation.
- If you want to save even more space you can use a single tickmark to indicate `quote`, like this: `'x`, instead of `quote x`.
- Summary: `quote` turns code into data (an s-expression) by skipping its evaluation.

`eval`

- This one is super cool, but very unsafe! (Arbitrary code execution can lead to you getting hacked. Yikes!)
- What if you wanted to take some symbols and evaluate them as Lisp code?
- This is like the opposite of `quote`. `quote` skips evaluation and `eval` forces evaluation.
- Here's an example:

```scheme
> (eval '(define x 5))
> x
5
```

- Summary: `eval` takes data (something quoted) and executes it as code.

![Image 2](https://lh3.googleusercontent.com/proxy/oZrDePo7fgYO0erTMO3YPrqG3GZP3-Uj5V0CfOWCd-ZKuYDOS4H0AKedzAjGlkJCuZvzGf4hrQOSwOuBcoAnmUEBZfQb6_W8q561kS-grhbFQj0FzU6Y9uvQ9HS7)

## Car, cdr, cons

- If you remember, the main datatype in Lisp is the list. Actually, lists with only two elements in them!
- You get the first one with `car`, and the second one with `cdr`. Here's an example:

```scheme
> (define x (cons (cons 1 2) (cons 3 4)))
> (car x)
(1 2)
> (cdr x)
(3 4)
> (cdr (cdr x))
(4)
> (car (cdr x))
3
```

- As you can see, Lisp makes lists with many elements possible through nesting the lists. A common function in Lisp is called `list`, which does this:

```scheme
> (define x (list 1 2 3 4 5))
> x
(1 2 3 4 5)
> (car x)
1
> (cdr x)
(2 3 4 5)
```

- Internally, `(list 1 2 3 4 5)` makes a list that actually looks like `(1 (2 (3 (4 (5 nil)))))`. Nifty!

- Let's implement these constructs:
`car`
`cdr`
`cons`
`quote`
`if`
`lambda`
`atom?`
`eq?`
`null?`
`display`
`quote`

- This might seem like a lot, but with Python it's actually pretty easy. I'll explain the constructs as we're implementing them.

## A tiny programming language

What we have done:
- `car`, `cdr`, `cons`, `define`, `if`, `lambda`, `atom?`, `eq?`, `null?` `display`, `quote`

- With just these constructs, we can
1. Make data structures
2. Define variables
3. Control the flow of a program
4. Make functions
5. Check an object's datatype
6. See if two objects are the same
7. Recursively go through lists
8. Print an object
9. Manipulate code as data: metaprogramming

- Let's celebrate by writing `map`, `filter`, and `reduce`.

- That's all you really need for a progamming language! All in under 100 lines of Python.
- I hope that you took something good away from this series of Lisp lessons. Farewell, fellow Lispers!