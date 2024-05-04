# # Importing necessary libraries
# import psutil
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Function to get CPU, Ethernet and memory usage
# def get_performance_data():
#     cpu_percent = psutil.cpu_percent()
#     memory_percent = psutil.virtual_memory().percent
#     # Get Ethernet usage
#     net_io_counters = psutil.net_io_counters()
#     ethernet_percent = (net_io_counters.bytes_sent + net_io_counters.bytes_recv) / (1024**2) # In MB
#     return cpu_percent, ethernet_percent, memory_percent

# # Animation function to update the graphs
# def update_plot(frame):
#     cpu_percent, ethernet_percent, memory_percent = get_performance_data()
    
#     # Update chart data
#     cpu_data.append(cpu_percent)
#     ethernet_data.append(ethernet_percent)
#     memory_data.append(memory_percent)
    
#     # Limit the data displayed on the graphs to maintain the viewing window
#     if len(cpu_data) > window_size:
#         cpu_data.pop(0)
#         ethernet_data.pop(0)
#         memory_data.pop(0)
    
#     # Clean and replot the graphs
#     ax[0].clear()
#     ax[0].plot(cpu_data, label='CPU %')
#     ax[0].set_title('CPU Usage (%)')
#     ax[0].legend()
    
#     ax[1].clear()
#     ax[1].plot(ethernet_data, label='Ethernet MB/s', color='green')
#     ax[1].set_title('Ethernet Usage (MB/s)')
#     ax[1].legend()
    
#     ax[2].clear()
#     ax[2].plot(memory_data, label='Memory %', color='orange')
#     ax[2].set_title('Memory usage (%)')
#     ax[2].legend()

# # Initial configuration of the window and graphics
# fig, ax = plt.subplots(3, 1, figsize=(10, 9))
# cpu_data, ethernet_data, memory_data = [], [], []
# # Number of points to display in the window
# window_size = 50

# # Set animation
# ani = FuncAnimation(fig, update_plot, interval=1000)

# plt.tight_layout()
# plt.show()




# import psutil
# import plotly.graph_objs as go
# from plotly.subplots import make_subplots
# import time

# # Function to get CPU, Ethernet and memory usage
# def get_performance_data():
#     cpu_percent = psutil.cpu_percent()
#     memory_percent = psutil.virtual_memory().percent
#     # Get Ethernet usage
#     net_io_counters = psutil.net_io_counters()
#     ethernet_percent = (net_io_counters.bytes_sent + net_io_counters.bytes_recv) / (1024**2) # In MB
#     return cpu_percent, ethernet_percent, memory_percent

# # Initial configuration of the window and graphics
# fig = make_subplots(rows=3, cols=1, subplot_titles=("CPU Usage (%)", "Ethernet Usage (MB/s)", "Memory usage (%)"))
# fig.update_layout(title_text="System Performance Monitor")
# fig.update_yaxes(title_text="Usage (%)", row=1, col=1)
# fig.update_yaxes(title_text="MB/s", row=2, col=1)
# fig.update_yaxes(title_text="Usage (%)", row=3, col=1)

# # Number of points to display in the window
# window_size = 50
# cpu_data = []
# ethernet_data = []
# memory_data = []
# x_data = []

# # Initialize the traces
# cpu_trace = go.Scatter(x=x_data, y=cpu_data, name='CPU %')
# ethernet_trace = go.Scatter(x=x_data, y=ethernet_data, name='Ethernet MB/s', line=dict(color='green'))
# memory_trace = go.Scatter(x=x_data, y=memory_data, name='Memory %', line=dict(color='orange'))

# # Add traces to figure
# fig.add_trace(cpu_trace, row=1, col=1)
# fig.add_trace(ethernet_trace, row=2, col=1)
# fig.add_trace(memory_trace, row=3, col=1)

# # Continuously update the plots
# while True:
#     try:
#         cpu_percent, ethernet_percent, memory_percent = get_performance_data()
        
