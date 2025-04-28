// Declare the finite field GF(q^2) where q is a prime power.
q := 3;  // Change this to your desired prime power
Fq2 := GF(q^2);

// Define the parameters
n := 60;    // Change this to your desired code length

// Define the polynomial ring over GF(q^2)
R<x> := PolynomialRing(Fq2);

// Define the polynomial x^n - 1
f := x^n - 1;
factorization := Factorization(f);
printf "Factorization of x^%o - 1 over GF(%o^2):\n%o\n", n, q, factorization;

// Determine the base (use the multiplicity of the first factor)
base := factorization[1][2] + 1;
r := #factorization;
numCyc := base^r;

// Base representation function
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

// Generate and print Quantum codes using Construction X
cyclic_code := 1;

for i in [1..numCyc-2] do  
    base_rep := BaseRepresentation(i, base);
    
    // Pad with leading zeros
    while #base_rep lt #factorization do
        base_rep := [0] cat base_rep;
    end while;

    for j in [1..#factorization] do
        cyclic_code := cyclic_code * (factorization[j][1]^base_rep[j]);
    end for;

    // Construct the classical cyclic code C
    C := CyclicCode(n, cyclic_code);
    dim_C := Dimension(C);
    minD_C := MinimumDistance(C);

    // Print the classical code C
    printf "\nClassical Code C: [%o, %o, %o] over GF(%o^2)\n", n, dim_C, minD_C, q^2;

    // Construct the Hermitian Dual of C
    CD := HermitianDual(C);  
    dim_CD := Dimension(CD);
    minD_CD := MinimumDistance(CD);

    // Print the Hermitian dual code C⊥h
    printf "Hermitian Dual Code C_perp_h: [%o, %o, %o] over GF(%o^2)\n", n, dim_CD, minD_CD, q^2;

    IntersectionCode := C meet CD;
    dim_Intersection := Dimension(IntersectionCode);

    // Calculate e as described in the theorem
    e := dim_C - dim_Intersection;

    SumCode := C + CD;
    minD_Sum := MinimumDistance(SumCode);

    // Calculate the minimum distance of the resulting quantum code
    dQ := Minimum([minD_CD, minD_Sum, minD_Sum + 1]);

    // Calculate quantum code parameters
    nQ := n + e;
    kQ := n - 2 * dim_C + e;

    // Print valid quantum codes only
    if kQ ge 0 then
        printf "Quantum Code Found: [[%o, %o, %o]]\n", nQ, kQ, dQ;
    end if;

    // Reset cyclic_code for the next iteration
    cyclic_code := 1;
end for;
