// Theorem 5.2: Quantum Codes from Symplectic Self-Orthogonal Codes (Dual Contained in Code)
q := 2;
n := 6;
k := 6;

F := GF(q);
G := RandomMatrix(F, k, 2*n);
C := LinearCode(G);

// Symplectic inner product
function SymplecticInnerProduct(u, v)
    n := #u div 2;
    sum := F!0;
    for i in [1..n] do
        sum +:= u[i]*v[n+i] - u[n+i]*v[i];
    end for;
    return sum;
end function;

// Symplectic dual
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

// Construct code if CDS ⊆ C
CDS := SymplecticDual(C);

if forall{c : c in Generators(CDS) | c in C} then
    d_s := 2*n;
    for v in C do
        if v notin CDS then
            ws := SymplecticWeight(Eltseq(v));
            if ws lt d_s then
                d_s := ws;
            end if;
        end if;
    end for;

    printf "Quantum Code Found: [[%o, %o, %o]] over GF(%o)\n", n, k-n, d_s, q;
else
    printf "No quantum code: CDS is not contained in C.\n";
end if;
