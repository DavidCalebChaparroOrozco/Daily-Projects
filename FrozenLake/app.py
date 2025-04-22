# Import necessary libraries
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from IPython.display import clear_output
import time
from collections import deque

# Custom epsilon decay function 
def epsilon_decay(episode, total_episodes, initial_epsilon=1.0, min_epsilon=0.01):
    decay_rate = 5 / total_episodes
    return min_epsilon + (initial_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

# Hyperparameter optimization 
def optimize_parameters(env, num_episodes=1000):
    # Find optimal hyperparameters through grid search
    param_grid = {
        'learning_rate': [0.1, 0.5, 0.9],
        'discount_factor': [0.8, 0.9, 0.99],
        'epsilon_decay_rate': [0.0001, 0.001, 0.01]
    }
    
    best_params = None
    best_success = 0
    
    print("Starting hyperparameter optimization...")
    for lr in param_grid['learning_rate']:
        for df in param_grid['discount_factor']:
            for edr in param_grid['epsilon_decay_rate']:
                q = np.zeros((env.observation_space.n, env.action_space.n))
                rewards = np.zeros(num_episodes)
                
                for i in range(num_episodes):
                    state = env.reset()[0]
                    terminated = False
                    eps = epsilon_decay(i, num_episodes)
                    
                    while not terminated:
                        if np.random.random() < eps:
                            action = env.action_space.sample()
                        else:
                            action = np.argmax(q[state,:])
                            
                        new_state, reward, terminated, _, _ = env.step(action)
                        
                        # Q-learning update
                        q[state,action] = q[state,action] + lr * (
                            reward + df * np.max(q[new_state,:]) - q[state,action])
                            
                        state = new_state
                    
                    if reward == 1:
                        rewards[i] = 1
                
                success_rate = np.mean(rewards[-100:])
                if success_rate > best_success:
                    best_success = success_rate
                    best_params = {'learning_rate': lr, 'discount_factor': df, 'epsilon_decay_rate': edr}
                    print(f"New best params: {best_params} Success: {best_success:.1%}")
    
    print("\nOptimization complete!")
    print(f"Best parameters: {best_params}")
    print(f"Best success rate: {best_success:.1%}")
    return best_params

# Model evaluation 
def evaluate_model(q_table, map_size="4x4", num_episodes=100, render=False, delay=0.1):
    env = gym.make('FrozenLake-v1', map_name=map_size, is_slippery=True, 
                render_mode='human' if render else None)
    successes = 0
    
    for episode in range(num_episodes):
        state = env.reset()[0]
        terminated = False
        truncated = False
        
        while not terminated and not truncated:
            if render:
                clear_output(wait=True)
                env.render()
                time.sleep(delay)
                
            action = np.argmax(q_table[state,:])
            state, reward, terminated, truncated, _ = env.step(action)
            
        if reward == 1:
            successes += 1
            
    success_rate = successes / num_episodes
    print(f"\nEvaluation complete ({num_episodes} episodes)")
    print(f"Success rate: {success_rate:.1%}")
    env.close()
    return success_rate

# Interactive demo 
def interactive_demo(q_table=None, map_size="4x4"):
    # Let user watch agent play in real-time
    if q_table is None:
        try:
            with open(f'frozen_lake{map_size}.pkl', 'rb') as f:
                q_table = pickle.load(f)
        except:
            print("No trained model found. Please train first.")
            return
    
    env = gym.make('FrozenLake-v1', map_name=map_size, is_slippery=True, render_mode='human')
    
    while True:
        state = env.reset()[0]
        terminated = False
        truncated = False
        
        while not terminated and not truncated:
            clear_output(wait=True)
            env.render()
            # Slow down for visualization
            time.sleep(0.3)  
            
            action = np.argmax(q_table[state,:])
            state, reward, terminated, truncated, _ = env.step(action)
            
        print("\nEpisode finished!")
        print(f"Result: {'Success!' if reward == 1 else 'Failed...'}")
        
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break
            
    env.close()

# Main training function with all enhancements
def train_agent(episodes=5000, map_size="4x4", render=False, optimize=False):
    # Train agent with Q-learning
    
    env = gym.make('FrozenLake-v1', map_name=map_size, is_slippery=True, 
                render_mode='human' if render else None)
    
    # Hyperparameter optimization if requested
    if optimize:
        params = optimize_parameters(env)
        learning_rate = params['learning_rate']
        discount_factor = params['discount_factor']
        epsilon_decay_rate = params['epsilon_decay_rate']
    else:
        # Default parameters
        learning_rate = 0.9
        discount_factor = 0.9
        epsilon_decay_rate = 0.001
    
    q_table = np.zeros((env.observation_space.n, env.action_space.n))
    rewards_per_episode = np.zeros(episodes)
    recent_successes = deque(maxlen=100)
    best_success_rate = 0
    
    print(f"\nStarting training on {map_size} map for {episodes} episodes...")
    print(f"Parameters: LR={learning_rate}, DF={discount_factor}, EDR={epsilon_decay_rate}")
    
    for i in range(episodes):
        state = env.reset()[0]
        terminated = False
        truncated = False
        epsilon = epsilon_decay(i, episodes)
        
        while not terminated and not truncated:
            if np.random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state,:])
                
            new_state, reward, terminated, truncated, _ = env.step(action)
            
            # Q-learning update
            q_table[state,action] = q_table[state,action] + learning_rate * (
                reward + discount_factor * np.max(q_table[new_state,:]) - q_table[state,action])
                
            state = new_state
        
        # Record success (Modification 9)
        if reward == 1:
            rewards_per_episode[i] = 1
            recent_successes.append(1)
        else:
            recent_successes.append(0)
            
        # Early stopping (Modification 9)
        current_success = np.mean(recent_successes)
        if len(recent_successes) == 100 and current_success > 0.8:
            print(f"\nEarly stopping at episode {i} (100-episode success rate: {current_success:.1%})")
            break
            
        # Save best model (Modification 9)
        if current_success > best_success_rate:
            best_success_rate = current_success
            with open(f'frozen_lake{map_size}_best.pkl', 'wb') as f:
                pickle.dump(q_table, f)
        
        # Progress logging (Modification 9)
        if i % 100 == 0 or i == episodes - 1:
            print(f"Episode {i}: ε={epsilon:.3f} | Success rate (last 100): {current_success:.1%}")

    env.close()
    
    # Save final model
    with open(f'frozen_lake{map_size}.pkl', 'wb') as f:
        pickle.dump(q_table, f)
    
    # Enhanced visualization (Modification 1)
    plt.figure(figsize=(12, 6))
    sns.set_style('whitegrid')
    
    # Calculate moving average
    moving_avg = np.convolve(rewards_per_episode, np.ones(100)/100, mode='valid')
    
    ax = sns.lineplot(x=range(len(moving_avg)), y=moving_avg, linewidth=2.5)
    plt.title(f'FrozenLake Training Progress\n{map_size} Map | {i+1} Episodes | Final Success Rate: {current_success:.1%}', fontsize=14)
    plt.xlabel('Episode', fontsize=12)
    plt.ylabel('Success Rate (100-episode moving avg)', fontsize=12)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tight_layout()
    plt.savefig(f'frozen_lake{map_size}_training.png', dpi=300)
    plt.close()
    
    print("\nTraining complete!")
    print(f"Best 100-episode success rate: {best_success_rate:.1%}")
    return q_table

