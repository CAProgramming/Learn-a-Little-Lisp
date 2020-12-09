(define my_map (lambda (f lst) (if (null? lst) lst (cons (f (car lst)) (my_map f (cdr lst))))))

(define fn (lambda (x) (+ x 1)))
(define l (cons 1 (cons 2 (cons 3 4))))

(my_map fn l)
; hm, map is still not working