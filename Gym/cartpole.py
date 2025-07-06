# Import necessary libraries
import gymnasium as gym 
import numpy as np      
import math             
import random           
import os               

# Initialize the CartPole environment with human rendering
env = gym.make("CartPole-v1", render_mode="human")

# Define the discretization buckets for each state variable and possible actions
# Format: (cart_position_buckets, cart_velocity_buckets, pole_angle_buckets, pole_velocity_buckets)

# Using fewer buckets for position/velocity to simplify
NUM_BUCKETS = (1, 1, 6, 12)  
# Number of possible actions (left/right)
NUM_ACTIONS = env.action_space.n  

# Define bounds for each state variable to limit the observation space
STATE_BOUNDS = list(zip(env.observation_space.low, env.observation_space.high))

# Adjust specific bounds for more effective learning:
# Constrain cart velocity
STATE_BOUNDS[1] = [-0.5, 0.5]  
# Constrain pole angular velocity
STATE_BOUNDS[3] = [-math.radians(50), math.radians(50)]  

# Path for saving/loading the Q-table
Q_TABLE_FILE = "q_table_cartpole.npy"

# Attempt to load pre-trained Q-table if available
if os.path.exists(Q_TABLE_FILE):
    q_table = np.load(Q_TABLE_FILE)
    print("✅ Loaded pre-trained Q-table.")
    # Run in demonstration mode
    TRAIN_MODE = False  
else:
    # Initialize Q-table with zeros if no pre-trained file exists
    q_table = np.zeros(NUM_BUCKETS + (NUM_ACTIONS,))
    TRAIN_MODE = True  # Run in training mode
    print("🛠️ Training new Q-table...")

# Reinforcement learning hyperparameters

# Minimum exploration probability
MIN_EXPLORE_RATE = 0.01    
# Minimum learning rate
MIN_LEARNING_RATE = 0.1    
# Controls decay rates
DECAY_FACTOR = np.prod(NUM_BUCKETS, dtype=float) / 10.0  
# Discount factor for future rewards
GAMMA = 0.99               
# Number of training episodes
EPISODES = 1000            
# Maximum timesteps per episode
MAX_T = 200                

# Convert continuous state variables into discrete buckets.
def discretize_state(state):
    """    
    Args:
        state: The continuous state observation from the environment
        
    Returns:
        tuple: Discrete state indices for each state variable
    """
    ratios = []
    for i in range(len(state)):
        min_val, max_val = STATE_BOUNDS[i]
        # Normalize each state variable to [0, 1] range
        ratios.append((state[i] - min_val) / (max_val - min_val))
    
    discretized_state = []
    for i in range(len(ratios)):
        # Map normalized values to bucket indices
        discretized_state.append(int(round((NUM_BUCKETS[i] - 1) * ratios[i])))
        # Ensure index stays within valid bucket range
        discretized_state[i] = min(NUM_BUCKETS[i] - 1, max(0, discretized_state[i]))
    
    return tuple(discretized_state)

# Select an action using ε-greedy policy.
def select_action(state, explore_rate):
    """    
    Args:
        state: Current discrete state
        explore_rate: Current probability of taking a random action
        
    Returns:
        int: Selected action (0 or 1 for CartPole)
    """
    if random.random() < explore_rate:
        # Exploration: random action
        return env.action_space.sample()
    else:
        # Exploitation: best known action from Q-table
        return int(np.argmax(q_table[state]))

# Calculate decaying exploration rate.
def get_explore_rate(t):
    """    
    Args:
        t: Current episode number or timestep
        
    Returns:
        float: Exploration rate between MIN_EXPLORE_RATE and 1.0
    """
    return max(MIN_EXPLORE_RATE, min(1.0, 1.0 - math.log10((t + 1) / DECAY_FACTOR)))

# Calculate decaying learning rate.
def get_learning_rate(t):
    """    
    Args:
        t: Current episode number or timestep
        
    Returns:
        float: Learning rate between MIN_LEARNING_RATE and 0.5
    """
    return max(MIN_LEARNING_RATE, min(0.5, 1.0 - math.log10((t + 1) / DECAY_FACTOR)))

# Training procedure
if TRAIN_MODE:
    print("🚀 Starting training process...")
    for episode in range(EPISODES):
        # Reset environment for new episode
        current_state, _ = env.reset()
        discretized_state = discretize_state(current_state)

        # Get current exploration and learning rates
        lr = get_learning_rate(episode)
        explore_rate = get_explore_rate(episode)
        # Track cumulative reward for this episode
        total_reward = 0  

        for t in range(MAX_T):
            # Select and execute action
            action = select_action(discretized_state, explore_rate)
            obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            new_discretized_state = discretize_state(obs)

            # Q-learning update using Bellman equation
            # Best Q-value for next state
            best_q = np.max(q_table[new_discretized_state])  
            current_q = q_table[discretized_state + (action,)]
            # Update Q-value for current state-action pair
            q_table[discretized_state + (action,)] += lr * (reward + GAMMA * best_q - current_q)

            # Transition to new state
            discretized_state = new_discretized_state
            total_reward += reward

            if done:
                # End episode if terminated
                break  

        # Print progress every 50 episodes
        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}/{EPISODES} — Score: {total_reward}")

    # Save the trained Q-table for future use
    np.save(Q_TABLE_FILE, q_table)
    print(f"💾 Q-table saved to {Q_TABLE_FILE}")

# Demonstration of the learned policy
print("\n🎮 Running agent with learned policy...")
for episode in range(5):
    current_state, _ = env.reset()
    state = discretize_state(current_state)
    total_reward = 0

    for t in range(MAX_T):
        # Always choose the best known action (no exploration)
        action = int(np.argmax(q_table[state]))  
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        state = discretize_state(obs)
        total_reward += reward
        
        if done:
            # End episode if terminated
            break  

    print(f"🎯 Demo Episode {episode + 1} — Score: {total_reward}")

# Close the environment
env.close()