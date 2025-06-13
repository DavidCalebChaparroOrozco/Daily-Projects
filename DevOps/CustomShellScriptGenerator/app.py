# Import necessary libraries
import os
import json
from jinja2 import Environment, FileSystemLoader

# Load configuration from JSON file
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

# Render shell script using Jinja2
def render_script(template_path, config):
    # Set the environment with the template folder
    env = Environment(loader=FileSystemLoader(template_path))
    
    # Load the specific template file
    template = env.get_template('base_script.sh.j2')
    
    # Render the template with the configuration data
    return template.render(config)

# Save the rendered script to an output file
def save_script(output_dir, script_name, content):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    script_path = os.path.join(output_dir, f"{script_name}.sh")

    with open(script_path, 'w') as file:
        file.write(content)

    # Make the script executable
    os.chmod(script_path, 0o755)
    print(f"✅ Script generated: {script_path}")

# Main function
def main():
    config_file = 'config/tasks_config.json'
    template_dir = 'templates'
    output_dir = 'output'

    # Load configuration
    config = load_config(config_file)

    # Generate shell script
    script_content = render_script(template_dir, config)

    # Save the shell script to output
    save_script(output_dir, config['script_name'], script_content)

if __name__ == "__main__":
    main()
