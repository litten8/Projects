print("pi calc 1 number");
x=int(input());
sigma=0;
for i in range(1,x+1):
    sigma+=(1/i)**2;
print((sigma*6)**(1/2));
