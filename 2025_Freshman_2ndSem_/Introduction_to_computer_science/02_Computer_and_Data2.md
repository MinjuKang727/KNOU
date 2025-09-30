> 이전 시간 안내  
> [1강. 컴퓨터와 자료 (1)        ](./01_Computer_and_Data1.md)  

<br>

# 2강. 컴퓨터와 자료 (2)          

## 학습 목차
> [1. 데이터와 정보](#1-데이터와-정보)  
> [2. 진법](#2-진법)
> [3. 정수 표현](#3-정수-표현)  
> [4. 실수 표현](#4-실수-표현)  
> [5. 문자 표현](#5-문자-표현)  

## 1. 데이터와 정보
### 데이터와 정보의 관계
- $I = P(D)$
    ```
    데이터 D → 처리기 P → 정보 I
    ```
    
    - 데이터(`D`)
        - 현실 세계로부터 관찰이나 측정을 통해 단순히 얻어지는 값/사실
        - 처리하고자 하는 대상
        - 하나의 원재료
    - 처리기(`P`)
        - 예전에는 사람이 했었던 것
        - 요즘은 컴퓨터가 하는 것
        - 데이터를 가공, 변환, 조작하는 곳
    - 정보(`I`)
        - 어떤 상황에 대해 적절한 의사결정을 수행할 수 있게 하는 지식
        - 데이터를 입력 받아 처리기에서 처리해서 나온 결과
        - 데이터를 처리하여 어떤 특정한 목적을 가지고 있는 처리 결과
    - 데이터 처리
        - 데이터를 정보로 만드는 과정  
            - 데이터 처리라고 하면 일반적으로 숫자만 다룰 것 같음
        - 정보 처리: 수치적인 것과 비수치적인 것을 모두 다 포함하는 일반적인 표현으로 사용

### 데이터의 표현 형태
- 데이터의 유형과는 무관하게 일관된 표현 방식 사용
    - 문자, 정수, 실수, 이미지, 비디오, 오디오 등 → "**비트 패턴**"
    - 메모리에 저장된 데이터 유형에 맞는 해석과 처리가 필요
        → 입·출력 장치나 프로그램의 책임/역할
    
### 데이터의 표현 단위
- 비트(bit; Binary digit)
    - 컴퓨터가 데이터를 표현하는 논리적 최소 단위
    - 0 🌚 / 1 🌝
- 바이트(Byte)
    - 길이가 8개인 비트 패턴
    ```
    🌚🌝🌝🌚🌚🌚🌚🌝  
     0 1 1 0 0 0 0 1
    ```
    - 영문자 하나 → 1바이트
    - 한글 하나 → 2바이트
    - **KB**($2^{10} \approx 10^3$), **MB**($2^{20} \approx 10^6$), **GB**($2^{30} \approx 10^9$), **TB**($2^{40} \approx 10^{12}$), **PB**($2^{50} \approx 10^{15}$), **EB**($2^{60} \approx 10^{18}$), **ZB**($2^{70} \approx 10^{21}$), **YB**($2^{80} \approx 10^{24}$) 
    - 워드(Word)
        - 컴퓨터 연산의 기본 단위가 되는 정보의 양
        - 보통 32bit, 64bit
        
---
## 2. 진법
- 수를 세는 방법 또는 단위
    - $r$진법 → 0, 1, $\cdots$, (r - 1)까지의 숫자만을 사용하는 진법 → $r$진수

        | 진법 | 사용하는 숫자 | 예 | 비고 |
        |:---:|:---|:---|:---|
        |2진법|$0, 1$|$1011_{2} \quad 1001_{b}$| b: binary |
        |8진법|$0, 1, \cdots, 7$|$13_{8} \quad 257_{o}$| o: octal|
        |10진법|$0, 1, 2, \cdots , 9$|$11_{10} \quad 123_{d}$| d: decimal|
        |16진법|$0, 1, \cdots , 9, A, B, C, D, E, F$|$B_{16} \quad FF30_{h}$| h: hexadecimal|
- 진법의 각 숫자는 위치에 따라 서로 다른 가중치(**자릿값**)를 가짐
    - $r$진법의 자릿값 → $r^x$($x$는 숫자의 위치를 나타내는 정수)
    - 123(일이삼) → 일백이십삼($= 1 \times 10^2 + 2 \times 10^1 + 3 \times 10^0$)

        ![이진법과 가중치](./IMGs/02_02_%EC%9D%B4%EC%A7%84%EC%88%98_%EA%B0%80%EC%A4%91%EC%B9%98.png)
### **2진수**를 **10진수**로 변환
- 10진수 = $\sum$(각 비트값 $\times$ `해당 비트 위치의 가중치`)
    - 해당 비트 위치의 가중치
        - $\cdots \ 2^4 \quad 2^3 \quad 2^2 \quad 2^1 \quad 2^0 \quad . \quad 2^{-1}\quad 2^{-2}\quad 2^{-3}\quad 2^{-4}\cdots$
        - $\cdots 16 \quad 8 \quad 4 \quad 2 \quad 1 \quad .\quad \frac{1}{2} \quad  \frac{1}{4} \quad \frac{1}{8} \quad \frac{1}{16} \cdots$ 
    - 예시
        - $101.1001_{(2)} \\\\ 
        \qquad = 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 0 \times 2^{-2} + 0 \times 2^{-3} + 1 \times 2^{-4}\\\\
        \qquad = 5.5625_{(10)}$
    
### **8**/**16진수**를 **10진수**로 변환
- 10진수 = $\sum$(각 숫자값 $\times$ `해당 위치의 가중치`)
    - 해당 위치의 가중치
        - $\cdots \ 8^4 \quad 8^3 \quad 8^2 \quad 8^1 \quad 8^0 \quad . \quad 8^{-1}\quad 8^{-2}\quad 8^{-3}\quad 8^{-4}\cdots$
        - $\cdots \ 8^4 \quad 16^3 \quad 16^2 \quad 16^1 \quad 16^0 \quad . \quad 16^{-1}\quad 16^{-2}\quad 16^{-3}\quad 16^{-4}\cdots$
    - 예시
        - $3456_{(8)} \\\\ 
        \qquad = 3 \times 8^3 + 4 \times 8^2 + 5 \times 8^1 + 6 \times 8^0\\\\
        \qquad = 1838_{(10)}$
        - $AE7_{(16)} \\\\ 
        \qquad = A \times 16^2 + E \times 16^1 + 7 \times 16^0\\\\
        \qquad = 10 \times 16^2 + 14 \times 16^1 + 7 \times 16^0\\\\
        \qquad = 2791_{(10)}$

### **10진수**를 **r진수**로 변환
> (r = 2, 8, 16)

- 정수부분과 소수 부분을 구분하여 각각의 방법으로 처리한 후,  
    각 결과를 단순히 연결해서 나열
- 예시: `60`.`6875`
    - 정수 부분: 60 → 111100
    - 소수 부분: 6875 → 1011
    - $60.6875_{(10)} = 111100.1011_{(2)}$

### 10진수_정수부분 →  r진수
```
입력값 = 10진수(정수 부분);
i = 0;

몫 = 입력값 / r;
나머지 = 입력값 mod r;
결과(i) = 나머지;

while (몫 != 0)
    입력값 = 몫;
    i = i + 1;

    몫 = 입력값 / r;
    나머지 = 입력값  mod r;
    결과(i) = 나머지
end

출력[결과(i), 결과(i - 1), ⋯, 결과(0)];
```

- 2진수 예제  

    ${\begin{array}{r} 
    \\ 2{\underline{\smash{\big)}\,\textcolor{red}{60}\,}}\phantom{\,\cdots\,0\,\uparrow}
    \\ 2 {\underline{\smash{\big)}\,30\,}}\,\cdots\, 0
    \\ 2 {\underline{\smash{\big)}\, 15\,}}\,\cdots\,0
    \\ 2 {\underline{\smash{\big)}\,\phantom{0} 7\,}}\,\cdots\,1
    \\ 2 {\underline{\smash{\big)}\,\phantom{0} 3\,}}\,\cdots\,1
    \\ 2 {\underline{\smash{\big)}\,\phantom{0} 1\,}}\,\cdots\,1
    \\ \phantom{2)\, 0}\textcolor{blue}{0}\,\,\cdots\,1
     \end{array}}
    {\begin{array}{r}
    \\\\\bigg\uparrow
    \\\bigg\uparrow
    \\\bigg\uparrow
    \end{array}}$

    $\therefore \,60_{10} = 111100_2$

