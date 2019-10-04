# IMATH Woche 3

## 1. Determinant

$$
{A=\left[\begin{array}{ll}{1} & {2} \\ {3} & {8}\end{array}\right] \quad
D=1 \cdot 8(-2) \cdot 3=2}
$$
$$
{B=\left[\begin{array}{cc}{(1-\lambda)} & {2} \\ {3} & {(8-\lambda)}\end{array}\right] \quad
D=(1-\lambda) \cdot(8-\lambda)-2 \cdot 3=1^{2}-9 \lambda+2}
$$

$$
c=\left|\begin{array}{ccc}{1} & {2} & {2} \\ {0} & {3} & {6} \\ {0} & {0} & {-1}\end{array}\right| \quad
D=1 \cdot 3 \cdot(-1)=-3
$$

## 2. Again: Determinant

### A)

$$
A=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ {2} & {2} & {8} \\ {3} & {3} & {10}\end{array}\right] \begin{array}{cc}{1} & {-1} \\ {2} & {2} \\ {3} & {3}\end{array}
$$

$$
\begin{equation}
\begin{split}
D & =1 \cdot 2 \cdot 10+(-1 \cdot 8 \cdot 3)+2 \cdot 2 \cdot 3-2 \cdot 2 \cdot 3-1 \cdot 8 \cdot 3-(-1 \cdot 2 \cdot 10) \\
& =-8
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
A & =\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
							 {2} & {2} & {8} \\ 
							 {3} & {3} & {10}\end{array}\right] \\

& =\left[\begin{array}{ccc}	{1} & {-1} & {2} \\ 
							{0} & {4} & {4} \\ 
							{3} & {3} & {10}\end{array}\right]\\

& =\left[\begin{array}{ccc}	{1} & {-1} & {2} \\ 
							{0} & {4} & {4} \\ 
							{0} & {6} & {4}\end{array}\right]\\
							
& =\left[\begin{array}{ccc}	{1} & {-1} & {2} \\ 
							{0} & {4} & {4} \\ 
							{0} & {0} & {-2}\end{array}\right]\\
\end{split}
\end{equation}
$$
$$
\begin{equation}
\begin{split}
D & = 1 \cdot 4 \cdot (-2) \\
& = -8
\end{split}
\end{equation}
$$

### B)

$$
B=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
						  {2} & {2} & {4} \\ 
						  {3} & {1} & {6}\end{array}\right]
						  
\begin{array}{cc}		  {1} & {-1} \\ 
						  {2} & {2} \\ 
						  {3} & {1}\end{array}
$$

$$
\begin{equation}
\begin{split}
D & =1 \cdot 2 \cdot 6 +(-1 \cdot 4 \cdot 3)+2 \cdot 2 \cdot 1-2 \cdot 2 \cdot 3-1 \cdot 4 \cdot 1-(-1 \cdot 2 \cdot 6) \\
& =0
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
B&=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
						  {2} & {2} & {4} \\ 
						  {3} & {1} & {6}\end{array}\right] \\
&=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
						  {0} & {4} & {0} \\ 
						  {3} & {1} & {6}\end{array}\right] \\
&=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
						  {0} & {4} & {0} \\ 
						  {0} & {4} & {0}\end{array}\right] \\
&=\left[\begin{array}{ccc}{1} & {-1} & {2} \\ 
						  {0} & {4} & {0} \\ 
						  {0} & {0} & {0}\end{array}\right] \\
						  
\end{split}
\end{equation}
$$
$$
\begin{equation}
\begin{split}
D & = 1 \cdot 4 \cdot 0 \\
& = 0
\end{split}
\end{equation}
$$

## 3. Again: Determinant

$$
\begin{equation}
\begin{split}
\det(A) & =\begin{vmatrix}
		{1} & {-1} & {0} & {0} \\ 
		{-1} & {2} & {-1} & {0} \\  
		{0} & {-1} & {2} & {-1} \\ 
		{0} & {0} & {-1} & {1} \\ 
		\end{vmatrix} \\
		\\
& =1 \cdot\begin{vmatrix}
		
		 {2} & {-1} & {0} \\  
		 {-1} & {2} & {-1} \\ 
		 {0} & {-1} & {1} \\ 
		\end{vmatrix}
  +1 \cdot\begin{vmatrix}		
		 {-1} & {0} & {0} \\  
		 {-1} & {2} & {-1} \\ 
		 {0} & {-1} & {1} \\ 
		\end{vmatrix} \\
		\\
& =2 \cdot\begin{vmatrix}		
		 {2} & {-1} \\  
		 {-1} & {1} \\ 
		\end{vmatrix}
  +1 \cdot\begin{vmatrix}		
		 {-1} & {0} \\  
		 {-1} & {1} \\ 
		\end{vmatrix}
  -1 \cdot\begin{vmatrix}		
		 {2} & {-1} \\  
		 {-1} & {1} \\ 
		\end{vmatrix} \\
		\\
&= 2 \cdot (1) + 1 \cdot  (-1) - 1 \cdot (1)\\
\\
&=0
		
\end{split}
\end{equation}
$$

