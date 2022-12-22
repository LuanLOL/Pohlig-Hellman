# Pohlig-Hellman

This is an implementation of Pohlig-Hellman's algorithm to solve discrete logs. 

Helper functions were converted from MATLAB implementations from code bank within:

"Introduction to Cryptography with Coding Theory, 3rd Edition" by Wade Trappe and Lawrence Washington

First, I found all of the prime factors that make up p-1 and split it up into two lists: the actual prime (this will be all q's we are testing) and how many times that prime is used. 
