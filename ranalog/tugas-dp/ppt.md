---
marp: true

--- 

# 0/1 *Knapsack* Problem
**Kelompok 1**
- Ariya Puttasa Suwarno (2106722663)
- Bisma Rohpanca Joyosumarto (2106635581)
- Carles Octavianus (2006568613)
- Farisan Hafizh (2106653804)
---

## Permasalahan
 
Diberikan $n$ item berbeda yan denga masing-masing item memiliki berat $w_i$ dan nilai $v_i$. Diberikan juga sebuah *knapsack* dengan kapasitas $W$. Tentukan item-item mana yang harus dimasukkan ke dalam *knapsack* sehingga total nilai dari item-item tersebut maksimum dan total beratnya tidak melebihi kapasitas *knapsack*.

Dalam bahasa yang lebih matematis, jika $S$ adalah himpunan semua solusi yang memenuhi batasan, maka kita ingin mencari $s^* \in S$ yang memaksimalkan fungsi $f$ sebagai berikut:

$$f(s^*) = \sum_{i\in s^*} v_i$$

---

## Contoh Masukkan
```python
4 10 # n W
4 8 5 3 # w_i
5 12 8 1 # v_i
```

## Contoh Keluaran
```python
13 # total nilai maksimum
```

atau

```python
[(1,4,5), (3,5,8)] # item-item yang dipilih
```

---



## Greed Akan Gagal
Sebagai contoh kalau kita lakukan pemilihan greedy dengan memilih item dengan nilai terbesar, kita akan mendapatkan solusi 12 yang tentu saja salah. 

---
## Solusi Dynamic Programming

Kita akan menggunakan pendekatan *bottom-up* dengan membangun solusi untuk submasalah yang lebih kecil.

Misalkan $dp(i-1,j)$ merupakan solusi dari submasalah, dengan batasan baru, yaitu, memilih dari item-item $1,2,\ldots,i-1$ dengan kapasitas maksimal $j$.

Andaikan kita memiliki solusi untuk $dp(i-1,x), \forall x\leq j$, maka kita dapat menghitung solusi untuk $dp(i,j)$ dengan mempertimbangkan item ke-$i$. 

Perhatikan bahwa solusi untuk $dp(i,j)$ dapat dihitung dari solusi $dp(i-1,x), x\leq j$ dengan mempertimbangkan apakah memasukkan item ke-$i$ pada konfigurasi solusi optimal $dp(i-1,x-w_i)$ menghasilkan solusi yang lebih baik.

Dengan begitu, kita dapat menuliskan persamaan rekurens untuk $dp(i,j)$ sebagai berikut:

---

$$dp(i,j)= \begin{cases} dp(i-1,j) & \text{jika } w_i > j \\ \max(dp(i-1,j), dp(i-1,j-w_i)+v_i) & \text{jika } w_i \leq j \end{cases}
$$


---
Kita akan meng-*address* asumsi berikut:

>Andaikan kita memiliki solusi untuk $dp(i-1,x), \forall x\leq j$, maka kita dapat menghitung solusi untuk $dp(i,j)$ dengan mempertimbangkan item ke-$i$. 


Mudah dilihat bahwa solusi $dp(i-1,x)$ untuk $x\leq j$ dapat dihitung dengan argumen serupa pada slide sebelumnya, *yaitu dengan mempertimbangkan apakah memasukkan item ke-$i-1$ pada konfigurasi solusi optimal $dp(i-2,x-w_{i-1})$ menghasilkan solusi yang lebih baik.

Dengan begitu kita dapat membangun tabel solusi $dp$ dari $dp(0,0)$ sampai $dp(n,W)$.

---

## Solusi Python
    
```python
def solve(weights, profits, n, max_w):
    dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, max_w+1):
          left_over = j - weights[i-1]
          dp[i][j] = dp[i-1][j]
          if (left_over>=0):
             dp[i][j] = max(dp[i][j], dp[i-1][left_over]+profits[i-1])
    return dp[n][max_w]

```


---

## Membangun Solusi

Kita dapat membangun solusi dengan mengikuti nilai-nilai yang ada pada tabel $dp$.

Prinsipnya sederhana saja. kita misalkan koordinat $(i,j)$ dari tabel sebagai sebuah node. 

Node tersebut akan terhubung dengan node-node lain tergantung pada nilai-nilai $dp(i,j)$ dan $dp(i-1,j)$. lebih detailnya

- jika $dp(i,j) = dp(i-1,j)$, maka node $(i,j)$ akan terhubung dengan node $(i-1,j)$
- jika $dp(i,j) = dp(i-1,j-w_i)+v_i$, dimana $j-w_i\geq 0$, maka node $(i,j)$ akan terhubung dengan node $(i-1,j-w_i)$

Lakukan breadth-first search dari node $(n,W)$ untuk membangun solusi hingga mencapai node $(0,j)$ atau $(i,0)$.

---

```python
def solve_with_traceback(weights, profits, n, max_w):
    dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, max_w+1):
          left_over = j - weights[i-1]
          dp[i][j] = dp[i-1][j]
          if (left_over>=0):
             dp[i][j] = max(dp[i][j], dp[i-1][left_over]+profits[i-1])

    queue = [(n, max_w, [])]
    list_of_solution = set()

    while queue:
        i, j, curr_solution = queue.pop(0)
        if (i==0 or j==0):
            list_of_solution.add(tuple(curr_solution))
            continue
        if (dp[i][j] == dp[i-1][j]):
            queue.append((i-1, j, curr_solution))

        for left_over in range(j-1, 0, -1):
            if (left_over+weights[i-1]>j):
                continue
            if (dp[i][j] == dp[i-1][left_over]+profits[i-1]):
                nxt_node = (i-1, left_over, curr_solution+[(i,weights[i-1],profits[i-1])])
                queue.append(nxt_node)

    return list_of_solution , dp[n][max_w]
       
```


---

# Terima Kasih




