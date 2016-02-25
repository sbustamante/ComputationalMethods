import numpy as np
import matplotlib.pylab as plt 

def Temp(x,y):
    return x**3 + 3*x-1+y**2 

def EPT( f,i, h=0.01,der=0 ):
    suma = -3*f[i]+4*f[i+(-1)**der*1]-f[i+(-1)**der*2]
    return suma/(2*h*(-1)**der)
  
def MPT( f,i, h = 0.01 ):    
    return (f[i+1]-f[i-1])/(2*h)

k = 1
X = np.linspace(1,10,100)
Y = np.linspace(0,50,100)
Tx = Temp(X,0)
Ty = Temp(0,Y)

Qx = np.zeros(len(X))
Qy = np.zeros(len(Y))
index_x = len(X)-1
index_y = len(Y)-1

Qx[0] = EPT( Tx,0 )    
Qy[0] = EPT( Ty,0 )    
i = np.arange( 1,index_x )
j = np.arange( 1,index_y )
Qx[1:-1] =  MPT( Tx,i )
Qy[1:-1] =  MPT( Ty,j )
Qx[-1] = EPT( Tx,index_x,der=1 ) 
Qy[-1] = EPT( Ty,index_y,der=1 ) 

Xm,Ym = plt.meshgrid(X,Y)
Qx,Qy = plt.meshgrid(Qx,Qy)
Q = k*np.sqrt(Qx**2+Qy**2)
plt.figure(figsize=(10,10))
plt.imshow(Q)
plt.colorbar(orientation="vertical",shrink=0.89)
plt.title("Color Map Density Flux Heat")
plt.show()