#         # Update data
#         cpu_data.append(cpu_percent)
#         ethernet_data.append(ethernet_percent)
#         memory_data.append(memory_percent)
#         x_data.append(time.time())  # Use time as x-axis
        
#         # Limit the data displayed on the graphs to maintain the viewing window
#         if len(cpu_data) > window_size:
#             cpu_data.pop(0)
#             ethernet_data.pop(0)
#             memory_data.pop(0)
#             x_data.pop(0)
        
#         # Update traces
#         cpu_trace = go.Scatter(x=x_data, y=cpu_data, name='CPU %')
#         ethernet_trace = go.Scatter(x=x_data, y=ethernet_data, name='Ethernet MB/s', line=dict(color='green'))
#         memory_trace = go.Scatter(x=x_data, y=memory_data, name='Memory %', line=dict(color='orange'))
        
#         # Update traces in the figure
#         fig.update_traces(cpu_trace, row=1, col=1)
#         fig.update_traces(ethernet_trace, row=2, col=1)
#         fig.update_traces(memory_trace, row=3, col=1)
        
#         # Show the updated figure
#         fig.show()
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
    
#     time.sleep(3)







# Importing necessary libraries
import psutil
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
from datetime import datetime

# Function to get CPU, Ethernet and memory usage
def get_performance_data():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    # Get Ethernet usage
    net_io_counters = psutil.net_io_counters()
    ethernet_percent = (net_io_counters.bytes_sent + net_io_counters.bytes_recv) / (1024**2) # In MB
    return cpu_percent, ethernet_percent, memory_percent

# Initial configuration of the window and graphics
fig = make_subplots(rows=3, cols=1, subplot_titles=("CPU Usage (%)", "Ethernet Usage (MB/s)", "Memory usage (%)"))
fig.update_layout(title_text="System Performance Monitor")
fig.update_yaxes(title_text="Usage (%)", row=1, col=1)
fig.update_yaxes(title_text="MB/s", row=2, col=1)
fig.update_yaxes(title_text="Usage (%)", row=3, col=1)

# Number of points to display in the window
window_size = 50
cpu_data = []
ethernet_data = []
memory_data = []
x_data = []

# Initialize the traces
cpu_trace = go.Scatter(x=x_data, y=cpu_data, name='CPU %')
ethernet_trace = go.Scatter(x=x_data, y=ethernet_data, name='Ethernet MB/s', line=dict(color='green'))
memory_trace = go.Scatter(x=x_data, y=memory_data, name='Memory %', line=dict(color='orange'))

# Add traces to figure
fig.add_trace(cpu_trace, row=1, col=1)
fig.add_trace(ethernet_trace, row=2, col=1)
fig.add_trace(memory_trace, row=3, col=1)

# Continuously update the plots
while True:
    try:
        cpu_percent, ethernet_percent, memory_percent = get_performance_data()
        
        # Update data
        cpu_data.append(cpu_percent)
        ethernet_data.append(ethernet_percent)
        memory_data.append(memory_percent)
        x_data.append(datetime.now().strftime('%H:%M:%S'))  # Use current time in military format
        
        # Limit the data displayed on the graphs to maintain the viewing window
        if len(cpu_data) > window_size:
            cpu_data.pop(0)
            ethernet_data.pop(0)
            memory_data.pop(0)
            x_data.pop(0)
        
        # Update traces
        cpu_trace = go.Scatter(x=x_data, y=cpu_data, name='CPU %')
        ethernet_trace = go.Scatter(x=x_data, y=ethernet_data, name='Ethernet MB/s', line=dict(color='green'))
        memory_trace = go.Scatter(x=x_data, y=memory_data, name='Memory %', line=dict(color='orange'))
        
        # Update traces in the figure
        fig.update_traces(cpu_trace, row=1, col=1)
        fig.update_traces(ethernet_trace, row=2, col=1)
        fig.update_traces(memory_trace, row=3, col=1)
        
        # Show the updated figure
        fig.show()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    time.sleep(3)