- 8진수

    ${\begin{array}{r} 
    \\ 8{\underline{\smash{\big)}\,\textcolor{red}{60}\,}}\phantom{\,\cdots\,0}
    \\ 8 {\underline{\smash{\big)}\phantom{\,0}7\,}}\,\cdots\, 4
    \\ \phantom{2)\, 0}\textcolor{blue}{0}\,\,\cdots\,7
     \end{array}}
    {\begin{array}{r}
    \\\\\bigg\uparrow
    \end{array}}$

    $\therefore \,60_{10} = 74_8$   

- 16진수

    $\begin{array}{r} 
    \\ 16{\underline{\smash{\big)}\,\textcolor{red}{60}\,}}\phantom{\,\cdots\,C}
    \\ 16 {\underline{\smash{\big)}\phantom{\,0}3\,}}\,\cdots\, C
    \\ \phantom{16)\, 0}\textcolor{blue}{0}\,\,\cdots\,3
        \end{array}
        {\begin{array}{r}
        \\\\\bigg\uparrow
        \end{array}}$

    $\therefore \,60_{10} = 3C_{16}$   

### 10진수_소수부분 → r진수
```
입력값 = 10진수(소수 부분);
i = 0;

while(입력값 != 0)
    임시변수 = 입력값 * r;
    결과(i) = 임시변수의 정수 부분;
    i = i + 1;
    입력값 = 임시변수의 소수 부분;
end

출력[0.결과(0), 결과(1), ⋯, 결과(i)];
```

