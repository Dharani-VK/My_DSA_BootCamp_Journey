#Problem Statement
"""
Given a number N. Your task is to create a program to calculate the N-th term of the Alice choice.

Alice's sequence consists of the squares of prime numbers: 2^2, 3^2, 5^2, 7^2, 11^2,13^2,17^2,19^2, 23^2, 29^2,…………

Input Format
The first line should contain only one line input given as number N.

Output Format
Output the square of the prime number at the N-th position in the sequence.

Constraints
1 <= N <= 10^5

Sample Testcase 0
Testcase Input
10
Testcase Output
841
Explanation
The Nth term is 841 It is one-based indexing, and by observing the pattern of the sequence then, all numbers are prime numbers and have to calculate the 10th term. So, The 10th number is 29, and its square is 841.

Sample Testcase 1
Testcase Input
3
Testcase Output
25
Explanation
The Nth term is 25 It is one-based indexing, and by observing the pattern of the sequence then, all numbers are prime numbers and have to calculate the 3rd term. 
So, the 3rd number is 5, and its square is 5^2 is 25. 
Sequence: 2, 3, 5 
Index.       : 1, 2, 3
"""

from math import log
# Enter your code here. Read input from STDIN. Print output to STDOUT
def sieve(limit):
  is_prime = [True] *(limit+1)
  is_prime[0] = is_prime[1] = False

  for i in range(2 , int(limit**0.5)+1):
    if is_prime[i]:
      for j in range( i*i , limit+1 , i):
        is_prime[j] = False
  
  prime = [i for i , val in enumerate(is_prime) if val]
  return prime


n = int(input())
if n <= 6:
  limit = 17
else:
  limit = int(n*(log(n) + log(log(n))))
finding = sieve(limit)
nth_prime = finding[n-1]
result = nth_prime ** 2
print(result)
