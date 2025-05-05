# Import necessary libraries
import pygetwindow as gw
import win32gui
import win32process
import win32con
import ctypes
import time
from datetime import datetime
import sys
import psutil
from collections import defaultdict, deque

class ComprehensiveWindowsInspector:
    def __init__(self):
        self.current_window = None
        self.current_title = ""
        self.current_pid = 0
        self.running = True
        self.update_interval = 1.0
        
        # Enhanced activity tracking

        # Track last 100 activities
        self.window_activity = deque(maxlen=100)  
        self.window_stats = defaultdict(lambda: {
            'total_time': 0.0,
            'last_activated': None,
            'activation_count': 0,
            'title': ''
        })
        self.start_time = time.time()
        self.last_update_time = time.time()
        
        # Process tracking

        # pid -> process info
        self.process_map = {}  
        
    # Get all visible windows with titles
    def get_all_windows(self):
        windows = []
        def callback(hwnd, _):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                windows.append(hwnd)
        win32gui.EnumWindows(callback, None)
        return windows
    
    # Get detailed information about a window
    def get_window_info(self, hwnd):
        try:
            title = win32gui.GetWindowText(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            
            # Get process info
            process = None
            if pid:
                try:
                    if pid not in self.process_map:
                        process_obj = psutil.Process(pid)
                        self.process_map[pid] = {
                            'name': process_obj.name(),
                            'exe': process_obj.exe(),
                            'status': process_obj.status()
                        }
                    process = self.process_map[pid]
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Get window placement
            try:
                placement = win32gui.GetWindowPlacement(hwnd)
                state = placement[1]
            except:
                state = -1
                
            # Get window rect
            try:
                rect = win32gui.GetWindowRect(hwnd)
                width = rect[2] - rect[0]
                height = rect[3] - rect[1]
            except:
                rect = (0, 0, 0, 0)
                width = height = 0
            
            return {
                'hwnd': hwnd,
                'title': title,
                'pid': pid,
                'process': process,
                'state': state,
                'position': (rect[0], rect[1]),
                'size': (width, height),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            print(f"Error getting window info: {e}")
            return None
    
    # Update window usage statistics
    def update_window_stats(self, window_info):
        if not window_info:
            return
            
        now = time.time()
        time_elapsed = now - self.last_update_time
        self.last_update_time = now
        
        # Update time for previous active window
        if self.current_pid in self.window_stats and self.window_stats[self.current_pid]['last_activated']:
            self.window_stats[self.current_pid]['total_time'] += time_elapsed
        
        # Update new window stats
        pid = window_info['pid']
        self.window_stats[pid]['title'] = window_info['title']
        self.window_stats[pid]['activation_count'] += 1
        self.window_stats[pid]['last_activated'] = now
        
        # Record activity
        self.window_activity.append(window_info)
    
    # Display information about all visible windows
    def display_all_windows(self):
        print("\n" + "="*80)
        print(f"ALL VISIBLE WINDOWS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=".center(50, "="))
        
        windows = self.get_all_windows()
        for i, hwnd in enumerate(windows, 1):
            info = self.get_window_info(hwnd)
            if info:
                active_marker = " (ACTIVE)" if hwnd == win32gui.GetForegroundWindow() else ""
                print(f"\n[{i}] {info['title']}{active_marker}")
                print(f"  PID: {info['pid']}")
                print(f"  Process: {info['process']['name'] if info['process'] else 'Unknown'}")
                print(f"  State: {self.get_state_name(info['state'])}")
                print(f"  Position: {info['position'][0]}, {info['position'][1]}")
                print(f"  Size: {info['size'][0]}x{info['size'][1]}")
        
        print("=".center(50, "="))
    
    # Display recent window activity
    def display_activity_log(self):
        print("\n" + "="*80)
        print(f"RECENT WINDOW ACTIVITY (Last {len(self.window_activity)} changes)")
        print("=".center(50, "="))
        
        for activity in reversed(self.window_activity):
            print(f"\n[{activity['timestamp']}] {activity['title']}")
            print(f"  PID: {activity['pid']}")
            print(f"  Process: {activity['process']['name'] if activity['process'] else 'Unknown'}")
        
        print("=".center(50, "="))
    
    # Display window usage statistics
    def display_usage_stats(self):
        print("\n" + "="*80)
        print("WINDOW USAGE STATISTICS")
        print("=".center(50, "="))
        
        # Calculate total tracked time
        total_tracked = time.time() - self.start_time
        
        # Update time for current window before displaying stats
        now = time.time()
        if self.current_pid in self.window_stats and self.window_stats[self.current_pid]['last_activated']:
            time_elapsed = now - self.last_update_time
            self.window_stats[self.current_pid]['total_time'] += time_elapsed
            self.last_update_time = now
        
        # Sort by total time (descending)
        sorted_stats = sorted(
            self.window_stats.items(),
            key=lambda x: x[1]['total_time'],
            reverse=True
        )
        
        if not sorted_stats:
            print("\nNo window activity statistics available yet.")
        else:
            for pid, stats in sorted_stats:
                if stats['total_time'] > 0:
                    proc_info = self.process_map.get(pid, {'name': 'Unknown'})
                    time_percent = (stats['total_time'] / total_tracked) * 100
                    print(f"\n{stats['title']} (PID: {pid})")
                    print(f"  Process: {proc_info['name']}")
                    print(f"  Activations: {stats['activation_count']}")
                    print(f"  Total time: {stats['total_time']:.1f}s ({time_percent:.1f}%)")
        
        print("=".center(50, "="))
    
    # Convert window state code to name
    def get_state_name(self, state):
        states = {
            win32con.SW_HIDE: "Hidden",
            win32con.SW_SHOWNORMAL: "Normal",
            win32con.SW_SHOWMINIMIZED: "Minimized",
            win32con.SW_SHOWMAXIMIZED: "Maximized",
            -1: "Unknown"
        }
        return states.get(state, f"Unknown ({state})")
    
    # Print the enhanced menu options
    def print_menu(self):
        print("\nEnhanced Windows Inspector - Menu Options:")
        print("1. Show active window info")
        print("2. List all visible windows")
        print("3. Show recent activity")
        print("4. Show usage statistics")
        print("5. Minimize current window")
        print("6. Close current window")
        print("7. Bring window to foreground")
        print("8. Exit")
    
    # Main application loop
    def run(self):
        print("Enhanced Windows Inspector - Comprehensive Window Monitor")
        print("Press Ctrl+C to exit at any time\n")
        
        try:
            while self.running:
                # Get current window info
                hwnd = win32gui.GetForegroundWindow()
                window_info = self.get_window_info(hwnd)
                
                # Update if window changed
                if window_info and (window_info['title'] != self.current_title or 
                        window_info['pid'] != self.current_pid):
                    self.current_window = hwnd
                    self.current_title = window_info['title']
                    self.current_pid = window_info['pid']
                    self.update_window_stats(window_info)
                
                # Display menu and get user input
                self.print_menu()
                choice = input("Enter your choice (1-8): ").strip()
                
                if choice == "1":
                    if window_info:
                        print("\n" + "="*50)
                        print("CURRENT ACTIVE WINDOW")
                        print("="*50)
                        print(f"Title: {window_info['title']}")
                        print(f"PID: {window_info['pid']}")
                        print(f"Process: {window_info['process']['name'] if window_info['process'] else 'Unknown'}")
                        print(f"State: {self.get_state_name(window_info['state'])}")
                        print(f"Position: {window_info['position'][0]}, {window_info['position'][1]}")
                        print(f"Size: {window_info['size'][0]}x{window_info['size'][1]}")
                        print("="*50 + "\n")
                    else:
                        print("\nNo active window detected!\n")
                elif choice == "2":
                    self.display_all_windows()
                elif choice == "3":
                    self.display_activity_log()
                elif choice == "4":
                    self.display_usage_stats()
                elif choice == "5":
                    if hwnd:
                        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
                        print(f"\nMinimized: {window_info['title']}\n")
                    else:
                        print("\nNo active window to minimize!\n")
                elif choice == "6":
                    if hwnd:
                        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                        print(f"\nSent close command to: {window_info['title']}\n")
                    else:
                        print("\nNo active window to close!\n")
                elif choice == "7":
                    if hwnd:
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetForegroundWindow(hwnd)
                        print(f"\nBrought to foreground: {window_info['title']}\n")
                    else:
                        print("\nNo window to bring to foreground!\n")
                elif choice == "8":
                    self.running = False
                else:
                    print("\nInvalid choice. Please try again.\n")
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\nExiting Windows Inspector...")
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")
        finally:
            # Finalize usage statistics before exiting
            now = time.time()
            if self.current_pid in self.window_stats and self.window_stats[self.current_pid]['last_activated']:
                time_elapsed = now - self.last_update_time
                self.window_stats[self.current_pid]['total_time'] += time_elapsed
            
            print("\nFinal Usage Statistics:")
            self.display_usage_stats()
            print("Goodbye!\n")

if __name__ == "__main__":
    # Check if running as admin
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("Running with administrator privileges")
    else:
        print("Running without administrator privileges (some operations might be limited)")
    
    # Create and run the inspector
    inspector = ComprehensiveWindowsInspector()
    inspector.run()