- 2진수

    ${\begin{array}{r}
    \textcolor{red}{0.6875}\quad\Rsh
    \\\underline{\times\,\phantom{0.000}2\,\,}\,\,\,\,\uparrow
    \\\small{\colorbox{lightblue}{1}.\colorbox{yellow}{375}\rightarrow}\scriptsize{\nearrow}
    \\\color{red}{\downarrow}\phantom{\qquad\qquad\,\,}
    \end{array}}
    {\begin{array}{r}\
    \huge\uparrow\\\\\\
    \end{array}}
    {\begin{array}{r}
    0.375\quad\Rsh
    \\\underline{\times\,\phantom{0.00}2\,\,}\,\,\,\,\uparrow
    \\\small{\colorbox{lightblue}{0}.\colorbox{yellow}{75}\rightarrow}\scriptsize{\nearrow}
    \\\color{red}{\downarrow}\phantom{\qquad\quad\,\,\,\,\,}
    \end{array}}
    {\begin{array}{r}
    0.75\quad\Rsh
    \\\underline{\times\,\phantom{0.0}2\,\,}\,\,\,\,\uparrow
    \\\small{\colorbox{lightblue}{1}.\colorbox{yellow}{5}\rightarrow}\scriptsize{\nearrow}
    \\\color{red}{\downarrow}\phantom{\qquad\quad\,\,}
    \end{array}}
    {\begin{array}{r}
    0.5\qquad\quad\,\,\,\,\,
    \\\underline{\times\,\phantom{0.}2\,\,}\quad\,\,\,\, \color{lightgreen}{\tiny{\nearrow}}\rightarrow
    \\\small{\colorbox{lightblue}{1}.\colorbox{pink}{0}\,}\,\,\color{lightgreen}{\nearrow}\qquad\,\,
    \\\color{red}{\downarrow}\qquad\qquad\quad
    \end{array}}
    {\begin{array}{r}
    \colorbox{lightgreen}{소수 부분이 0이면 멈춤}\\\\
    \end{array}}
    \\0.\colorbox{lightblue}{1\qquad\qquad\qquad0\qquad\qquad\quad\,\,\,1\qquad\qquad\,\,\,\,1}
    $

