q := 2;
Fq2 := GF(q^2);
n := 5;

R<x> := PolynomialRing(Fq2);
f := x^n - 1;
factorization := Factorization(f);

// CSS base representation
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

for i in [1..numCyc-2] do
    rep1 := BaseRepresentation(i, base);
    while #rep1 lt r do
        rep1 := [0] cat rep1;
    end while;

    g1 := 1;
    for j in [1..r] do
        g1 *:= factorization[j][1]^rep1[j];
    end for;
    C1 := CyclicCode(n, g1);

    for k in [i+1..numCyc-1] do  // Ensure C2 is different and not identical
        rep2 := BaseRepresentation(k, base);
        while #rep2 lt r do
            rep2 := [0] cat rep2;
        end while;

        g2 := 1;
        for j in [1..r] do
            g2 *:= factorization[j][1]^rep2[j];
        end for;
        C2 := CyclicCode(n, g2);

        // Check if C2⊥ ⊆ C1
        if Dual(C2) subset C1 then
            d1 := MinimumDistance(C1);
            d2 := MinimumDistance(C2);
            d := n;  // Upper bound for min weight

            for v in C1 do
                if not v in Dual(C2) then
                    wt := Weight(v);
                    if wt lt d then d := wt; end if;
                end if;
            end for;
            for v in C2 do
                if not v in Dual(C1) then
                    wt := Weight(v);
                    if wt lt d then d := wt; end if;
                end if;
            end for;

            printf "CSS Quantum Code from Theorem 6: [[%o, %o, %o]]_%o^2\n", 
    n, Dimension(C1) + Dimension(C2) - n, d, q;

        end if;
    end for;
end for;
