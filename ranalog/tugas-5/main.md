3. Bila diberikan bentuk $T(n)=T(n / 2)+1$, untuk $n>1$, dan $n=2^k$ (untuk suatu integer k), maka tentukan oder dari $T(n)$.

Jawab:

jika $n=2^k$, maka kita bisa tulis persamaan rekurensinya menjadi $T(2^k)=T(2^{k-1})+1$.

Misalkan $T(2^k)=s_k$, maka kita punya $s_k=s_{k-1}+1$.

perhatikan bahwa ini adalah persamaan rekurensi tak-homogen dengan $p(n)=1$ dan $b = 1$.
dengan begitu kita punya bentuk persamaan karakteristiknya
$$
(s-1)(s-b)^{(d+1)} = (s-1)(s-1) = (s-1)^2
$$

dengan $d$ adalah orde dari $p(n)$.

karena akar ganda, maka kita punya solusi untuk $s_k$ adalah
$$
s_k = c_1 1^k + c_2 k 1^k
$$

dengan begitu, kita punya
$$
T(2^k) = c_1 + c_2 k
$$
$$
T(n) = c_1 + c_2 \log_2 n
$$

jadi orde dari $T(n)$ adalah $\Theta(\log n)$.


    