import gym
import numpy as np


class Maze:

    @staticmethod
    def choose_action(state):
        action = 0
        epsilon = 0.8

        epsilon_choice = np.random.uniform(0, 1)

        if epsilon_choice < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])
        return action

    @staticmethod
    def update(state, state2, reward, action, action2):
        predict = Q[state, action]
        target = reward + 0.8 * Q[state2, action2]
        Q[state, action] = Q[state, action] + 0.9 * (target - predict)


import gym_maze
# Create an environment
env = gym.make("maze-random-10x10-plus-v0")
observation = env.reset()

# Define the maximum number of iterations
NUM_EPISODES = 1000

for episode in range(NUM_EPISODES):

    # TODO: Implement the agent policy here
    # Note: .sample() is used to sample random action from the environment's action space

    # Choose an action (Replace this random action with your agent's policy)
    action = env.action_space.sample()

    # Perform the action and receive feedback from the environment
    next_state, reward, done, truncated = env.step(action)

    if done or truncated:
        observation = env.reset()

# Close the environment
env.close()