def main():
    P = 45
    print("The value of P:", P)
    G = 7
    print("The value of G:", G)
    # a  private key
    a = 37
    print("The private key of Alice:", a)
    x = pow(G, a) % P

    b = 308
    print("The private key b for Bob:", b)
    y = pow(G, b) % P
    ka = pow(y, a) % P  
    kb = pow(x, b) % P

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
