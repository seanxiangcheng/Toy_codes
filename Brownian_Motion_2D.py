"""
  Code of Brownian Motion Animination 
  This code is a 'toy' code to study 'class' and 'animation';
  Just for study and exerciese purpose;
  It may be non-optimal;
  
  This code is ready to run;
  you can also tune the parameters in the main function;
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.animation as animation

class BM2d(object):
  
  # Initialization of 2D Brownian Motion
  def __init__(self, dt=0.01, D=1.0, T=10.0, N=2, L1=10.0, L2=10.0):
    self.t = 0.0                        # t: starting time 0.0
    self.dt = dt                        # dt: time step
    self.T = T                          # T: total simulated time
    self.N = N                          # N: number of particles
    self.D = D                          # D: diffusion constant
    self.L1 = L1                        # L1: Length of Dimension 1
    self.L2 = L2                        # L2: Length of Dimension 2
    self.X = np.random.rand(N,2)        # X: Positions of all particles
    self.X[:,0] = self.X[:,0]*L1        # Convert positions to range ... 
    self.X[:,1] = self.X[:,1]*L2        # ... L1 and L2
  
  # One Step Move of 2D Brownian Motion
  # Return null
  def move(self):
    self.X = self.X + norm.rvs(loc = 0, size = self.X.shape, scale = self.D**2*self.dt)
    for i in range(self.N):
      if self.X[i, 0] > self.L1:
        self.X[i, 0] -= self.L1
      if self.X[i, 0] < 0.0:
        self.X[i, 0] = -self.X[i, 0]
      if self.X[i, 1] > self.L2:
        self.X[i, 1] -= self.L2
      if self.X[i, 1] < 0.0:
        self.X[i, 1] = -self.X[i, 1]
    self.t = self.t + self.dt
    

  # Trajactory of the 2D Brownian Motion
  # Returns the trajactory of each time step in a matrix of N-by-D-by-Steps
  def traj(self):
    nsteps = int(self.T/self.dt)
    trajX = np.zeros((self.N, self.D, nsteps))
    for i in range(nsteps):
      trajX[:,:,i] = self.X
      self.move()
    return trajX
    
  def plot_traj(self, mstyle = 'o', msize = 6, lstyle = '-', lwidth = 1.0):
    traj = self.traj()
    for i in range(traj.shape[0]):
      plt.plot(traj[i,0,0], traj[i,1,0], mstyle+'b', markersize = msize)
      plt.plot(traj[i,0,:], traj[i,1,:], lstyle, linewidth = lwidth)
      plt.plot(traj[i,0,-1], traj[i,1,-1], mstyle+'r', markersize = msize)
    plt.xlabel('X')
    plt.ylabel('Y')



### global variables for animation ###
### I am a beginner (12/20/2014). If there is a better way, 
### please let me know by chengxiang.cn@gmail.com ###
test = BM2d()
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, xlim=(0, 10), ylim=(0, 10))
positions, = ax.plot([], [])

def main():
  global test, fig, ax, positions
  dt = 0.1
  T = 10
  N = 10
  L1 = 10 
  L2 = 10 
  D = 1
  msize = 4
  Nsteps = T/dt
  test = BM2d(dt = dt, T = T, N = N, L1 = L1, L2 = L2, D = D)
  
  ### Annimiation ###
  positions, = ax.plot([], [], 'bo', ms = msize)
  plt.grid('on')
  anim = animation.FuncAnimation(fig, animate, frames = 50, init_func=init, interval=100, blit=True)
  #anim.save('bm.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
  #anim.save('bm.gif', writer='imagemagick', fps=10);
  plt.show()


def animate(i):
  global test, positions
  test.move()
  positions.set_data(test.X[:,0], test.X[:,1])  # update the data
  return positions,

#Init only required for blitting to give a clean slate.
def init():
  global test, positions
  positions.set_data([], [])
  return positions, 
    
if __name__ == "__main__":
  main()
