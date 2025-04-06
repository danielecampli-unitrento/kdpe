# The Hogwarts quests

1. [Written problems](#1-written-problems)
	1. [The Express measurement](#11-the-express-measurement)
	2. [The Owlery conundrum](#12-the-owlery-conundrum)
	3. [The gnomic uplifting](#13-the-gnomic-uplifting)
	4. [The Hogwarts visitors](#14-the-hogwarts-visitors)
	5. [The Witchcraft houses leveling](#15-the-witchcraft-houses-leveling)
	6. [Magic and marginal densities](#16-magic-and-marginal-densities)
	7. [The McGonagall's award](#17-the-mcgonagalls-award)


> [!IMPORTANT]
> **Disclaimer: AI tools assistance**
> Some problems were solved with the help of AI tools.

> [!WARNING]
> **Warning: unreviewed document**
>  The following exercises have not been reviewed by expert humans; be aware their solutions can contain mistakes.

## 1. Written problems
### 1.1. The Express measurement
You are tracking the distance to the Hogwarts Express. A magical instrument reports it’s $100$ leagues away. Before the reading, your belief about the distance $D$ was a Gaussian $D ∼ \mathcal{N}(µ = 98, σ^2 = 16)$. The instrument’s reading is the true distance plus Gaussian noise $\mathcal{N}(0, 4)$.
1. What is the PDF of your prior belief of the train’s true distance?
2. What is the PDF of seeing a reading of $100$ leagues, given the true distance is $t$?
3. What is the PDF of your posterior belief (after the reading) of the train’s true distance? (You can leave a constant and don’t need to simplify).

**Solutions**
1. **Answer**: $\mathcal{P}(d)\sim$ $\mathcal{N}(\mu=98, \sigma^2=16)=$ $\frac{1}{\sqrt{2\pi \sigma^2}}\exp\left(-\frac{(d-\mu)^2}{2\sigma^2}\right)$
   The prior belief on the train true distance, $\mathcal{P}(d)$, is given by the probability density function of a normal distribution of mean $\mu=98$ and and variance $\sigma^2=16$.
2. **Answer**:  $\mathcal{P}(d=100|t)\sim\mathcal{N}(\mu=100,\sigma^2=4)$ $=\frac{1}{\sqrt{ 8\pi }}\exp\left( -\frac{(100-t)^2}{8} \right)$
   The true distance $t$ is a measurement that can be though as the result of estimating the mean of the underlying, true distribution, and then applying a perturbation modelled as stated in the problem description, i.e. a normal distribution $\mathcal{N}=(\mu=0,\sigma^2=4)$. Using the properties of the normal distributions, we can respectively sum their mean and variances in order to model a new, normal distribution which account for the true distance plus the noise density estimation. In other words, we know that $\mathcal{T}(d)=\mathcal{N}(\mu=t,\sigma^2=0)$ -that is, a normal distribution of mean equal to $t$ and with no variance, to account for "the true value $t$" condition-, while the noise has density $\epsilon(d)=\mathcal{N}(\mu=d,\sigma^2=4)$. Summing them up, we obtain the density of every possible measurement $\mathcal{M}(d)\sim$ $\mathcal{T}(d)+\epsilon(d)\sim$ $\mathcal{N}(\mu=t, \sigma^2=0+4=4)$. In particular, in this case the distance $d=100$, hence we can finally compute the final solution: $\mathcal{M(d=100)}\sim\mathcal{N}(\mu=100,\sigma^2=4)$ $=\frac{1}{\sqrt{ 8\pi }}\exp\left( -\frac{(100-t)^2}{8} \right)$.
3. **Answer**: $\mathcal{P}(t|d) = \frac{\mathcal{P}(d=100|t)\mathcal{P(d=100)}}{\mathcal{P(t)}}$
   We want to calculate the posterior $R(d)$ after the reading $d=100$, given that the true distance is $t$. In notation, we want to calculate $\mathcal{P}(d|t)$, and this can be accomplished using the Bayes' theorem: $\mathcal{P}(t|d)=\frac{\mathcal{P}(d|t)\mathcal{P}(d)}{\mathcal{P(t)}}$. We have already calculated all the components of the numerator, since in the first exercise we have calculated $P(d)$, while in the second one we estimated $P(d=100|t)$, where $d=100$ is our measurement. In this case the true distribution $\mathcal{P}(t)$ is not given, but we can leave it just indicated and finally solve in a symbolic way the whole exercise: $$\begin{aligned}\mathcal{P}(t|d) &= \frac{\mathcal{P}(d=100|t)\mathcal{P(d=100)}}{\mathcal{P(t)}}\\&= \frac{1}{\sqrt{ 8\pi }}\exp\left( -\frac{(100-t)^{2}}{8} \right)\cdot \frac{1}{\sqrt{ 32\pi }}\exp\left( -\frac{(100-98)^2}{32} \right)\cdot \mathcal{P}(t)^{-1}\end{aligned}$$

### 1.2. The Owlery conundrum
On average, $5.5$ owls arrive at the Owlery per minute. What is the probability that:
1. More than $7$ owls will arrive in the next minute?
2. More than $13$ owls will arrive in the next $2$ minutes?
3. More than $15$ owls will arrive in the next $3$ minutes?

**Solutions**
1. **Answer**: $\mathcal{Poi(\lambda=5.5, x>7)} = 1- \sum^{7}_{i=0}\frac{e^{-7}7^i}{i!}$
   The problem can be solved by the means of a Poisson distribution estimation:  we want to calculate $\mathcal{Poi}(\lambda=5.5,x>7)$. In order to achieve this, we can compute the inverse of a finite sum to find the final solution to the problem: 
   $$\begin{aligned}
   \mathcal{Poi(\lambda=5.5, x>7)} &= \\
   &=1-\mathcal{Poi}\left(\lambda=5.5, x\leq 7 \right) \\
   &=1-\sum^{7}_{i=0}\mathcal{Poi(\lambda=5.5,x=i)} \\
   &= 1- \sum^{7}_{i=0}\frac{e^{-\lambda}\lambda^i}{i!} \\
   &= 1- \sum^{7}_{i=0}\frac{e^{-7}7^i}{i!}
   \end{aligned}$$
2. **Answer**: $\mathcal{Poi}(\lambda=11,x>13)=$ $1 - \sum^{13}_{i=0} \frac{e^{-11}11^i}{i!}$
   The solution to this problem is similar to that of the previous one, but we have to adjust for 1. $x>13$ and 2. the timeframe is not $1$ minute, but $2$. To achieve the second condition, we have to choices: multiply the final probability by 2, or double the average $\lambda=5.5 \to \lambda \cdot 2= 11$; the answer will not vary, so we choose the latter way in order to tide up a bit the whole notation. The following is the final solution: $$\begin{aligned}
	\mathcal{Poi}(\lambda=11,x>13) &= \\
		&= 1 - \mathcal{Poi}(\lambda=11,x \leq 13) \\
		&= 1 - \sum^{13}_{i=0} \mathcal{Poi}(\lambda=11, x=i) \\
		&= 1 - \sum^{13}_{i=0} \frac{e^{-\lambda}\lambda^{i}}{i!} \\
		&= 1 - \sum^{13}_{i=0} \frac{e^{-11}11^i}{i!} \\
		
\end{aligned}$$
3. **Answer**: $\mathcal{Poi}(\lambda=16.5,x>15)=$ $1 - \sum^{15}_{i=0} \frac{e^{-16.5}16.5^i}{i!}$
   The solution can be calculated exactly like in the previous exercise:
   $$
   \begin{aligned}
	\mathcal{Poi}(\lambda=16.5,x>15) &= \\
		&= 1 - \mathcal{Poi}(\lambda=16.5,x\leq 15) \\
			&= 1 - \sum^{15}_{i=0}\mathcal{Poi}(\lambda=16.5,x=i) \\
			&= 1 - \sum^{15}_{i=0} \frac{e^{-\lambda}\lambda^{i}}{i!} \\
			&=1 - \sum^{15}_{i=0} \frac{e^{-16.5}16.5^i}{i!}
\end{aligned}$$

### 1.3. The gnomic uplifting
The median $m$ of a continuous random variable $X$ (like the height of a gnome) having cumulative distribution function $\mathcal{F}$ is the value $m$ such that $\mathcal{F}(m) = 0.5$. Find the median of $X$ in terms of distribution parameters) if:
1. $X ∼ \mathcal{Uni}(a, b)$ (Uniform distribution, like the spread of Floo powder).
2. $X ∼ \mathcal{N}(µ, σ^2)$ (Normal distribution, like scores on the O.W.L.s).

**Solutions**
1. **Answer**: $m=\frac{1}{2}(a+b)$
   The CDF of a uniform distribution is defined as follows: 
   $$\mathcal{F}(x)= \begin{cases}0 & x<a \\
\frac{x-a}{b-a} & a\leq x \leq b \\
1 & x > b \end{cases}$$
   In this case we have $\mathcal{F}(x=m)=0.5$, hence we are considering the case $\mathcal{F}(x=m)=\frac{m-a}{b-a}$, when the median is between $a$ and $b$. Now we have to solve $\frac{m-a}{b-a}=\frac{1}{2}$ $\implies$ $m=\frac{a+b}{2}$, which is also our final answer. The answer reflects the general property of a uniform distribution in the range $[a,b]$, where the median is equal to the mean.
2. **Answer**: $m=\mu$
   The CDF of a normal distribution is defined as follows: $$ \Phi\left( \frac{x-\mu}{\sigma} \right) = \frac{1}{\sqrt{ 2\pi }}\int^{x}_{-\infty}e^{-\frac{1}{2}t^{2}}dt=\frac{1}{2}\left[ 1+erf\left( \frac{x-\mu}{\sigma\sqrt{ 2 }} \right) \right]$$
   Where the $erf(x)$ function is defined as $$erf(x)=\frac{1}{\sqrt{ \pi }}\int_{-x}^{x} e^{-t^2}dt$$
   When we deal with a normal distribution, the mean and the median coincides; in fact, if we fix  $\mu=m$, we obtain that $erf(x) = 0$ (trivial to see), and $\Phi(x=m)=\frac{1}{2}$, which is the exact condition we have to work with from the beginning. The answer is then $m=\mu$.

### 1.4. The Hogwarts visitors
Let $X_i$ be the number of students visiting the Hogwarts library in week $i$, where $X_i ∼ \mathcal{N}(2200, 52900)$. Assume weekly visits $X_i$ are independent.  
1. What is the probability that the total number of visitors in the next two weeks exceeds $5000$? 
2. What is the probability that the weekly number of visitors exceeds $2000$ in at least $2$ of the next $3$ weeks?

**Solutions**
1. **Answer**: $\mathbb{P}(X_{i}+X_{i+1}> 5000)$
   $= \sum_{i=0}^{5000}\frac{1}{\sqrt{ 211600\pi }}\exp\left( -\frac{(i-4400)^2}{211600} \right)$ $=1-\Phi\left( \frac{5000-4400}{\sqrt{ 105800 }} \right)$
   We want to calculate the probability $\mathbb{P}(X_{i}+X_{i+1}< 5000)$, where $X_{i},X_{i+1}\sim \mathcal{N}(2200,52900)$, and are two independent random variables. First, we can state that $\mathbb{P}(X_{i}+X_{i+1}>5000) = 1 - \mathbb{P}(X_{i}+X_{i+1}\leq 5000)$. The sum of independent normally distributed variables is also a normal distribution, with the mean equal to the sum of the singular means, and variance equal to the sum of the standalone variances. This translates into the following: $$X_i+X_{i+1} \sim \mathcal{N}(\mu=4400, \sigma^2=105800)$$
   The answer to the problem is then just a sum of density estimates, like shown below: $$\begin{aligned}
\mathbb{P}(X_{i}+X_{i+1}> 5000) &= \\
&= 1-\mathbb{P}(X_{i}+X_{i+1}\leq 5000) \\
&= 1-\sum^{5000}_{i=0} \mathcal{N}(x=i; \mu=4400, \sigma^{2}=105800)\\
&= 1-\sum_{i=0}^{5000} \frac{1}{\sqrt{ 2\pi \sigma^2 }}\exp\left( -\frac{(i-\mu)^2}{2\sigma^2} \right)\\
&= 1-\sum_{i=0}^{5000}\frac{1}{\sqrt{ 211600\pi }}\exp\left( -\frac{(i-4400)^2}{211600} \right)
\end{aligned}$$
The same solution can be derived using the CDF of a normal distribution, simplifying a bit the overall notation: $$\mathbb{P}(X_{i}+X_{i+1}>5000)=1 - \Phi\left(\frac{5000-\mu}{\sigma} \right)=1-\Phi\left( \frac{5000-4400}{\sqrt{ 105800 }} \right)$$
2. **Answer**: ${3 \choose 2} \alpha^{2}(1-\alpha)^1+ {3 \choose 3}\alpha^{3}(1-a)^{0}$, with $\alpha = 1-\Phi\left( \frac{2000-4400}{\sqrt{ 105800 }} \right)$
   Suppose we already know the probability of having a week where the number of visitors exceeds 2000, i.e. $\alpha=\mathbb{P}(X_{i}>2000)$; since we want to calculate the probability that the same happens in two out of three weeks, we can model the situation using a binomial distribution. In practice, let's call $W$ a variable having values in $\{0,1,2,3\}$, indicating the numbers of weeks where the 2000 visitors threshold has been exceeded. As already stated, $W \sim Bin(n,k)$, with $k \in \{0,1,2,3\}$ and $n=3$. We are interested in calculating $\mathbb{P}(W\geq 2)=\mathbb{P}(W=2)+\mathbb{P}(W=3)$ given the probability measure $\alpha$ we have already assumed to have. Of course, this is not the case, so let's calculate such probability using the same technique adopted in the preceding problem: $$
   \begin{aligned}
\alpha = \mathbb{P}(X_{i}>2000) &= \\
&= 1 - \mathbb{P}(X_{i}\leq 2000) \\
&= 1 - \sum_{i=0}^{2000} \mathcal{N}(x=i; \mu=2200; \sigma^{2=52900)}\\
&= 1 - \sum_{i=0}^{2000} \frac{1}{\sqrt{ 2\pi \sigma^2 }}\exp\left( -\frac{(i-\mu)^2}{2\sigma^2} \right)\\
&= 1 - \sum_{i=1}^{2000} \frac{1}{\sqrt{ 21600\pi }}\exp\left( -\frac{(i-4400)^2}{211600} \right)\\
&=1 - \Phi\left(\frac{2000-\mu}{\sigma} \right)\\
&=1-\Phi\left( \frac{2000-4400}{\sqrt{ 105800 }} \right)
\end{aligned}$$
Wrapping everything together using the binomial modelling explained above, the wanted probability is the following: $$\mathbb{P}(W\geq 2) ={3 \choose 2} \alpha^{2}(1-\alpha)^1+ {3 \choose 3}\alpha^{3}(1-a)^{0}$$
### 1.5. The Witchcraft houses levelling
Let $X,Y$ and $Z$ be independent random variables representing the magical power levels of three Hogwarts students, where $X \sim \mathcal{N}(\mu_1,\sigma^2_{1})$ (Gryffindor), $Y \sim \mathcal{N}(\mu_2,\sigma^2_{2})$ (Hufflepuff), and $Z \sim \mathcal{N}(\mu_{3}, \sigma^2_{3})$ (Ravenclaw).
1. Let $A=X+Y$. What is the distribution of the combined power $A$?
2. Let $B=5X+2$. What is the distribution of $B$ (perhaps after a power-enhancing charm)?
3. Let $C=aX-bY+c^2Z$, where $a,b,c$ are real-valued constants representing spell modifiers. What is the distribution (and parameters) for $C$? Show how you derived your answer.

**Solutions**
1. **Answer**: $A=X+Y \implies A \sim \mathcal{N}(\mu_{1}+\mu_{2},\sigma^2_{1}+\sigma^2_{2})$
   The answer is pretty straightforward, since the sum of two normal distribution is still a normal distribution on mean equal to the sum of single means, and variance equal to the sum of single variances: $$A=X+Y \implies A \sim \mathcal{N}(\mu_{1}+\mu_{2},\sigma^2_{1}+\sigma^2_{2})$$
2. **Answer**: $B \sim \mathcal{N}(5\mu_{1}+2,\ 25\sigma^2_{1})$
   Both the mean and the variance are linear maps, and we can use their properties to derive the form of B, that of course will still be a normal distribution. $$\begin{aligned}\mathbb{E}[B]&=\mathbb{E}[X+5]=5\mathbb{E}[X]+2 \\ &= 5\mu_{1}+2\\ Var(B)&=Var(5X+2)=5^{2}Var(X)=25Var(X)\\&=25\sigma^2_{1}\end{aligned}$$
   The conclusive answer follows immediately: $$B \sim \mathcal{N}(5\mu_{1}+2,\ 25\sigma^2_{1})$$
3. **Answer**: $C \sim \mathcal{N}(a\mu_{1}-b\mu_{2}+c^{2}\mu_{3},\ a^2\sigma_{1}^2+b^2\sigma^2_{2}+c^4\sigma^2_{3} )$
   The answer can be calculated exactly like in the previous exercise, like just a little bit more of effort in computations. $$\begin{aligned}
\mathbb{E}[C]&=\mathbb{E}[aX-bY+c^2Z]=a\mathbb{E}[X]-b\mathbb{E}[Y]+c^{2}\mathbb{E}[Z]\\
&= a\mu_{1}-b\mu_{2}+c^{2}\mu_{3}\\
Var(C) &= Var(aX-bY+c^2Z)=a^2Var(X)+b^2Var(Y)+c^4Var(Z)\\
&=a^2\sigma_{1}^2+b^2\sigma^2_{2}+c^4\sigma^2_{3}
\end{aligned}$$The answer is then: $$C \sim \mathcal{N}(a\mu_{1}-b\mu_{2}+c^{2}\mu_{3},\ a^2\sigma_{1}^2+b^2\sigma^2_{2}+c^4\sigma^2_{3} )$$
   

### 1.6. Magic and marginal densities
The joint probability density function of continuous random variables $X$ (skill in Potions) and $Y$ (skill in Charms) is given by $f_{X,Y}(x,y)=c\frac{y}{x}$ where $0 < y < x < 1$.  
1. What is the value of $c$ for this to be a valid probability density function?  
2. Are Potion skill ($X$) and Charm skill ($Y$) independent? Explain.  
3. What is the marginal density function of $X$?
4. What is the marginal density function of $Y$?

**Solutions**
1. **Answer**: $c=4$ (we are deliberating ignoring $c=4+k$, putting $k=0$).
   A probability density function still models a probability, so its codomain must be confined between $[0,1]$. We can calculate the value of $c$ calculation the integral of the joint density function: $$\int_{0}^{1}\int_{0}^{x}c \frac{y}{x}dydx=1$$With a bit of calculations we get the following: $$\int_{0}^{1}\left[ c \frac{y^2}{2x} \right]^{y=x}_{{y=0}}dx=\int_{0}^{1}\left( c \frac{x^2}{2x}-0 \right)dx=\int_{0}^{1}c\frac{x}{2}dx=\left[ \frac{cx^2}{4} \right]_{x=0}^{x=1}=\frac{c}{4}+k=1$$Ignoring the constant $k$, we have $c=4$.
2. **Answer**: No, since the product of the marginal distribution is different from the joint density.
   After having solved exercise 3 and 4, we can say that $X$ and $Y$ are not independent, since the product of their marginal densities is not equal to the join density given as assumption. In particular, we have the following justifying the answer: $$f_{X,Y}(x,y)=c \frac{y}{x} \neq 2x-4y\ln(y)+k=f_{X}(x)f_{Y}(y)$$
3. **Answer**: $$f_{X}(x)= \begin{cases}
2x+k_{1} &0<x<1 \\ \\
0 & \text{otherwise}
\end{cases}$$
   The marginal density function of $X$ can be obtained by integrating the joint PDF with respect to $y$ over the range $(-\infty,+\infty)$, for a fixed $x$: $$f_X(x)=\int^{+\infty}_{-\infty}f_{X,Y}(x,y)dy=\int^{x}_{0}4 \frac{y}{x}dy=2x+k$$
   We limited the integration only to the range where $x$ applies, given as assumption. In the more general case, the marginal density function of $X$ is equal to: $$f_{X}(x)= \begin{cases}
2x+k_{1} &0<x<1 \\ \\
0 & \text{otherwise}
\end{cases}$$
4. **Answer**:  $$f_{X}(x)= \begin{cases}
-4y\ln(y)+k_{2} &0<y<1 \\ \\
0 & \text{otherwise}
\end{cases}$$
   The marginal density function of $Y$ can be obtained by integrating the joint PDF with respect to $x$ over the range $(-\infty,+\infty)$, for a fixed $x$: $$f_X(x)=\int^{+\infty}_{-\infty}f_{X,Y}(x,y)dy=\int^{1}_{y}4 \frac{y}{x}dy=-4y\ln(y)+k_{2}$$
   We limited the integration only to the range where $x$ applies, given as assumption. In the more general case, the marginal density function of $X$ is equal to: $$f_{X}(x)= \begin{cases}
-4y\ln(y)+k_{2} &0<y<1 \\ \\
0 & \text{otherwise}
\end{cases}$$

### 1.7. The McGonagall's award
Choose a number $X$ at random from the set of house points $\{1,2,3,4,5,6\}$ awarded by Professor McGonagall. Now choose a number $Y$ at random from the subset of points no larger than $X$, $\{1,\ldots,X\}$.
1. Determine the joint probability mass function of $X$ (initial points) and $Y$ (second random selection).
2. Determine the conditional mass function $\mathbb{P}(X=j|Y=i)$ as a function of $i$ and $j$.
3. Are $X$ and $Y$ independent? Explain.

**Solutions**
1. **Answer**: $$\mathbb{P}(X=x,Y=y)=\begin{cases}
\frac{1}{6x} &x \in \{1,\ldots,6\},\ y \in \{1,\ldots,x\} \\
0 & \text{otherwise}
\end{cases}$$
   We assume that we can pick a random number from $1$ to $6$ with equal probability. This means that we have to deal with a uniform distribution, and that $\forall x |\ x\in \{1,2,3,4,5,6\}$, $\mathbb{P}(X=x)=\frac{1}{6}$. But what is the probability $\mathbb{P}(Y=y)=?$ If we take a number $x$, let's say 4, then the remaining valid choices for $y$ would be $1,2,3,4$, because $y\leq x$. This means that $\mathbb{P}(Y=y)=\frac{1}{x}$, for every $y \in \{1,2,3,4,5,6\}$.
   The joint probability is then $\frac{1}{x} \cdot \frac{1}{6}=\frac{1}{6x}$, and in general can be defined as follows: $$\mathbb{P}(X=x,Y=y)=\begin{cases}
\frac{1}{6x} &x \in \{1,\ldots,6\},\ y \in \{1,\ldots,x\} \\
0 & \text{otherwise}
\end{cases}$$
2. **Answer**: $$\mathbb{P}(X=j,Y=i)=\begin{cases} \frac{j^{-1}}{\sum_{x=i}^{6} \frac{1}{6x}} &j \in \{i,\ldots,6\}\\ \\
0 & \text{otherwise}

\end{cases}$$
   The conditional mass function can be expressed as: $$\mathbb{P}(X=j|Y=i)=\frac{\mathbb{P}(Y=i|X=j)\mathbb{P}(X=j)}{\mathbb{P}(Y=i)}=\frac{\mathbb{P}(X=j,Y=i)}{\mathbb{P}(Y=i)}$$The numerator has already been calculated in the previous problem, so we just need to calculate the denominator. This is just a simple sum over all the possible values that are valid once we have fixed a $y$, i.e. all the values of $x$ such that $x\geq y$: $$\mathbb{P}(Y=i)=\sum_{x=i}^{6} \mathbb{P}(X=x, Y=i)=\sum_{x=i}^{6} \frac{1}{6x}$$
   Hence, the final answer is the following: $$\mathbb{P}(X=j,Y=i)=\begin{cases} \frac{j^{-1}}{\sum_{x=i}^{6} \frac{1}{6x}} &j \in \{i,\ldots,6\}\\ \\
0 & \text{otherwise}

\end{cases}$$
3. **Answer**: No, $X$ and $Y$ are not independent.
   In order to solve the problem we must check if the joint distribution is equal to the product of the marginal ones. $$\mathbb{P}(X=x,Y=y)=\frac{1}{6x}\stackrel{?}{=}{\frac{1}{6}\sum_{y=x}^{6} \frac{1}{6y}}=\mathbb{P}(X=x)\mathbb{P}(Y=y)$$
   We can clearly see that the equality does not hold; for example, with $x=5$ and $y=6$, we have $\frac{1}{30} = \frac{1}{30}+\frac{1}{36}$, which is of course false.
