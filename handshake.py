# https://www.hackerrank.com/challenges/handshake/problem

# Handshakes = n*(n - 1)/2
# Because each of the n people can shake hands with n - 1 people (they would not shake their own hand)n
# And the handshake between two people is not counted twice. This formula can be used for any number of people.

n = int(input())

handshakes = (n*(n-1))//2

print(handshakes)
