import gym
import gym_anytrading
from gym_anytrading.envs import TradingEnv, StocksEnv, ForexEnv
from gym_anytrading.datasets import STOCKS_GOOGL
import matplotlib.pyplot as plt

env = gym.make('stocks-v0')

observation = env.reset()
while True:
    action = env.action_space.sample()
    # action = 1
    # obs, reward, done, info = env.step(action)
    obs, reward, done, info = env.step(action)
    print("action: {} \n obs [price diff]: {}".format(action, obs))
    # env.render()
    if done:
        print("info:", info)
        break

plt.cla()
env.render()
plt.show()
