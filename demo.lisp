(define nil (quote ()))

(define map
	(lambda (f lst)
		(if (null? lst) lst
			(cons (f (car lst)) (map f (cdr lst))))))

(define filter
	(lambda (f lst)
		(if (null? lst) lst
			(if (f (car lst))
				(cons (car lst) (filter f (cdr lst)))
				(filter f (cdr lst))))))

(define reduce
	(lambda (f lst seed)
		(if (null? lst) seed
			(f (car lst) (reduce f (cdr lst) seed)))))

(display (map (lambda (x) (+ x 1)) (cons 1 (cons 2 (cons 3 nil)))))
(display (filter atom? (cons (cons 1 (cons 2 nil)) (cons 3 nil))))
(display (reduce + (cons 1 (cons 2 (cons 3 (cons 4 (cons 5 nil))))) 0))