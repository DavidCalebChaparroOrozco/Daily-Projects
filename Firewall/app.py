import socket
import json
import logging
from datetime import datetime

# Define a simple Firewall class
class SimpleFirewall:
    def __init__(self, rules_file='rules.json'):
        self.rules = self.load_rules(rules_file)
        self.setup_logging()

    # Load rules from a JSON file.
    def load_rules(self, rules_file):
        try:
            with open(rules_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Save rules to a JSON file.
    def save_rules(self, rules_file='rules.json'):
        with open(rules_file, 'w') as file:
            json.dump(self.rules, file, indent=4)

    # Add a new rule to the firewall.
    def add_rule(self, direction, protocol, port, action):
        self.rules.append({
            'direction': direction,
            'protocol': protocol,
            'port': port,
            'action': action
        })
        self.save_rules()

    # Remove a rule by index.
    def remove_rule(self, index):
        if 0 <= index < len(self.rules):
            self.rules.pop(index)
            self.save_rules()

    # Setup logging to file.
    def setup_logging(self):
        logging.basicConfig(filename='firewall.log', level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    # Filter traffic based on predefined rules.
    def filter_traffic(self, direction, protocol, port, ip=None):
        for rule in self.rules:
            if (rule['direction'] == direction and
                rule['protocol'] == protocol and
                rule['port'] == port):
                action = rule['action']
                log_message = f"Traffic: {direction} {protocol} port {port} from {ip} -> Action: {action}"
                logging.info(log_message)
                return action
        log_message = f"Traffic: {direction} {protocol} port {port} from {ip} -> Action: block"
        logging.info(log_message)
        return "block"

# Simulate network traffic
def simulate_traffic(firewall):
    traffic = [
        {"direction": "incoming", "protocol": "TCP", "port": 80, "ip": "192.168.1.1"},
        {"direction": "incoming", "protocol": "TCP", "port": 22, "ip": "192.168.1.2"},
        {"direction": "outgoing", "protocol": "TCP", "port": 443, "ip": "192.168.1.3"},
        {"direction": "incoming", "protocol": "TCP", "port": 8080, "ip": "192.168.1.4"},
        {"direction": "outgoing", "protocol": "TCP", "port": 8080, "ip": "192.168.1.5"},
    ]

    for packet in traffic:
        action = firewall.filter_traffic(**packet)
        print(f"Traffic: {packet['direction']} {packet['protocol']} port {packet['port']} from {packet['ip']} -> Action: {action}")

# Main function
if __name__ == "__main__":
    firewall = SimpleFirewall()

    # Add a new rule
    firewall.add_rule("incoming", "TCP", 9090, "allow")

    # Simulate network traffic
    simulate_traffic(firewall)