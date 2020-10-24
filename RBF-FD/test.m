%test functions in octave


S=[90,100,110]; K=100; T=1.0; r=0.03; sig=0.15;
U=[10.726486710094511 4.820608184813253 1.828207584020458];
x=BSeuCallUII_RBFFD(S,K,T,r,sig);

disp(x);