# Main menu (Modification 6)
def main_menu():
    q_table = None
    map_size = "4x4"
    
    while True:
        clear_output(wait=True)
        print("╔════════════════════════════════╗")
        print("║    FROZEN LAKE Q-LEARNING      ║")
        print("╠════════════════════════════════╣")
        print("║ 1. Train new model             ║")
        print("║ 2. Evaluate trained model      ║")
        print("║ 3. Interactive demo            ║")
        print("║ 4. Hyperparameter Optimization ║")
        print("║ 5. Change map size             ║")
        print("║ 6. Exit                        ║")
        print("╚════════════════════════════════╝")
        print(f"\nCurrent map: {map_size}")
        
        choice = input("\nSelect an option (1-6): ")
        
        if choice == '1':
            episodes = int(input("Number of training episodes (e.g., 5000): "))
            optimize = input("Optimize hyperparameters? (y/n): ").lower() == 'y'
            render = input("Render during training? (y/n): ").lower() == 'y'
            q_table = train_agent(episodes, map_size, render, optimize)
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            if q_table is None:
                try:
                    with open(f'frozen_lake{map_size}.pkl', 'rb') as f:
                        q_table = pickle.load(f)
                except:
                    print("No trained model found. Please train first.")
                    input("\nPress Enter to continue...")
                    continue
            
            episodes = int(input("Number of evaluation episodes (e.g., 100): "))
            render = input("Render during evaluation? (y/n): ").lower() == 'y'
            evaluate_model(q_table, map_size, episodes, render)
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            interactive_demo(q_table, map_size)
            
        elif choice == '4':
            env = gym.make('FrozenLake-v1', map_name=map_size, is_slippery=True)
            optimize_parameters(env)
            env.close()
            input("\nPress Enter to continue...")
            
        elif choice == '5':
            new_size = input("Enter map size (4x4 or 8x8): ")
            if new_size in ["4x4", "8x8"]:
                map_size = new_size
                print(f"Map size changed to {map_size}")
            else:
                print("Invalid size. Use 4x4 or 8x8")
            time.sleep(1)
            
        elif choice == '6':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please select 1-6.")
            time.sleep(1)

if __name__ == '__main__':
    main_menu()