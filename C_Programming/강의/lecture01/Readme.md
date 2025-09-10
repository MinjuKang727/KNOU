# 01강. C언어의 개요

> ## 학습목차  
> [1. C 언어의 등장과 발전](#1-c-언어의-등장과-발전)  
> [2. C 프로그램의 작성](#2-c-프로그램의-작성)  
> [3. C 프로그램의 구성](#3-c프로그램의-구성)  
> [4. 에러와 경고](#4-에러와-경고)  

---

## 1. C 언어의 등장과 발전

### 1. 컴퓨터 프로그래밍과 프로그래밍 언어
- 프로그래밍이란?
    > 컴퓨터가 작업을 수행하기 위해 실행해야 하는 일련의 명령을 작성하는 것


- 프로그래밍 언어
    > 프로그램을 작성하기 위해 사용되는 언어  

<br>

```
컴퓨터 하드웨어
```
🔼  

```
제 1세대 언어(기계어)   
ex) 00000101 00010000 00000000 
```  

🔼(어셈블러)  
    
```
제2세대 언어(어셈블리어)  
ex) ADD AX, 0010H  
```

🔼(컴파일러, 인터프리터)  

```
제3세대 언어(고급언어: C, C++, Java, Python 등)  
ex) a+= 16;
```

---

### 2. C 언어
- C 언어의 탄생
    - 1972년에 Bell 연구소의 Denis Ritchie가 시스템 프로그래밍을 위한 목적으로 개발한 프로그래밍 언어
        - 컴퓨터 기종간 호환성이 높은 고급 프로그래밍 언어
        - 하드웨어 수준의 제어와 빠른 실행이 가능한 프로그램을 만들 수 있는 언어  

        ➡️ PDP-7컴퓨터에서 어셈블리어로 구현한 Unix 커널을 C언어로 재 작성  

        ➡️ 다양한 컴퓨터에 Unix 운영체제를 이식할 수 있게 됨

    - C 언어의 연혁
        - 1960 : ALGOL 60 
        - 1963 : CPL(Combined Programming Language) 
            - 영국 캠브릿지 대학에서 만든 프로그래밍 언어
            - 처음에는 Cambridge Programming Language의 약자였으나  
            이후 런던 대학과 공동으로 만들게 되면서  
            Combined Programming Language로 이름 변경
        - 1967 : BCPL(Basic CPL)
        - 1970 : B언어
        - 1972 : C언어
            - 아직 표준화 되기 전
        - 1978 : K&R C (Kernighan&Ritchie's C)
            - Brian Kernighan과 Dennis Ritchie이 쓴 C언어 책이 사실상 표준처럼 사용됨
        - 1989 : ANSI C(C89)
            - ANSI(미국 국립 표준 협회)에서 C언어의 표준 지정
        - 1990 : ISO C(C90)
            - ISO(국제 표준화 기구)에서 지정한 C언어 표준
            - 이전의 ANSI C를 인정하여 만든 것이므로 ANSI C와 거의 같음
        - *1999 : C99*  (여기부터는 ANSI C와 거의 동일)
        - *2011 : C11*
        - *2017 : C17*
        - *2023 : C23*
- C 언어의 특징
    - 범용 고급 언어
        - 논리적인 처리 구조를 만들 수 있는 데이터 표현 및 흐름 제어를 할 수 있음
        - 여러 가지 유용한 처리를 위한 표준 라이브러리를 제공함
        - 프로그램의 이식성이 높음
    - 시스템 프로그래밍에 적합한 언어
        - 저급언어 수준의 특성이 있으며, 하드웨어 제어에 적합함.
        - 매우 빠른 실행 속도
    - 간결한 문법 구조로 되어 있음

---

## 2. C 프로그램의 작성

### 1. 프로그램 개발 단계

`프로그램의 목적 정의`-----[ 요구분석, 시스템 분석, 기능 정의]  
↓  
`프로그램 설계`-----[분석된 기능을 처리하기 우한 프로그램 구조 설계]  
↓  
`소스코드 작성`-----[프로그램 설계를 기반으로 언어의 문법에 따라 작성]  
↓  
`컴파일/링크`-----[소스코드의 문법 검사 및 실행 가능 코드로 변환]  
↓  
`프로그램 실행`-----[필요한 데이터를 제공하여 프로그램 실행]  
↓  
`테스트와 디버깅`-----[에러를 검사하여 디버깅을 함]  
↓  
`유지 보수`-----[사용 중 발생하는 에러 및 변경 사항 처리]  

---

### 2. C 프로그래밍을 실행 파일로 만드는 과정

1. **코딩** : C언어의 문법에 맞게 프로그램을 작성하는 과정
    - **소스 파일**(Sub.h, Sub.c, Sample.c) : C형태의 코드를 갖고 있는 파일 
    - 프로그램은 하나의 파일로 만들 수도 있지만 프로그램의 규모가 커지면 커질수록 여러개의 소스 파일로 나누어 관리하는 것이 편리하기 때문에  
    보통은 하나의 프로그램 안에 여러개의 소스 파일이 존재
2. **컴파일** : 소스 파일을 목적 파일로 변환하는 과정
    - **목적 파일**(sub.obj, Sample.obj) : 소스 코드를 기계가 이해할 수 있는 기계어 형태의 코드로 만들어 낸 것
        - 물론 여기에는 그 외에 실제 실행 파일을 만드는 데 필요한 부가 정보를 포함되어 있을 수 있음.
        - Microsoft의 개발도구로 프로그램 개발 시, 컴파일을 하게 되면 `obj` 확장자를 가짐.
3. **링크** : 목적 파일과 라이브러리를 묶어서 하나의 실행 파일을 만드는 과정
    - **라이브러리** : 컴파일러에서 제공하거나 또는 다른 여러 가지 용도에 맞게 미리 제공된 여러 요소
    - **실행 파일** : 목적 파일과 프로그램에 필요한 라이브러리를 묶어 만든 실행할 수 있는 형태의 코드 파일, 이 파일을 이용해 실제로 프로그램을 동작시킬 수 있음.

- **빌드** : 컴파일 과정과 링크 과정을 통틀어 이르는 말
    - 링크하는 과정까지를 통틀어 빌드하는 과정을 컴파일이라고 통칭하기도 함.

- 필요한 도구
    - 소스 코드 편집기
    - 컴파일러
    - 링커
    - 디버깅 도구

    ➡️ 통합 개발 환경(IDE; Integrated Development Environment)

    ex) Microsoft의 **Visual Studio**/ **DEV C++** / Code::Blocks / eclipse / VS Code
    > <u>**Visual Studio, Dev C++**</u>은 자동으로 C언어 컴파일러가 설치됨.  
    (별도 설치 없이 바로 실습 가능👍*추천*👍)  
    > 다른 IDE는 별도의 설치 필요


---

## 3. C프로그램의 구성
### 1. C프로그램의 기본 구조

```c
/* 도입부 */
......
```
```c
/* main 함수 */
int main()
{
    /* 필요한 선언문, 명령문 등 */
    ......
}
```
```c
/* 프로그램에 필요한 함수 선언 */
void f()
{
    ......
}
```

- C프로그램 작성시의 일반적인 규칙
    - 반드시 하나 이상의 함수를 표함해야 한다.
    - main() 함수가 반드시 존재해야 한다.
    - 함수의 몸체는 시작과 끝을 알리는 중괄호{}를 사용하여 블록으로 구성한다.
    - 블록 안에는 변수 선언문, 치환·연산·함수 호출 등의 명령을 기입한다.
    - 선행처리 지시어(preprocessing directives)를 제외한 문장의 끝에는 세미콜론(;)을 붙인다.

- C프로그램을 구성하는 토큰의 종류
    > **토큰** : 프로그램을 구성하는 가장 작은 단위(이름, 연산자, 상수 등)  

    - **예약어**(키워드) : C에서 고유한 문법 및 의미가 정해진 단어
    - **명칭** : 변수, 함수 등을 식별하기 위해 정의하는 이름
    - **상수** : 값이 변하지 않는 자료(정수, 실수, 문자 등)
    - **문자열** : 큰따옴표("")로 붂인 문자 시퀀스
    - **구두점** : 고유한 문법 및 의미가 정해진 기호
        - 예: `=`, `+`, `-`, `*`, `/` 등의 연산자나 `;`, `,`, 괄호(`(`, `)`) 등의 구분자
    - **설명문** : 프로그램에 대한 주석
        - `/* */` 또는 `//`

- **예약어**(reserved word, keyword)
    - C에서 고유한 문법 및 의미가 정해진 단어
        - 정해진 용도가 아닌 다른 용도로는 사용할 수 없음.
    - 예약어 종류
        - 자료형 관련 예약어 : `char`, `int`, `float`, `short`, `long`, `double`, `unsigned`, `struct`, `union`, `enum`, `void`, `typeof` 등
        - 기억 관련 예약어 : `auto`, `static`, `extern`, `register`, `volatile`, `sizeof` 등
        - 제어 관련 예약어 : `if`, `else`, `switch`, `case`, `default`, `for`, `while`, `do`, `break`, `continue`, `return` 등
    
- **명칭**(identifier)
    - 프로그램 내의 여러가지 요소를 식별하기 위해 정의함
        - 변수, 함수 등
    - 명칭 정의 규칙
        - 영문자(대·소문자 구분함)와 숫자의 조합으로 만든다.
        - 명칭의 첫 문자는 영문자나 밑줄(`_`)이어야 한다.  
            (*하지만 되도록이면 밑줄로 시작하는 명칭은 만들지 말자!*)
        - 특수문자를 사용할 수 없다. 단, 밑줄은 사용할 수 있다.
        - 문자 사이에 공백이 있어서는 안 된다.
        - 예약어를 사용할 수 없다.
    - 올바르게 정의한 명칭의 예😊👍
        - `myname` : 영문자로 구성된 명칭
        - `myName` : myname과 다른 명칭(Camel case)
        - `MyName` : myname과 다른 명칭(Pascal case)
        - `my_name` : 밑줄 사용 가능(snake case)
        - `flag01` : 영문자와 숫자 조합 가능
        - `For` : 사용 가능✨(예약어 for와는 구분됨)
    - 잘못된 명칭의 예💣☠️
        - `my name` : 문자 사이 공백 사용 불가
        - `my#name` : 특수문자 사용 불가
        - `my-name` : 툭수문자(연산 기호) 사용 불가
        - `4days` : 숫자로 시작 불가
        - `auto` : 예약어 사용 불가

- **상수**(constant)
    - 수치 상수(123)
    - 문자 상수('a')
    - 문자열 상수("KNOU")

- **연산자**(operator)
    - 여러가지 유형의 연산을 표현함
        - 산술 연산
        - 관계 연산
        - 논리 연산
        - 비트 연산
        - 대입 연산  

          등
    - 연산의 대상을 피연산자라고 함
        - 연산의 종류에 따라 1~3개의 피연산자가 사용됨.

- **설명문**(comment, 주석문)
    - 프로그램에 대한 설명을 작성하는 문장
        - 임의의 형식으로 작성하며, 컴파일러는 설명문의 영역은 무시함.
    - 작성 방법
        - `/*`와 `*/`사이에 작성한 모든 문장은 설명문임.  
            ▶️ 여러 줄에 걸친 긴 설명문을 작성할 때 편리함.
        - `//` 기호 이후의 문장은 그 행의 끝까지 설명문임.  
            ▶️ 간단한 설명문을 작성할 때 편리함.

## 4. 에러와 경고

### 에러(error)
- 프로그램을 정상적으로 빌드할 수 없는 문제가 포함된 소스 코드의 경우 에러 메세지를 출력함.
    - C 언어의 문법에 맞지 않는 형식의 문장을 사용한 경우
    - 반드시 필요한 요소가 누락된 경우
- 에러 발생 시 빌드가 중지되어 목적 코드 및 실행 파일이 생성되지 않음.
    - 에러 메시지를 확인하여 반드시 수정해야 함.

### 경고(warning)
- 빌드를 진행할 수는 있지만, 문제 발생 가능성이 있는 소스 코드를 작성한 경우
    - 사용하지 않는 변수나 함수를 정의한 경우
    - 오차가 발생할 수 있는 문장 등
- 경고가 있더라도 실행 파일은 생성되며, 프로그램을 실행할 수 있음
- 경고 메시지의 내용을 파악하여 필요한 경우에는 적절히 수정하며, 아무런 문제가 없는 경고는 무시할 수 있음.

### 에러가 발생한 코드의 사례

- 에러가 발생한 코드의 사례 1️⃣
    ```c
    #include <stdio.h>

    int main() 
    {
        printf("Hello~\n")
    }
    ```
    ➡️ 
    ```txt
    Compiling single file...
    --------
    - Filename: C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c
    - Compiler Name: TDM-GCC 9.2.0 64-bit Release

    Processing C source file...
    --------
    - C Compiler: C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin\gcc.exe
    - Command: gcc.exe "C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c" -o "C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.exe" -fexec-charset=cp949 -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\include" -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\x86_64-w64-mingw32\include" -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\lib\gcc\x86_64-w64-mingw32\9.2.0\include" -L"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\lib" -L"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\x86_64-w64-mingw32\lib" -static-libgcc
    C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c: In function 'main':
    C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c:5:23: error: expected ';' before '}' token
        5 |     printf("Hello~\n")
        |                       ^
        |                       ;
        6 | }
        | ~                      

    Compilation results...
    --------
    - Errors: 1
    - Warnings: 0
    - Compilation Time: 0.11s
    ```

    printf() 함수 실행 후, 세미콜론(`;`)을 붙여 주지 않아 구문 오류 발생!  

    수정해보자.
    ```c
    #include <stdio.h>

    int main() 
    {
        printf(Hello~\n);
    }
    ```

    ![세미콜론을 붙이지 않아 발생한 구문 오류 수정 결과 Hello~가 정상적으로 출력된 것을 확인할 수 있습니다.](/KNOU/C_Programming/lecture01/image/error_correction_result.png)

<br>

- 에러가 발생한 코드의 사례 2️⃣

    ```c
    #include <stdio.h>

    int main() 
    {
        print("Hello~\n");
    }
    ```
    ➡️
    ```txt
    Compiling single file...
    --------
    - Filename: C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c
    - Compiler Name: TDM-GCC 9.2.0 64-bit Release

    Processing C source file...
    --------
    - C Compiler: C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\bin\gcc.exe
    - Command: gcc.exe "C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c" -o "C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.exe" -fexec-charset=cp949 -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\include" -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\x86_64-w64-mingw32\include" -I"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\lib\gcc\x86_64-w64-mingw32\9.2.0\include" -L"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\lib" -L"C:\Program Files (x86)\Embarcadero\Dev-Cpp\TDM-GCC-64\x86_64-w64-mingw32\lib" -static-libgcc
    C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c: In function 'main':
    C:\Users\minju\Programming\KNOU\C_Programming\lecture01\error_example.c:5:5: warning: implicit declaration of function 'print'; did you mean 'printf'? [-Wimplicit-function-declaration]
        5 |     print("Hello~\n");
        |     ^~~~~
        |     printf
    C:/Program Files (x86)/Embarcadero/Dev-Cpp/TDM-GCC-64/bin/../lib/gcc/x86_64-w64-mingw32/9.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:\Users\minju\AppData\Local\Temp\ccM2WyQY.o:error_example.c:(.text+0x15): undefined reference to `print'

    collect2.exe: error: ld returned 1 exit status

    Compilation results...
    --------
    - Errors: 1
    - Warnings: 1
    - Compilation Time: 0.23s
    ```

    정의되지 않은 함수 `print()`를 사용하여 경고와 에러가 1개씩 발생!  

    
---
---
## 정리하기
- C언어는 범용 고급언어이면서 저급언어 수준의 특성이 있어 시스템 프로그래밍에 적합한 언어이다.
- C프로그램은 소스 파일을 작성한 다음 컴파일과 링크 과정을 통해 실행 파일로 변환된다.
    - *컴파일과 링크 과정을 묶어 빌드 과정이라고 한다.*
- C프로그램 개발에 필요한 도구를 모아 놓은 통합개발환경(IDE)을 이용하여 편리하게 프로그램을 작성할 수 있다.
- C프로그램은 1개 이상의 함수로 구성되며, 기본적으로 main()함수를 작성한다.
- C프로그램은 예약어, 명칭, 상수, 문자열, 구두점, 설명문 등의 토큰을 문법과 의미에 맞게 나열하여 작성한다.
- 작성된 프로그램의 빌드 과정에서 에러나 경고가 나올 수 있다.
- 에러는 반드시 수정하여야 하며,  
경고는 잘 확인한 후 필요하다면 적절히 수정하여 가급적 경고 메시지가 나오지 않게 하는 것이 바람직하다.


<br>

> 다음 시간 안내  
> [02강. 자료형과 선행처리기](../lecture02/readme.md)