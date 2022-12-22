function x = pohlig_hellman(p, a, b)
    factors = factor(p-1);
    qlist = unique(factors);
    counterlist = histcounts(round(double(factors)));
    indices = find(counterlist == 0);
    counterlist(indices) = [];
    counterlist = sym(counterlist);
    masterx = [];
    for index=1:length(qlist)
     q = qlist(index);
     xlist = [];
     prevb = powermod(b, (p-1)/q, p);
     currx = prevb;
     for k=0:q-1
         if (powermod(a, k * ((p-1)/q), p) == currx)
             xlist = [xlist, k];
             break
         end
     end
     % Found x0 and will now continue on to find the rest of the current q’s
     % betas and xs
     prevb = b;
     counter = sym('1');
     while (counter < counterlist(index))
      
         prevb = mod(prevb*powermod(invmodn(powermod(a,xlist(end),p), p), q^(counter-1), p), p);
      
         currx = powermod(prevb, (p-1)/(q^(counter + 1)), p);
         for k=0:q-1
             if (powermod(a, k * ((p-1)/q), p) == currx)
                 xlist = [xlist, k];
                 break
             end
         end
         counter = counter + 1;
     end
     overallx = 0;
     % overallx is the x found for the current modulus
     for j=sym('1'):counterlist(index)
      
         overallx = mod(overallx + (q^(j-1))*xlist(j), q^counterlist(index));
     end
     % masterx holds all of the x for all respective modulus
     masterx = [masterx overallx];
    end
    xforcrt = [];
    for w=1:length(masterx)
     xforcrt = [xforcrt; [masterx(w), qlist(w)^counterlist(w)]];
    end
    % xforcrt holds all x and q^r pairings where r is the number of q that
    % factor into p-1

    x = crt(xforcrt(:, 1).', xforcrt(:, 2).');

end

