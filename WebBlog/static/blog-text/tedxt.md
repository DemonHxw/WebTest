题目链接：https://atcoder.jp/contests/abc172/tasks/abc172_f

题意：给你$n$堆石子，每堆石子有$a[i]$个。现在两个人玩游戏，每次可以重一推石子中取走$1$个，$2$个，或者把这一堆石子全部取走。现在在游戏开始之前，你可以将第一堆中的若干($1->a[1]-1$)个石子放到第二堆，问你最少放多少个可以保证后手必赢，如果不行的话，输出$-1$。

思路：首先我们知道这是一个$nim$游戏，结论就是$a[1] \bigoplus a[2]\bigoplus a[3] ... \bigoplus a[n]=0$的话，后手必败。所以这一题题意就可以转化成，求解最小的$ans$，使得
$(a[1]-ans) \bigoplus (a[2]+ans)\bigoplus a[3] ... \bigoplus a[n]=0$
那该怎么求呢？$1e12$的数据范围，暴力是不可能的啦...
我们设$A = a[1] - ans,B = a[2] + ans$，这样我们就可以可以知道
$A  \bigoplus B = a[3]  \bigoplus... \bigoplus a[n]=y$
$A+B = a[1] + a[2] = x$

现在就需要一个非常有用的公式$a + b = a \bigoplus b + 2(a \bigwedge b)$

这样我们就可以得到
$$ \left\{
\begin{aligned}
A \bigoplus B  & = & y \\
A \bigwedge B  & = & \frac{(x - y)}2
\end{aligned}
\right.
$$

另$\frac{x-y}{2} = X , y = Y$(只是为了后续书写看起来舒服点)
这里我们就可以看到$x > y$ || $(x - y)$%$2 !=0$，那可定要输出-1。
我们用$X_i,Y_i,A_i,B_i$表示分别表示$X,Y,A,B$第$i$位二进制数，现在我们就是要找到
$A < a[1]$的最大值，可以看到$A_{min} = X$，那我们接下来就看一下$X_i,Y_i$四种情况下$A$的值有啥变化。
$X_i = 1$ && $Y_i = 1$，$A_i,B_i$无解，输出-1；
$X_i = 1$ && $Y_i = 0$，$A_i = 1,B_i = 0$ || $A_i = 0,B_i = 1$，因为我们要让$A$尽量大，我们就要在$A + 2^{i-1} < a[1]$的情况下让$A_i = 1$;
$X_i = 0$ && $Y_i = 1$，$A_i = 1,B_i=1$，$A$值不变；
$X_i = 0$ && $Y_i = 0$，$A_i=0,B_i=0$，$A$值不变；

这样，这道题就可以解出来啦，具体操作详见代码。

AC代码：

```cpp
#define _CRT_SECURE_NO_WARNINGS 1

#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <vector>
#include <cstdio>
#include <string>
#include <iomanip>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define LL long long
#define pii pair<int,int>
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d\n",x)
#define plld(x) printf("%lld\n",x)
#define rep(i,a,b) for(int i = (a) ; i <= (b) ; i++)
#define per(i,a,b) for(int i = (a) ; i >= (b) ; i--)
#define mem(a) memset(a,0,sizeof(a))
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
#define fast_io ios::sync_with_stdio(false)

const LL mod = 1e9 + 7;
const int maxn = 5e5 + 7;
const int INF = 0x3f3f3f3f;
const double pi = acos(-1.0);

int main() {

#ifndef ONLINE_JUDGE
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
	long _begin_time = clock();
#endif

    int n;
    sd(n);
    LL a, b;
    slld(a), slld(b);
    LL sum = a + b;
    LL Xor = 0;
    rep(i,3,n) {
        LL x;
        slld(x);
        Xor ^= x;
    }

    bool flag = false;
    if(sum < Xor || (sum - Xor) % 2 != 0) flag = true;

    LL And = sum - Xor >> 1;
    LL ans = And;
    per(i,60,0) {
        int xx = ((And >> i) & 1LL);
        int yy = ((Xor >> i) & 1LL);
        if(xx && yy) {
            flag = true;
            break;
        }
        if(!xx && yy && ((ans | (1LL << i)) <= a)) {
            ans |= (1LL << i);
        }
    }

    if(!ans || ans > a || flag) puts("-1");
    else plld(a-ans);

#ifndef ONLINE_JUDGE
	long _end_time = clock();
	// cout << "time = " <<  _end_time - _begin_time << endl;
#endif
    return 0;
}
```