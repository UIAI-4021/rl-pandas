import gym
import numpy as np
import gym_maze



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
env = gym.make("maze-random-10x10-v0")
observation = env.reset()


NUM_EPISODES = 1000


Q = np.zeros((100, 4))
for episode in range(NUM_EPISODES):
    print(episode)
    training = 0
    state1 = 0
    action1 = Maze.choose_action(state1)

    while training < 100:
        # Visualizing the training
        env.render()

        # Getting the next state
        state2, reward, done, info = env.step(action1)
        state2 = state2[0] * 10 + state2[1]

        # Choosing the next action
        action2 = Maze.choose_action(state2)


        # Learning the Q-value
        Maze.update(state1, state2, reward, action1, action2)

        state1 = state2
        action1 = action2

        # Updating the respective vaLues
        training += 1

        next_state, reward, done, truncated = env.step(action1)

        # If at the end of learning process
        if state1 == 99:
            reward = 1
        else:
            reward = (-0.5)/state1

        if done or truncated:
            observation = env.reset()
            training = 100
            print("WON  ********************************!")

env.close()
