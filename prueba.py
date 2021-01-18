import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
np.random.seed(seed=42)


def create_data():
    x = PolynomialFeatures(degree=6).fit_transform(np.linspace(-2,2,100).reshape(100,-1))
    x[:,1:] = MinMaxScaler(feature_range=(-2,2),copy=False).fit_transform(x[:,1:])
    l = lambda x_i: np.cos(0.8*np.pi*x_i)
    data = l(x[:,1])
    noise = np.random.normal(0,0.1,size=np.shape(data))
    y = data+noise
    y= y.reshape(100,1)
    print(x)
    print(y)
    # Normalize Data
    return {'x':x,'y':y}

def plot_function(x,y,w,Error,w_s):
    fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(40,10))
    ax[0].plot(x[:,1],[np.cos(0.8*np.pi*x_i) for x_i in x[:,1]],c='lightgreen',linewidth=3,zorder=0)
    ax[0].scatter(x[:,1],y)
    ax[0].plot(x[:,1],np.dot(x,w))
    ax[0].set_title('Function')
    ax[1].scatter(range(iterations),Error)
    ax[1].set_title('Error')



    plt.show()



# initialize variables
data = create_data()
x = data['x']
y = data['y']
w = np.random.normal(size=(np.shape(x)[1],1))
eta = 0.1
iterations = 10000
batch = 10



def stochastic_gradient_descent(x,y,w,eta):
    derivative = -(y-np.dot(w.T,x))*x.reshape(np.shape(w))
    return eta*derivative


def batch_gradient_descent(x,y,w,eta):
    derivative = np.sum([-(y[d]-np.dot(w.T.copy(),x[d,:]))*x[d,:].reshape(np.shape(w)) for d in range(len(x))],axis=0)
    return eta*(1/len(x))*derivative


def mini_batch_gradient_descent(x,y,w,eta,batch):
    gradient_sum = np.zeros(shape=np.shape(w))
    for b in range(batch):
        choice = np.random.choice(list(range(len(x))))
        gradient_sum += -(y[choice]-np.dot(w.T,x[choice,:]))*x[choice,:].reshape(np.shape(w))
        return eta*(1/batch)*gradient_sum

# Update w
w_s = []
Error = []
for i in range(iterations):
    # Calculate error
    error = (1/2)*np.sum([(y[i]-np.dot(w.T,x[i,:]))**2 for i in range(len(x))])
    Error.append(error)
    # Stochastic Gradient Descent
    """
    for d in range(len(x)):
        w-= stochastic_gradient_descent(x[d,:],y[d],w,eta)
        w_s.append(w.copy())
    """
    # Minibatch Gradient Descent
    """
    w-= mini_batch_gradient_descent(x,y,w,eta,batch)
    """

    # Batch Gradient Descent

    w -= batch_gradient_descent(x,y,w,eta)




# Show predicted weights
print(w_s)

# Plot the predicted function and the Error
plot_function(x,y,w,Error,w_s)