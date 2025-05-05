F := GF(7);
n := 58;

R<x> := PolynomialRing(F);
f := x^n - 1;
factorization := Factorization(f);

base := factorization[1][2] + 1;
r := #factorization;
numCyc := base^r;

function BaseRepresentation(n, b)
    Q := [];
    while n gt 0 do
        a := n mod b;
        Append(~Q, a);
        n := n div b;
    end while;
    Reverse(~Q);
    return Q;
end function;

cyclic_code := 1;

for i in [1..numCyc-2] do
    base_rep := BaseRepresentation(i, base);
    while #base_rep lt #factorization do
        base_rep := [0] cat base_rep;
    end while;

    for j in [1..#factorization] do
        cyclic_code := cyclic_code * (factorization[j][1]^base_rep[j]);
    end for;

    C := CyclicCode(n, cyclic_code);
    CD := Dual(C);

    if CD subset C then
        Q := CSSCode(C, CD);
        printf "Quantum Code Found: [[%o, %o, %o]] over GF(%o)\n", n, 2 * Dimension(C) - n, MinimumDistance(Q), 7;
    end if;

    if C subset CD then
        Q := CSSCode(CD, C);
        printf "Quantum Code Found: [[%o, %o, %o]] over GF(%o)\n", n, 2 * Dimension(CD) - n, MinimumDistance(Q), 7;
    end if;

    cyclic_code := 1;
end for;
