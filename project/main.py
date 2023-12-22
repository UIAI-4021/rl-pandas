import gym
import numpy as np
import gym_maze

alpha = 0.1  # learning rate
gamma = 0.99  # discount factor
epsilon = 0.1  # exploration-exploitation trade-off
total_episodes = 1000  # number of episodes

def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(action_space_size)
    else:
        return np.argmax(q_table[state, :])
    
def update(state, action, reward, next_state, next_action):
    q_table[state, action] = q_table[state, action] + alpha * \
                            (reward + gamma * q_table[next_state, next_action] - q_table[state, action])



# Create an environment
env = gym.make("maze-random-10x10-v0")
observation = env.reset()


NUM_EPISODES = 1000

<<<<<<< HEAD
for episode in range(NUM_EPISODES):
<<<<<<< HEAD

    # TODO: Implement the agent policy here
=======
=======
Q = np.zeros((100, 4))
sum = 0

for episode in range(NUM_EPISODES):
    print(f'episode : {episode}')
>>>>>>> 2cf75f1 (tmp)
    training = 0
    state1 = 0
    action1 = Maze.choose_action(state1)
    env.render()

    for t in range(200):  # maximum time steps per episode
        env.render()

        # Choose the current action using epsilon-greedy policy
        action = choose_action(state)

        # Take the chosen action and observe the next state and reward
        next_state, reward, done, _ = env.step(action)

        # Choose the next action using epsilon-greedy policy
        next_action = choose_action(next_state)

        # Update Q-value
        update(state, action, reward, next_state, next_action)

        state = next_state

        if done:
            break
<<<<<<< HEAD
>>>>>>> 5872190 (adding mai parts)
    # Note: .sample() is used to sample random action from the environment's action space

    # Choose an action (Replace this random action with your agent's policy)
    action = env.action_space.sample()

    # Perform the action and receive feedback from the environment
    next_state, reward, done, truncated = env.step(action)

    if done or truncated:
        observation = env.reset()

# Close the environment
=======


# Close the environment
print(sum)
>>>>>>> 2cf75f1 (tmp)
env.close()