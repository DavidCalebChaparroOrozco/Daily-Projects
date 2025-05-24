# Importing necessary modules
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import rcParams

class NeuralNetworkApp:
    # Initialize the main application window with modern dark theme
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Neural Network Visualizer by David Caleb")
        self.root.geometry("1100x750")
        self.root.configure(bg='#1e1e1e')
        
        # Custom style configuration
        self._setup_styles()
        
        self.layer_entries = []
        self.canvas = None

        self._setup_menu()
        self._setup_main_ui()

    # Configure custom styles for widgets
    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main colors
        bg_color = '#2a2a2a'
        fg_color = '#e0e0e0'
        accent_color = '#4ec9b0'
        entry_bg = '#3a3a3a'
        
        # General style configuration
        style.configure('.', background=bg_color, foreground=fg_color)
        style.map('.', background=[('active', '#3a3a3a')])
        
        # Specific widget styles
        style.configure('TFrame', background=bg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Segoe UI', 10))
        style.configure('TButton', background='#3a3a3a', foreground=fg_color, 
                        borderwidth=1, relief='solid', font=('Segoe UI', 9))
        style.map('TButton', background=[('active', '#4a4a4a')])
        style.configure('TEntry', fieldbackground=entry_bg, foreground=fg_color, 
                        insertcolor=fg_color, borderwidth=1, relief='solid')
        style.configure('TNotebook', background=bg_color, borderwidth=0)
        style.configure('TNotebook.Tab', background='#3a3a3a', foreground=fg_color,
                        padding=[10, 5], font=('Segoe UI', 9))
        style.map('TNotebook.Tab', background=[('selected', bg_color), ('active', '#4a4a4a')])
        
        # Configure matplotlib dark theme
        rcParams['figure.facecolor'] = bg_color
        rcParams['axes.facecolor'] = bg_color
        rcParams['axes.edgecolor'] = accent_color
        rcParams['axes.labelcolor'] = fg_color
        rcParams['text.color'] = fg_color
        rcParams['xtick.color'] = fg_color
        rcParams['ytick.color'] = fg_color

    # Create a modern menu bar
    def _setup_menu(self):
        menubar = tk.Menu(self.root, bg='#2a2a2a', fg='#e0e0e0', activebackground='#3a3a3a')
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0, bg='#2a2a2a', fg='#e0e0e0')
        file_menu.add_command(label="New", command=self._reset_app)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0, bg='#2a2a2a', fg='#e0e0e0')
        help_menu.add_command(label="Quick Start", command=self._show_quick_start)
        help_menu.add_command(label="About", command=self._show_about)
        
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)

    # Setup the main user interface with tabs
    def _setup_main_ui(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Configuration tab
        config_tab = ttk.Frame(self.notebook)
        self.notebook.add(config_tab, text="Configuration")
        self._setup_config_tab(config_tab)
        
        # Visualization tab
        self.viz_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.viz_tab, text="Visualization")
        self._setup_viz_tab(self.viz_tab)

    # Setup the configuration tab with input controls
    def _setup_config_tab(self, parent):
        # Left panel - Network structure
        left_frame = ttk.LabelFrame(parent, text="Network Structure", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Number of layers control
        layers_frame = ttk.Frame(left_frame)
        layers_frame.pack(fill=tk.X, pady=5)
        ttk.Label(layers_frame, text="Number of Layers:").pack(side=tk.LEFT)
        self.num_layers_var = tk.IntVar(value=3)
        layer_entry = ttk.Entry(layers_frame, textvariable=self.num_layers_var, width=5)
        layer_entry.pack(side=tk.RIGHT, padx=5)
        
        # Set layers button
        set_btn = ttk.Button(left_frame, text="Configure Layers", command=self._create_layer_inputs)
        set_btn.pack(pady=10)
        
        # Layer configuration
        self.layer_config_frame = ttk.LabelFrame(left_frame, text="Layer Configuration", padding=10)
        self.layer_config_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Right panel - Visualization controls
        right_frame = ttk.LabelFrame(parent, text="Visualization Controls", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # Visualize button
        viz_btn = ttk.Button(right_frame, text="Generate Visualization", 
                            command=self._visualize, style='Accent.TButton')
        viz_btn.pack(pady=20)
        
        # Help section
        help_frame = ttk.LabelFrame(right_frame, text="Quick Help", padding=10)
        help_frame.pack(fill=tk.X, pady=10)
        help_text = """ 
        1. Set number of layers
        2. Configure neurons per layer
        3. Click 'Generate Visualization'
        4. View results in Visualization tab
        """
        ttk.Label(help_frame, text=help_text, justify=tk.LEFT).pack()
        
        # Initialize layer inputs
        self._create_layer_inputs()

    # Setup the visualization tab
    def _setup_viz_tab(self, parent):
        self.viz_canvas_frame = ttk.Frame(parent)
        self.viz_canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Placeholder for visualization
        ttk.Label(self.viz_canvas_frame, text="Network visualization will appear here", 
                    font=('Segoe UI', 12)).pack(expand=True)

    # Create input fields for each layer's neuron count
    def _create_layer_inputs(self):
        for widget in self.layer_config_frame.winfo_children():
            widget.destroy()
        self.layer_entries.clear()

        try:
            num_layers = self.num_layers_var.get()
            if num_layers < 1:
                raise ValueError("At least 1 layer required")
                
            for i in range(num_layers):
                frame = ttk.Frame(self.layer_config_frame)
                frame.pack(fill=tk.X, pady=3)
                
                ttk.Label(frame, text=f"Layer {i+1} neurons:").pack(side=tk.LEFT, padx=5)
                var = tk.IntVar(value=4 if i != num_layers-1 else 1)  # Default output layer to 1
                entry = ttk.Entry(frame, textvariable=var, width=8)
                entry.pack(side=tk.RIGHT)
                self.layer_entries.append(var)
                
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            self.num_layers_var.set(3)
            self._create_layer_inputs()

    # Generate and display the neural network visualization
    def _visualize(self):
        try:
            layer_structure = [v.get() for v in self.layer_entries]
            if any(n <= 0 for n in layer_structure):
                raise ValueError("All layers must have at least 1 neuron")
                
            # Clear previous visualization
            for widget in self.viz_canvas_frame.winfo_children():
                widget.destroy()
            
            # Generate new visualization
            visualizer = NeuralNetworkVisualizer(layer_structure)
            fig = visualizer.draw_network()
            
            # Embed in canvas
            self.canvas = FigureCanvasTkAgg(fig, master=self.viz_canvas_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Switch to visualization tab
            self.notebook.select(self.viz_tab)
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate visualization: {str(e)}")

    # Reset the application to initial state
    def _reset_app(self):
        self.num_layers_var.set(3)
        self._create_layer_inputs()
        for widget in self.viz_canvas_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.viz_canvas_frame, text="Network visualization will appear here", 
                    font=('Segoe UI', 12)).pack(expand=True)
        self.notebook.select(0)

    # Show quick start guide
    def _show_quick_start(self):
        messagebox.showinfo("Quick Start",
            "How to use this visualizer:\n\n"
            "1. Go to Configuration tab\n"
            "2. Set the number of layers\n"
            "3. Click 'Configure Layers'\n"
            "4. Enter neurons for each layer\n"
            "5. Click 'Generate Visualization'\n"
            "6. View results in Visualization tab\n\n"
            "Tip: Output layer typically has 1 neuron for binary classification.")

    # Show about information
    def _show_about(self):
        messagebox.showinfo("About",
            "Neural Network Structure Visualizer\n"
            "Version 2.0\n\n"
            "A tool for visualizing neural network architectures.\n"
            "Features:\n"
            "- Interactive layer configuration\n"
            "- Clean, dark theme interface\n"
            "- Detailed network visualization")

    # Run the application
    def run(self):
        self.root.mainloop()


class NeuralNetworkVisualizer:
    # Initialize visualizer with layer structure.
    def __init__(self, layer_structure):
        """
        
        Args:
            layer_structure (list): Number of neurons in each layer
        """
        self.layer_structure = layer_structure
        self.neuron_color = '#4ec9b0'  # Teal accent color
        self.connection_color = '#5a5a5a'

    # Create the network visualization.
    def draw_network(self):
        """
        
        Returns:
            matplotlib.figure.Figure: The generated figure
        """
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
        ax.axis('off')
        
        # Add title with architecture
        arch_text = " → ".join(map(str, self.layer_structure))
        ax.set_title(f"Neural Network Architecture: {arch_text}", 
                    pad=20, color='white', fontsize=12)
        
        self._draw_layers(ax)
        plt.tight_layout()
        return fig

    # Draw all layers and connections
    def _draw_layers(self, ax):
        total_layers = len(self.layer_structure)
        max_neurons = max(self.layer_structure)
        
        # Calculate spacing
        h_spacing = 1.0 / max(1, total_layers - 1)
        v_spacing = 1.0 / max(1, max_neurons - 1)

        for i, layer_size in enumerate(self.layer_structure):
            x_pos = i * h_spacing
            y_positions = self._get_neuron_positions(layer_size, v_spacing)
            
            # Draw neurons
            for y in y_positions:
                neuron = plt.Circle((x_pos, y), 0.02, 
                                    color=self.neuron_color, 
                                    zorder=4)
                ax.add_patch(neuron)
            
            # Draw connections to previous layer
            if i > 0:
                prev_size = self.layer_structure[i - 1]
                prev_y_pos = self._get_neuron_positions(prev_size, v_spacing)
                
                for y in y_positions:
                    for py in prev_y_pos:
                        px = (i - 1) * h_spacing
                        ax.plot([px, x_pos], [py, y], 
                                color=self.connection_color,
                                linewidth=0.8, 
                                alpha=0.6,
                                zorder=3)

    # Calculate vertical positions for neurons in a layer.
    def _get_neuron_positions(self, neurons, spacing):
        """    
        Args:
            neurons: Number of neurons
            spacing: Vertical spacing between neurons
            
        Returns:
            list: Y positions for neurons
        """
        if neurons == 1:
            # Center single neuron
            return [0.5]  
        
        total_height = (neurons - 1) * spacing
        start_y = 0.5 - total_height / 2
        return [start_y + i * spacing for i in range(neurons)]


if __name__ == "__main__":
    app = NeuralNetworkApp()
    app.run()