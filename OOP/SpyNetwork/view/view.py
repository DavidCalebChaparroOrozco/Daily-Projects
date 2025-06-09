from datetime import datetime
from tabulate import tabulate

class SpyView:
    # Initialize the view with common display setting
    def __init__(self):
        self.SECTION_WIDTH = 60
        self.COLOR_RED = '\033[91m'
        self.COLOR_GREEN = '\033[92m'
        self.COLOR_YELLOW = '\033[93m'
        self.COLOR_BLUE = '\033[94m'
        self.COLOR_RESET = '\033[0m'

    # Display the main men
    def display_menu(self):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'SPY NETWORK MANAGEMENT SYSTEM BY DAVID CALEB'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║{'MAIN MENU'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ 1. Manage Spies{' ' * (self.SECTION_WIDTH - 16)}║")
        print(f"║ 2. Manage Missions{' ' * (self.SECTION_WIDTH - 19)}║")
        print(f"║ 3. Manage Information Leaks{' ' * (self.SECTION_WIDTH - 28)}║")
        print(f"║ 4. Generate Reports{' ' * (self.SECTION_WIDTH - 20)}║")
        print(f"║ 5. Exit{' ' * (self.SECTION_WIDTH - 8)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display the spy management submen
    def display_spy_menu(self):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'SPY MANAGEMENT'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ 1. Add New Spy{' ' * (self.SECTION_WIDTH - 15)}║")
        print(f"║ 2. View All Spies{' ' * (self.SECTION_WIDTH - 18)}║")
        print(f"║ 3. View Spy Details{' ' * (self.SECTION_WIDTH - 20)}║")
        print(f"║ 4. Deactivate Spy{' ' * (self.SECTION_WIDTH - 18)}║")
        print(f"║ 5. Back to Main Menu{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display the mission management submen
    def display_mission_menu(self):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'MISSION MANAGEMENT'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ 1. Create New Mission{' ' * (self.SECTION_WIDTH - 22)}║")
        print(f"║ 2. View All Missions{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"║ 3. View Mission Details{' ' * (self.SECTION_WIDTH - 24)}║")
        print(f"║ 4. Assign Spy to Mission{' ' * (self.SECTION_WIDTH - 25)}║")
        print(f"║ 5. Complete Mission{' ' * (self.SECTION_WIDTH - 20)}║")
        print(f"║ 6. Back to Main Menu{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display the information leak submen
    def display_leak_menu(self):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'INFORMATION LEAK MANAGEMENT'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ 1. Create New Leak{' ' * (self.SECTION_WIDTH - 19)}║")
        print(f"║ 2. View All Leaks{' ' * (self.SECTION_WIDTH - 18)}║")
        print(f"║ 3. View Leak Details{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"║ 4. Verify Leak{' ' * (self.SECTION_WIDTH - 15)}║")
        print(f"║ 5. Back to Main Menu{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display the report generation submen
    def display_report_menu(self):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'REPORT GENERATION'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ 1. Network Status Report{' ' * (self.SECTION_WIDTH - 25)}║")
        print(f"║ 2. Active Missions Report{' ' * (self.SECTION_WIDTH - 26)}║")
        print(f"║ 3. Spy Skills Inventory{' ' * (self.SECTION_WIDTH - 24)}║")
        print(f"║ 4. Leak Analysis{' ' * (self.SECTION_WIDTH - 17)}║")
        print(f"║ 5. Back to Main Menu{' ' * (self.SECTION_WIDTH - 21)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Get input from the user with a custom promp
    def get_user_input(self, prompt):
        return input(f"{self.COLOR_YELLOW}{prompt}: {self.COLOR_RESET}")

    # Display a message to the user (error or success
    def display_message(self, message, is_error=False):
        if is_error:
            print(f"{self.COLOR_RED}[!] {message}{self.COLOR_RESET}")
        else:
            print(f"{self.COLOR_GREEN}[*] {message}{self.COLOR_RESET}")

    # Display detailed information about a sp
    def display_spy_details(self, spy):
        if not spy:
            self.display_message("Spy not found!", is_error=True)
            return
            
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'SPY DETAILS'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ Real Name: {spy['real_name'].ljust(self.SECTION_WIDTH - 12)}║")
        print(f"║ Cover Name: {spy['cover_name'].ljust(self.SECTION_WIDTH - 13)}║")
        print(f"║ Nationality: {spy['nationality'].ljust(self.SECTION_WIDTH - 14)}║")
        print(f"║ Status: {'Active' if spy['active'] else 'Inactive'}{' ' * (self.SECTION_WIDTH - 15)}║")
        print(f"║ Clearance Level: {str(spy['clearance_level']).ljust(self.SECTION_WIDTH - 18)}║")
        print(f"║ Skills: {', '.join(spy['skills']).ljust(self.SECTION_WIDTH - 10)}║")
        print(f"║ Last Mission: {spy['last_mission'] if spy['last_mission'] else 'None'}{' ' * (self.SECTION_WIDTH - 22)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display detailed information about a missio
    def display_mission_details(self, mission):
        if not mission:
            self.display_message("Mission not found!", is_error=True)
            return
            
        status_color = self.COLOR_GREEN if mission['status'] == 'Completed' else \
                        self.COLOR_RED if mission['status'] == 'Failed' else \
                        self.COLOR_YELLOW

        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'MISSION DETAILS'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ Name: {mission['name'].ljust(self.SECTION_WIDTH - 7)}║")
        print(f"║ Objective: {mission['objective'].ljust(self.SECTION_WIDTH - 12)}║")
        print(f"║ Location: {mission['location'].ljust(self.SECTION_WIDTH - 11)}║")
        print(f"║ Priority: {str(mission['priority']).ljust(self.SECTION_WIDTH - 11)}║")
        print(f"║ Status: {status_color}{mission['status'].ljust(self.SECTION_WIDTH - 9)}{self.COLOR_BLUE}║")
        print(f"║ Required Skills: {', '.join(mission['required_skills']).ljust(self.SECTION_WIDTH - 18)}║")
        print(f"║ Assigned Spies: {str(len(mission['assigned_spies'])).ljust(self.SECTION_WIDTH - 17)}║")
        print(f"║ Start Date: {mission['start_date'] if mission['start_date'] else 'Not started'}{' ' * (self.SECTION_WIDTH - 22)}║")
        print(f"║ End Date: {mission['end_date'] if mission['end_date'] else 'Not completed'}{' ' * (self.SECTION_WIDTH - 20)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display detailed information about an information lea
    def display_leak_details(self, leak):
        if not leak:
            self.display_message("Leak not found!", is_error=True)
            return
            
        verification_status = f"{self.COLOR_GREEN}Verified" if leak['verified'] else f"{self.COLOR_RED}Unverified"
        
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{'LEAK DETAILS'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║ Source: {leak['source'].ljust(self.SECTION_WIDTH - 9)}║")
        print(f"║ Classification: {leak['classification'].ljust(self.SECTION_WIDTH - 17)}║")
        print(f"║ Verification: {verification_status}{self.COLOR_BLUE}{' ' * (self.SECTION_WIDTH - 19)}║")
        print(f"║ Date: {leak['leak_date'].ljust(self.SECTION_WIDTH - 7)}║")
        print(f"║ Recipient: {leak['recipient'] if leak['recipient'] else 'None'}{' ' * (self.SECTION_WIDTH - 16)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║{'CONTENT'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║{leak['content'].ljust(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║{'ENCRYPTED HASH'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        print(f"║{leak['encrypted_content'].ljust(self.SECTION_WIDTH)}║")
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")

    # Display a list of spies in a table forma
    def display_spies_list(self, spies):
        if not spies:
            self.display_message("No spies found!", is_error=True)
            return
            
        table_data = []
        for spy in spies:
            status = "Active" if spy['active'] else "Inactive"
            table_data.append([
                spy['id'][:8] + "...",
                spy['cover_name'],
                spy['real_name'],
                spy['nationality'],
                status,
                ', '.join(spy['skills'][:3]) + ('...' if len(spy['skills']) > 3 else '')
            ])
            
        headers = ["ID", "Cover Name", "Real Name", "Nationality", "Status", "Skills"]
        print(f"\n{self.COLOR_BLUE}{tabulate(table_data, headers=headers, tablefmt='grid')}{self.COLOR_RESET}")

    # Display a list of missions in a table forma
    def display_missions_list(self, missions):
        if not missions:
            self.display_message("No missions found!", is_error=True)
            return
            
        table_data = []
        for mission in missions:
            status_color = self.COLOR_GREEN if mission['status'] == 'Completed' else \
                            self.COLOR_RED if mission['status'] == 'Failed' else \
                            self.COLOR_YELLOW
            table_data.append([
                mission['id'][:8] + "...",
                mission['name'],
                mission['location'],
                mission['priority'],
                f"{status_color}{mission['status']}{self.COLOR_BLUE}",
                str(len(mission['assigned_spies']))
            ])
            
        headers = ["ID", "Name", "Location", "Priority", "Status", "Agents"]
        print(f"\n{self.COLOR_BLUE}{tabulate(table_data, headers=headers, tablefmt='grid')}{self.COLOR_RESET}")

    # Display a list of information leaks in a table forma
    def display_leaks_list(self, leaks):
        if not leaks:
            self.display_message("No leaks found!", is_error=True)
            return
            
        table_data = []
        for leak in leaks:
            verification = f"{self.COLOR_GREEN}✔" if leak['verified'] else f"{self.COLOR_RED}✘"
            table_data.append([
                leak['id'][:8] + "...",
                leak['source'][:15] + ("..." if len(leak['source']) > 15 else ""),
                leak['classification'],
                f"{verification}{self.COLOR_BLUE}",
                leak['leak_date'][:10]
            ])
            
        headers = ["ID", "Source", "Classification", "Verified", "Date"]
        print(f"\n{self.COLOR_BLUE}{tabulate(table_data, headers=headers, tablefmt='grid')}{self.COLOR_RESET}")

    # Display a formatted report based on the report typ
    def display_report(self, report_data, report_type):
        print(f"\n{self.COLOR_BLUE}╔{'═' * self.SECTION_WIDTH}╗")
        print(f"║{f'{report_type.upper()} REPORT'.center(self.SECTION_WIDTH)}║")
        print(f"╠{'═' * self.SECTION_WIDTH}╣")
        
        if report_type == "network status":
            print(f"║{'Spies:'.ljust(20)} {report_data['active_spies']} active, {report_data['inactive_spies']} inactive{' ' * (self.SECTION_WIDTH - 40)}║")
            print(f"║{'Missions:'.ljust(20)} {report_data['missions_completed']} completed, {report_data['missions_failed']} failed, {report_data['missions_in_progress']} in progress{' ' * (self.SECTION_WIDTH - 60)}║")
            print(f"║{'Leaks:'.ljust(20)} {report_data['verified_leaks']} verified, {report_data['unverified_leaks']} unverified{' ' * (self.SECTION_WIDTH - 45)}║")
            
        elif report_type == "active missions":
            headers = ["Mission Name", "Location", "Priority", "Agents", "Days Active"]
            table_data = []
            for mission in report_data:
                start_date = datetime.fromisoformat(mission['start_date']) if mission['start_date'] else datetime.now()
                days_active = (datetime.now() - start_date).days
                table_data.append([
                    mission['name'],
                    mission['location'],
                    mission['priority'],
                    len(mission['assigned_spies']),
                    days_active
                ])
            table_str = tabulate(table_data, headers=headers, tablefmt='plain')
            for line in table_str.split('\n'):
                print(f"║ {line.ljust(self.SECTION_WIDTH - 2)}║")
                
        elif report_type == "skills inventory":
            skills = {}
            for spy in report_data:
                for skill in spy['skills']:
                    skills[skill] = skills.get(skill, 0) + 1
                    
            sorted_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)
            print(f"║{'Top Skills Across All Spies'.center(self.SECTION_WIDTH)}║")
            print(f"╠{'═' * self.SECTION_WIDTH}╣")
            for skill, count in sorted_skills[:10]:
                print(f"║ {skill.ljust(30)} {str(count).ljust(5)} agents{' ' * (self.SECTION_WIDTH - 43)}║")
                
        elif report_type == "leak analysis":
            sources = {}
            classifications = {}
            for leak in report_data:
                sources[leak['source']] = sources.get(leak['source'], 0) + 1
                classifications[leak['classification']] = classifications.get(leak['classification'], 0) + 1
                
            print(f"║{'Leak Sources Analysis'.center(self.SECTION_WIDTH)}║")
            print(f"╠{'═' * self.SECTION_WIDTH}╣")
            for source, count in sorted(sources.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"║ {source.ljust(30)} {str(count).ljust(5)} leaks{' ' * (self.SECTION_WIDTH - 43)}║")
                
            print(f"╠{'═' * self.SECTION_WIDTH}╣")
            print(f"║{'Classification Analysis'.center(self.SECTION_WIDTH)}║")
            print(f"╠{'═' * self.SECTION_WIDTH}╣")
            for classification, count in sorted(classifications.items(), key=lambda x: x[1], reverse=True):
                print(f"║ {classification.ljust(30)} {str(count).ljust(5)} leaks{' ' * (self.SECTION_WIDTH - 43)}║")
                
        print(f"╚{'═' * self.SECTION_WIDTH}╝{self.COLOR_RESET}")