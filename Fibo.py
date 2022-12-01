# recursive implementation of Fibonacci with Time complexity of O(n) and Space complexity of O(n)

def fib(N : int, a: int = 0,b: int = 1,sum: int = 1 ) -> int:
 
    #check if it reached the base condition
    if (N != 0) :
        
        #print each number 
        print(a ,end = " ")
        #calculate the next
        sum = a + b
        a = b
        b = sum
        #decrease the condition value 
        N -= 1
        #call the function with new values
        fib(N,a, b, sum)
#prints first Nth number of the Fibonacci
fib(500)