- 8진수

    ${\begin{array}{r}
    \textcolor{red}{0.6875}\quad\Rsh
    \\\underline{\times\,\phantom{0.000}8\,\,}\,\,\,\,\uparrow
    \\\small{\colorbox{lightblue}{5}.\colorbox{yellow}{5}}\,\scriptsize{\rightarrow\rightarrow\rightarrow\nearrow}
    \\\color{red}{\downarrow}\phantom{\qquad\qquad\,\,\,}
    \end{array}}
    {\begin{array}{r}
    0.5\,\,
    \\\underline{\times\,\phantom{0.}8\,\,}
    \\\small{\colorbox{lightblue}{4}.\colorbox{pink}{0}}
    \\\color{red}{\downarrow}\quad\,\,\,
    \end{array}}
    \\0.\colorbox{lightblue}{5\qquad\qquad\qquad4}
    $

- 16진수

    ${\begin{array}{r}
    \textcolor{red}{0.6875}\,\,
    \\\underline{\times\,\phantom{0.00}16\,\,}
    \\\small{\colorbox{lightblue}{11}.\colorbox{pink}{0}}\quad\,\,\,
    \\\color{red}{\downarrow}\qquad\quad
    \end{array}}
    \\0.\colorbox{lightblue}{B}
    $

<br>

<span style="background-color:yellow">$\,\therefore\,{0.6875}_{10} = {0.1011}_{2} = {0.54}_{8} = {0.B}_{16}$</span>

※ 예외적인 경우

$\quad\quad \color{red}{{\tiny{\nearrow}}\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow\rightarrow{\tiny{\searrow}}}$  
${\begin{array}{r}
\colorbox{yellow}{\textcolor{red}{0.6}}\,\,\,\,\Rsh
\\\underline{\times\,\phantom{0.}2\,\,}\,\,\,\uparrow
\\\small{\colorbox{lightblue}{1}.\colorbox{yellow}{2}}\scriptsize{\rightarrow\nearrow}
\\\color{red}{\downarrow}\qquad\,\,\,\,\,
\end{array}}
{\begin{array}{r}
0.2\quad\Rsh
\\\underline{\times\,\phantom{0.}2\,\,}\,\,\,\,\uparrow
\\\small{\colorbox{lightblue}{0}.\colorbox{yellow}{4}\,}\scriptsize{\rightarrow\nearrow}
\\\color{red}{\downarrow}\qquad\quad
\end{array}}
{\begin{array}{r}
0.4\quad\Rsh
\\\underline{\times\,\phantom{0.}2\,\,}\,\,\,\,\uparrow
\\\small{\colorbox{lightblue}{0}.\colorbox{yellow}{8}\,}\scriptsize{\rightarrow\nearrow}
\\\color{red}{\downarrow}\qquad\quad
\end{array}}
{\begin{array}{r}
0.8\quad\Rsh
\\\underline{\times\,\phantom{0.}2\,\,}\,\,\,\,\uparrow
\\\small{\colorbox{lightblue}{1}.\colorbox{yellow}{6}\,}\scriptsize{\rightarrow\nearrow}
\\\color{red}{\downarrow}\qquad\quad
\end{array}}
{\begin{array}{r}
\colorbox{yellow}{\textcolor{red}{0.6}}\\\\\\\\
\end{array}}
{\begin{array}{r}
\color{lightgreen}{\cdots\, \cdots}
\end{array}}
\\0.\colorbox{lightblue}{1\qquad\qquad\,\,0\qquad\qquad\,\,0\qquad\qquad\,\,\,1}\qquad\qquad 1\quad0\quad0\quad1\quad\cdots
$

$\therefore \, {0.6}_{10} = {0.1001}_{2}$

<i><u>컴퓨터에서 나타내는 실수는 정확한 값이 아니라 <b>"근사값"</b>이다.</u><br>
얼마나 더 많은 메모리가 주어지는지에 따라 좀 더 그 값에 가까워질 수는 있겠지만 정확한 값이 아니다.</i>

