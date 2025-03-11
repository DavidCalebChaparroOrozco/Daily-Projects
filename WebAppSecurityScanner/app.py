# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import tkinter as tk
from tkinter import scrolledtext, messagebox

class WebSecurityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.vulnerabilities = []

    # Scan the target URL for potential XSS vulnerabilities.
    def scan_for_xss(self):
        self.log("Scanning for XSS vulnerabilities...")
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                form_action = form.get('action')
                form_method = form.get('method', 'get').lower()
                payload = "<script>alert('XSS')</script>"
                data = {}
                for input_tag in form.find_all('input'):
                    input_name = input_tag.get('name')
                    input_type = input_tag.get('type', 'text')
                    if input_type == 'text':
                        data[input_name] = payload

                target_url = urljoin(self.target_url, form_action) if form_action else self.target_url
                if form_method == 'post':
                    response = self.session.post(target_url, data=data)
                else:
                    response = self.session.get(target_url, params=data)

                if payload in response.text:
                    self.vulnerabilities.append(f"XSS Vulnerability Found in {target_url}")
                    self.log(f"XSS Vulnerability Found in {target_url}")
        except Exception as e:
            self.log(f"Error during XSS scan: {e}")

    # Scan the target URL for potential CSRF vulnerabilities.
    def scan_for_csrf(self):
        self.log("Scanning for CSRF vulnerabilities...")
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                if not form.find('input', {'name': 'csrf_token'}):
                    self.vulnerabilities.append(f"CSRF Vulnerability Found in {self.target_url}")
                    self.log(f"CSRF Vulnerability Found in {self.target_url}")
                    break
        except Exception as e:
            self.log(f"Error during CSRF scan: {e}")

    # Scan the target URL for potential SQL Injection vulnerabilities.
    def scan_for_sqli(self):
        self.log("Scanning for SQL Injection vulnerabilities...")
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                form_action = form.get('action')
                form_method = form.get('method', 'get').lower()
                payload = "' OR '1'='1"
                data = {}
                for input_tag in form.find_all('input'):
                    input_name = input_tag.get('name')
                    input_type = input_tag.get('type', 'text')
                    if input_type == 'text':
                        data[input_name] = payload

                target_url = urljoin(self.target_url, form_action) if form_action else self.target_url
                if form_method == 'post':
                    response = self.session.post(target_url, data=data)
                else:
                    response = self.session.get(target_url, params=data)

                if "error" in response.text.lower() or "sql" in response.text.lower():
                    self.vulnerabilities.append(f"SQL Injection Vulnerability Found in {target_url}")
                    self.log(f"SQL Injection Vulnerability Found in {target_url}")
        except Exception as e:
            self.log(f"Error during SQL Injection scan: {e}")

    # Scan the target URL for exposed files and directories.
    def scan_for_exposed_files(self):
        self.log("Scanning for exposed files and directories...")
        common_files = ["robots.txt", "sitemap.xml", ".env", "config.php"]
        for file in common_files:
            try:
                response = self.session.get(urljoin(self.target_url, file))
                if response.status_code == 200:
                    self.vulnerabilities.append(f"Exposed File Found: {file}")
                    self.log(f"Exposed File Found: {file}")
            except Exception as e:
                self.log(f"Error scanning for {file}: {e}")

    # Log messages to the UI.
    def log(self, message):
        self.output_area.insert(tk.END, message + "\n")
        self.output_area.see(tk.END)

    # Generate a report of all vulnerabilities found.
    def generate_report(self):
        if not self.vulnerabilities:
            self.log("No vulnerabilities found.")
        else:
            self.log("Vulnerabilities Found:")
            for vulnerability in self.vulnerabilities:
                self.log(f"- {vulnerability}")
            # Save report to a file
            with open("vulnerability_report.txt", "w") as file:
                file.write("\n".join(self.vulnerabilities))
            self.log("Report saved to 'vulnerability_report.txt'.")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Application Security Scanner by David Caleb")
        self.geometry("800x600")
        self.configure(bg="#2d2d2d")

        # UI Elements
        self.label = tk.Label(self, text="Web Application Security Scanner", font=("Arial", 16), bg="#2d2d2d", fg="white")
        self.label.pack(pady=10)

        self.url_label = tk.Label(self, text="Enter Target URL:", bg="#2d2d2d", fg="white")
        self.url_label.pack()

        self.url_entry = tk.Entry(self, width=50, bg="#3d3d3d", fg="white")
        self.url_entry.pack(pady=10)

        self.scan_button = tk.Button(self, text="Scan", command=self.start_scan, bg="#4CAF50", fg="white")
        self.scan_button.pack(pady=10)

        self.output_area = scrolledtext.ScrolledText(self, width=90, height=25, bg="#3d3d3d", fg="white")
        self.output_area.pack(pady=10)

    # Start the scanning process.
    def start_scan(self):
        target_url = self.url_entry.get()
        if not target_url:
            messagebox.showerror("Error", "Please enter a target URL.")
            return

        scanner = WebSecurityScanner(target_url)
        scanner.output_area = self.output_area  # Pass the output area to the scanner

        # Clear previous results
        self.output_area.delete(1.0, tk.END)
        scanner.vulnerabilities.clear()

        # Run scans
        scanner.scan_for_xss()
        scanner.scan_for_csrf()
        scanner.scan_for_sqli()
        scanner.scan_for_exposed_files()

        # Generate report
        scanner.generate_report()

if __name__ == "__main__":
    app = Application()
    app.mainloop()

# https://www.linkedin.com/
# https://www.facebook.com/
# https://www.twitter.com/
# https://www.google.com/
# https://www.github.com/
# https://www.instagram.com/
# https://www.youtube.com/
# https://www.medium.com/