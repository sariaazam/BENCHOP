args  = argv();
disp(args);
%pa1 = any(args(:) == 'pa1');
%disp(pa1);
disp(args(1,1));
ismember('pa1', args)