### r진수 간의 변환(r = 2, 8, 16)

![r진수간 진법 변환 방법](./IMGs/02_02_r%EC%A7%84%EC%88%98%EA%B0%84_%EB%B3%80%ED%99%98.png)

- 2진법 수 3개를 8진법 수 1개로 표현
- 16진수 1개는 2진수 4개로 표현

- 8진수 ⇄ 16진수 진법 변환 방법
    - 직접 바꾸는 방법은 없음
    - 10진수나 2진수를 거쳐서 변환해야 함.

---
## 3. 정수 표현
> 소숫점이 맨 오른쪽에 있다고 가정  
> 컴퓨터의 메모리 크기에 따라 실제 나타낼 수 있는 정수의 범위가 정해짐.  

### 정수 표현 방법
- 부호 없는 정수
    - 부호(`+`, `-`) 비트가 없음
    - n비트: $0 \sim 2^n-1$
    - 8비트: $0 \sim 255$
- 부호 있는 정수
    - 최상위 비트 ⇒ **부호 비트**(0: 양수, 1: 음수)
    - 형태
        - 양의 정수는 모두 동일
        - 음의 정수는 서로 다른 형태를 가짐
            - `부호화-크기`: 절대값으로 표현
                - $-(2^{n-1}-1)\,\sim\,+(2^{n-1}-1)$
                - +0 (<span style="color:red">00000000</span>)
                - -0 (<span style="color:red">10000000</span>)
            - `1의 보수`: 양수에 대한 보수로서 표현
                - $-(2^{n-1}-1)\,\sim\,+(2^{n-1}-1)$
                - +0 (<span style="color:red">00000000</span>)
                - -0 (<span style="color:red">11111111</span>)  

            *`부호화-크기`와 `1의 보수`는 0을 기준으로 나타낼 수 있는 양수와 음수가 대칭<br>나타낼 수 있는 값의 크기가 동일<br>
            ∵ 0이 2개(+0, -0; 대칭을 이룸)*

            - `2의 보수`: (1의 보수 + 1)로 음수 표현
                - $-2^{n-1}\,\sim\,+(2^{n-1}-1)$
                - 음수보다 양수가 하나 더 많은 값을 나타낼 수 있음.

### 부호 없는 정수
| 주어진 수 | 2진수 | n비트 할당 <i>(n = 8)</i> |비고|
|:---:|:---:|:---|:---|
|115|1110011|$\colorbox{lightblue}{{\color{gray}{0}}}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}$||
|275|<span style="background-color:lightgreen;">1</span>00010011|${\color{red}{1}}\,\colorbox{pink}{0}\,\colorbox{pink}{0}\,\colorbox{pink}{0}\,\colorbox{pink}{1}\,\colorbox{pink}{0}\,\colorbox{pink}{0}\,\colorbox{pink}{1}\,\colorbox{pink}{1}$<br><span style="color:red">↳ 오버플로(Overflow)</span>|275 > 255<br>더 많은 메모리가 주어져야만 정확한 값을 표현 가능|

### 부호 있는 정수
- n = 8비트인 경우
    - 양수: $\colorbox{yellow}{{\color{red}{0}}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}$
        - 예: $\colorbox{lightblue}{124} = \colorbox{yellow}{{\color{red}{0}}}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}$
    - 음수: $\colorbox{yellow}{{\color{red}{1}}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}\,\colorbox{wheat}{\phantom{0}}$
        - 예: -124
            - `부호화-크기`  
            : 부호 비트만 `1`로 바꾸고 그 뒤에 절댓값을 이진수로 써 준다.  
            $\colorbox{yellow}{{\color{red}{1}}}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}$
            - `1의 보수`  
            : 0 → **1**, 1 → **0**  
            부호 비트는 그대로 둠  
            $\colorbox{yellow}{{\color{red}{1}}}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}\,\colorbox{wheat}{0}\,\colorbox{wheat}{1}\,\colorbox{wheat}{1}$
            - `2의 보수`  
            : (1의 보수) + 1  
            $\,\,\,\,\colorbox{yellow}{{\color{red}{1}}}{\colorbox{q}{0}}{\colorbox{q}{0}}{\colorbox{q}{0}}{\colorbox{q}{0}}{\colorbox{q}{0}}{\colorbox{q}{1}}{\colorbox{q}{1}}
            \\\underline{+\qquad\qquad\qquad\qquad1\,\,}$  
            $\,\,\,\,\colorbox{yellow}{{\color{red}{1}}}\colorbox{wheat}{0}\colorbox{wheat}{0}\colorbox{wheat}{0}\colorbox{wheat}{0}\colorbox{wheat}{1}\colorbox{wheat}{0}\colorbox{wheat}{0}$

