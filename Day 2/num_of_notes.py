#def find_notes(num):
    #d={}
    #notes=[2000,500,200,100,50,20,10,5,2,1]
    #for i in notes:
        #c=num//i
        #d[i]=c
        #if c>0:
            #num=num%i
    #return d

def f(num):
    d={}
    if num>=2000:
        d[2000]=num//2000
        num=num%2000
    if num>=500 and num<2000:
        d[500]=num//500
        num=num%500
    if num>=200 and num<500:
        d[200]=num//200
        num=num%200
    if num>=100 and num<200:
        d[100]= num//100
        num=num%100
    if num>=50 and num<100:
        d[50]=num//50
        num=num%50
    if num>=20 and num<50:
        d[20]=num//20
        num=num%20
    if num>=10 and num<20:
        d[10]=num//10
        num=num%10
    if num>=5 and num<10:
        d[5]=num//5
        num=num%5
    if num>=2 and num<5:
        d[2]=num//2
    if num==1:
        d[1]=1
    return d
print(f(5628))
        