![Lisp Logo](https://upload.wikimedia.org/wikipedia/commons/f/f4/Lisplogo.png)

## Lisp Time!

![Lisp Meme](https://external-preview.redd.it/q5w8a3gQviELV61GNJbZX_Kara5xxiRjlMAm7C4dwMY.jpg?auto=webp&s=cf7b79be2c23ad48335f497d9a04a60c326d0e51)

### History

#### Lisp + Scheme

#### Original vs. Modern Lisp
- The original Lisp was very simple and had fairly few rules.
- Modern Lisp implementations tend to have an abundance of features.
- In terms of simplicity and elegance, they are nowhere near the simplicity of the original Lisp.

#### A Solution: Scheme
- Scheme was created to embody the original simplicity of the first Lisp
- That's why we're using Scheme today, because it's ultimately much more elegant,
- And it's much easier to teach as well.
- In fact, Scheme used to be the language that most colleges used to teach programming with!
- MIT used to teach a great introductory course to programming in Scheme.
- The textbook they used was called the Structure and Interpretation of Computer Programs.
- That book is awesome! You should definitely read it sometime.
- Nowadays colleges just use Python or Java. Boo!

#### Factoids
- `.scm` is the file extension for a Scheme file
- I'll be referring to the language here as Lisp because this isn't just about teaching Scheme,
- It's about teaching you what all of the Lisps have in common, and why they are so powerful.
- We'll be using Sublime Text today, but you can use VSCode if you want.

#### S-expressions

![Parentheses!](https://i.redd.it/9gwghrz9rcs11.jpg)

- S-expressions are what define Lisp. This is what they look like.

```scheme
> (f 1 (g 2 3) 4)
```

```scheme
> (define (index lst ind)
    (if (zero? ind) lst
      (index (cdr lst) (- ind 1))))
```

```scheme
> (define (map f lst)
    (if (null? lst) lst
        (cons (f (car lst)) (map f (cdr lst)))))
> (map (lambda (x) (* x x)) (quote (5 6 7 8)))
(25 36 49 64)
```

- While languages like Java and Python use semicolons and line breaks to delimit separate statements, Lisp uses parentheses. Each interpreter knows that a statement is complete once the number of left parentheses is equal to the number of right parentheses. Count the number of parentheses for each statement above, and you'll see that the number of left and right ones are equal!

```scheme
> (define (collatz n)
    (cond
        ((= n 1) (list 1))
        ((= (mod n 2) 0) (cons n (collatz (/ n 2))))
        (else (cons n (collatz (+ (* 3 n) 1))))))

> (display (collatz 21))
(21 64 32 16 8 4 2 1)
```

- **How can something so ***weird***-looking be so powerful**?
- Let's find out. If everyone has the package manager Brew installed, go to this link to install Scheme for your OS:
https://scheme.com/download/
- If you're on a Mac and have the Homebrew package manager installed, you can type `brew install chezscheme` for a quick installation.
- To start Chez Scheme, simply type `chez` in your terminal. There you can test out expressions and see the results printed out.
- If you want to exit Chez Scheme, just press `ctrl-d`.
- If you want to run a file, do this: `chez --script __filename__`.

#### Arithmetic

- In most languages, arithmetic operators go between the numbers.
- Lisp treats these operators as functions, and therefore, puts the function in front.

```scheme
> (+ 2 3 4)
9
> (* 4 5 (+ 9 6))
300
> (/ 3 9 6)
1/18
```

- This is the equivalent code in Python:

```python
>>> 2 + 3 + 4
9
>>> 4 * 5 * (6 + 9)
300
>>> 3 / 9 / 6
0.05555555555555555
```

- Try some expressions out! Have fun with it. Remember to match the number of left and right parentheses!

- Since we don't have too much time, I'll give you a bag of functions to mess around with:

`define`

- This defines a variable or a function. You can use it like this:

```scheme
(define x 5)
(define y (* (+ 1 2) (+ 3 4)))

(define (f x) (x + 1))
(define (triple-sum x y z) (+ x y z))
```

`display`

- This prints out a variable, function, or raw value. This is how you use it:

```scheme
(display 25)
(display (/ 3 6 9))
(display "This is awesome!")
(display x)
```

`if`

- This works just like an `if` statement in Python. It takes three arguments: a condition, a true branch, and a false branch:

```scheme
(define x 5)

(if (= x 5) (display "X is 5!") (display ("X is not 5!")))
```

- This is only the beginning of Lisp's most important functions, which I hope we'll go into another meeting.

- Now, let's build an interpreter!