### 정수 표현 방법 비교
![정수 표현 방법 비교: 부호 없는 정수 vs 부호 있는 정수](./IMGs/02_03_%EC%A0%95%EC%88%98%EC%9D%98_%ED%91%9C%ED%98%84_%EB%B0%A9%EB%B2%95.png)


### 2의 보수 방식의 응용
> 실제 컴퓨터가 사용하는 방법

- 뺄셈: ${\colorbox{blue}{A - B} \longrightarrow}\,{\colorbox{blue}{A+(-B)}}$
    - 예시: 24 - 17
        ${\begin{array}{r}
        \quad00011000\quad\scriptsize{+24}\,\,
        \\\underline{-\,\,00010001\,\,}\,\,\,\scriptsize{\colorbox{yellow}{+17}}
        \end{array}}
        {\begin{array}{r}
        \quad{}_{\colorbox{yellow}{\color{red}{2의 보수}}}\quad\,\,\,\,
        \\\color{red}{\overrightarrow{\qquad\qquad\qquad}}
        \end{array}}
        {\begin{array}{r}
        00011000\,\,\,\,\scriptsize{+24}\,\,
        \\\underline{{\color{red}{+}}\,\,11101111\,\,}\,\,\,\scriptsize{\colorbox{yellow}{-17}}
        \\{\colorbox{pink}{1}}00000111\,\,\,\,\scriptsize{+7}\,\,\,\,
        \\\color{red}{\hookrightarrow \, 무시}\qquad\quad
        \end{array}}$ 


*🤔이건 그냥 내가 궁금한 거~<br>
위 계산에서 올림 비트 `1`을 무시해도 어떻게 정확한 값이 나올까?*

![정수 표현 방법 비교: 부호 없는 정수 vs 부호 있는 정수](./IMGs/02_03_%EC%9D%B4%EC%A7%84%EC%88%98_%ED%91%9C%ED%98%84_%EB%AA%A8%EB%93%88%EB%9F%AC_%EC%82%B0%EC%88%A0_%EC%9B%90%EB%A6%AC.png)

*∵ 2의 보수를 이용한 방법이 256을 주기로 순환하는 수학적 특성을 가지고 있기 때문입니다.*

### 2의 보수 방식의 응용
- 이진수 **10001101**은 **십진수**로 얼마인가?
    - 8비트, 2의 보수 방식을 이용했을 때

        ```
        ① 10진수를 이진수로 변환
        ② 보수 계산
        ③ 보수 결과 + 1
        의 결과가 10001101
        ```

        역으로 계산해보자.

        ```
        결과: 10001101
        ① 결과 - 1: 10001100
        ② 보수 계산: 11110011
        ③ 이진수를 십진수로 변환: -115
        ```
---
## 4. 실수 표현
- 과학적 표기법을 활용한 부동소수점 방식으로 표현
    - 과학적 표기법 예시
        - 1,234,000,000,000 $\color{purple}{\longrightarrow}$ <span style="background-color:lightblue">$\quad1.234 \times 10^{12}\quad$</span>
        - 0.0000000005678 $\color{purple}{\longrightarrow}$ <span style="background-color:lightgreen">$\quad-5.678 \times 10^{-10}\quad$</span>
---
## 5. 문자 표현       

<br>

> 다음 시간 안내  
> [3강. 자료구조 (1)         ](./03_Data_Structure1.md)  