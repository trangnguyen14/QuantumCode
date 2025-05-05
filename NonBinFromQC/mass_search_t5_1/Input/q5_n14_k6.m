// Theorem 5.1: Quantum Codes from Symplectic Self-Orthogonal Codes

q := 5;
n := 14;  // Half the classical code length
k := 6;

F := GF(q);
G := RandomMatrix(F, k, 2*n); // Generator matrix
C := LinearCode(G); // Classical code C

// Define symplectic inner product
function SymplecticInnerProduct(u, v)
    n := #u div 2;
    sum := F!0;
    for i in [1..n] do
        sum +:= u[i]*v[n+i] - u[n+i]*v[i];
    end for;
    return sum;
end function;

// Compute symplectic dual
function SymplecticDual(C)
    V := VectorSpace(BaseRing(C), Length(C));
    Dual := sub<V | >;
    for v in V do
        if forall{c : c in Generators(C) | SymplecticInnerProduct(Eltseq(c), Eltseq(v)) eq 0} then
            Dual := sub<V | Setseq(Generators(Dual)) cat [v]>;
        end if;
    end for;
    return LinearCode(Dual);
end function;

// Symplectic weight
function SymplecticWeight(v)
    n := #v div 2;
    count := 0;
    for i in [1..n] do
        if v[i] ne 0 or v[n+i] ne 0 then
            count +:= 1;
        end if;
    end for;
    return count;
end function;

// Construct quantum code if possible
CDS := SymplecticDual(C);

if forall{c : c in Generators(C) | c in CDS} then
    d_s := 2*n;
    for v in CDS do
        if v notin C then
            ws := SymplecticWeight(Eltseq(v));
            if ws lt d_s then
                d_s := ws;
            end if;
        end if;
    end for;

    printf "Quantum Code Found: [[%o, %o, %o]] over GF(%o)\n", n, n-k, d_s, q;
else
    printf "No symplectic quantum code produced: C not subset of CDS.\n";
end if;
