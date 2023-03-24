#def sine(x):
def collatz():

     while True:
         try:
            inp = input("Please type a number greater than one or 'quit' to quit ")
            if inp == "quit" or inp == "q" or inp == "Q":
                print("goodbye")
                break
            i = int(inp)
         except ValueError:
             print("value is not an integer, try again")
             continue;
         if i<=1:
             print("you typed",i, ",which is not greater than one")
             continue;
         print("Giving Collatz sequense for", i)
         j = 1;
         while i > 1:
             print("Iteration",j,"results in",i)
             j=j+1
             if i%2==0:
                 i=i//2
                 continue;
             else:
                 i=i*3+1
                 continue;
         print("Iteration", j, "results in 1")

def sine(x):
    sin = x
    for j in range(1,51):
        power = 1
        for y in range(j+2):
            power*=x
        f = 1
        mul = j + 2
        while mul > 0:
            f*=mul
            mul = mul - 1
        nextEl = power/f
        sign = 1
        for k in range(j):
            sign = sign*(-1)
        sin = sin + sign*nextEl
    print(sin)




