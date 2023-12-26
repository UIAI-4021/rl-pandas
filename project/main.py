import gym
import numpy as np
import gym_maze
from tqdm import tqdm

class Maze:

    @staticmethod
    def choose_action(state):
        action = 0
        epsilon = 0.1

        epsilon_choice = np.random.choice((1,0) , p=[epsilon, 1-epsilon])

        # epsilon_choice = np.random.uniform(0, 1)

        if epsilon_choice:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])
        return action

    @staticmethod
    def update(state, state2, reward, action, action2):
        predict = Q[state, action]
        target = reward + 0.9 * Q[state2, action2]
        Q[state, action] = Q[state, action] + 0.1 * (target - predict)


# Create an environment
env = gym.make("maze-random-10x10-plus-v0")
observation = env.reset()

NUM_EPISODES = 1000

total_win_during_learning = 0

Q = np.zeros((100, 4))
#for episode in tqdm(range(NUM_EPISODES) , desc= 'Learning'):
for episode in range(NUM_EPISODES):
    #print(f'Episode: {episode}')

    training = 0
    state1 = 0
    action1 = Maze.choose_action(state1)

    while training < 200:   #or not done
        env.render()

        # Getting the next state
        state2, reward, done, truncated = env.step(action1)
        state2 = state2[0] * 10 + state2[1] #converting state from 2d into 1d out of 100

        # Choosing the next action
        action2 = Maze.choose_action(state2)

        # Learning the Q-value
        Maze.update(state1, state2, reward, action1, action2)

        state1 = state2
        action1 = action2

        # Updating the respective vaLues
        training += 1

        # If at the end of learning process
        if state1 == 99:
            reward = 1
        else:
            reward = (-0.5)/state1

        if done or truncated:
            observation = env.reset()
            total_win_during_learning +=1
            # print("WON  ********************************!")
            break

#==========================================================
# TESTING THE AGENT AFTER LEARNING USING SARSA ALGORITHN.
#==========================================================

next_state = 0
total_win_after_learning = 0
observation = env.reset()
for i in range(10000):
    env.render()
    action = np.argmax(Q[next_state, :])
    # print(f'action is: {action}')

    next_state, reward, done, truncated = env.step(action)
    next_state = next_state[0] * 10 + next_state[1]

    if done or truncated:
        total_win_after_learning +=1
        observation = env.reset()

print(f'total win in 10000 itterarion after learning: {total_win_after_learning}')

print(f'total win during learning is : {total_win_during_learning}')
env.close()