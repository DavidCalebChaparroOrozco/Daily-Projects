class MuseumView:
    def __init__(self):
        # ANSI color codes for colorful UI
        self.colors = {
            'header': '\033[95m',
            'blue': '\033[94m',
            'cyan': '\033[96m',
            'green': '\033[92m',
            'warning': '\033[93m',
            'fail': '\033[91m',
            'end': '\033[0m',
            'bold': '\033[1m',
            'underline': '\033[4m'
        }

    # Display a colorful header.
    def display_header(self, title):
        print(f"\n{self.colors['header']}{'=' * 50}")
        print(f"{title.upper():^50}")
        print(f"{'=' * 50}{self.colors['end']}\n")

    # Display the main menu with options.
    def display_menu(self):
        self.display_header("museum guide interactive system")
        
        menu_options = [
            ("1", "Explore Artifacts"),
            ("2", "View Exhibitions"),
            ("3", "Take a Virtual Tour"),
            ("4", "Manage Artifacts (Admin)"),
            ("5", "Manage Exhibitions (Admin)"),
            ("6", "Manage Tours (Admin)"),
            ("0", "Exit")
        ]
        
        print(f"{self.colors['blue']}Main Menu:{self.colors['end']}")
        for num, option in menu_options:
            print(f"  {self.colors['cyan']}{num}.{self.colors['end']} {option}")
        
        print(f"\n{self.colors['warning']}Enter your choice (0-6):{self.colors['end']} ", end="")
        return input()

    # Display a list of artifacts.
    def display_artifacts(self, artifacts):
        self.display_header("museum artifacts collection")
        
        if not artifacts:
            print(f"{self.colors['warning']}No artifacts found.{self.colors['end']}")
            return
        
        for artifact in artifacts:
            print(f"\n{self.colors['green']}Artifact ID: {artifact['id']}{self.colors['end']}")
            print(f"{self.colors['bold']}Name:{self.colors['end']} {artifact['name']}")
            print(f"{self.colors['bold']}Era:{self.colors['end']} {artifact['era']}")
            print(f"{self.colors['bold']}Culture:{self.colors['end']} {artifact['culture']}")
            print(f"{self.colors['bold']}Description:{self.colors['end']} {artifact['description'][:100]}...")
            print(f"{self.colors['bold']}Location:{self.colors['end']} {artifact['location']}")
            print("=".center(50, '='))

    # Display detailed information about a single artifact.
    def display_artifact_details(self, artifact):
        self.display_header(f"artifact details: {artifact['name']}")
        
        print(f"{self.colors['bold']}ID:{self.colors['end']} {artifact['id']}")
        print(f"{self.colors['bold']}Name:{self.colors['end']} {artifact['name']}")
        print(f"{self.colors['bold']}Era:{self.colors['end']} {artifact['era']}")
        print(f"{self.colors['bold']}Culture:{self.colors['end']} {artifact['culture']}")
        print(f"{self.colors['bold']}Location:{self.colors['end']} {artifact['location']}")
        print(f"\n{self.colors['underline']}Description:{self.colors['end']}\n{artifact['description']}")
        
        if 'image_url' in artifact:
            print(f"\n{self.colors['cyan']}Image available at: {artifact['image_url']}{self.colors['end']}")
        
        print(f"\n{self.colors['warning']}Added on: {artifact['created_at']}{self.colors['end']}")

    # Display a list of exhibitions.
    def display_exhibitions(self, exhibitions):
        self.display_header("current exhibitions")
        
        if not exhibitions:
            print(f"{self.colors['warning']}No exhibitions found.{self.colors['end']}")
            return
        
        for exhibition in exhibitions:
            print(f"\n{self.colors['green']}Exhibition ID: {exhibition['id']}{self.colors['end']}")
            print(f"{self.colors['bold']}Title:{self.colors['end']} {exhibition['title']}")
            print(f"{self.colors['bold']}Theme:{self.colors['end']} {exhibition['theme']}")
            print(f"{self.colors['bold']}Dates:{self.colors['end']} {exhibition['start_date']} to {exhibition['end_date']}")
            print(f"{self.colors['bold']}Description:{self.colors['end']} {exhibition['description'][:100]}...")
            print("=".center(50, '='))

    # Display detailed information about a single exhibition.
    def display_exhibition_details(self, exhibition):
        self.display_header(f"exhibition details: {exhibition['title']}")
        
        print(f"{self.colors['bold']}ID:{self.colors['end']} {exhibition['id']}")
        print(f"{self.colors['bold']}Title:{self.colors['end']} {exhibition['title']}")
        print(f"{self.colors['bold']}Theme:{self.colors['end']} {exhibition['theme']}")
        print(f"{self.colors['bold']}Dates:{self.colors['end']} {exhibition['start_date']} to {exhibition['end_date']}")
        print(f"\n{self.colors['underline']}Description:{self.colors['end']}\n{exhibition['description']}")
        
        if 'artifacts' in exhibition and exhibition['artifacts']:
            print(f"\n{self.colors['bold']}Featured Artifacts:{self.colors['end']}")
            for artifact_id in exhibition['artifacts']:
                print(f"  - Artifact ID: {artifact_id}")
        
        print(f"\n{self.colors['warning']}Added on: {exhibition['created_at']}{self.colors['end']}")

    # Display a list of virtual tours.
    def display_tours(self, tours):
        self.display_header("available virtual tours")
        
        if not tours:
            print(f"{self.colors['warning']}No virtual tours available.{self.colors['end']}")
            return
        
        for tour in tours:
            print(f"\n{self.colors['green']}Tour ID: {tour['id']}{self.colors['end']}")
            print(f"{self.colors['bold']}Name:{self.colors['end']} {tour['name']}")
            print(f"{self.colors['bold']}Duration:{self.colors['end']} {tour['duration']} minutes")
            print(f"{self.colors['bold']}Description:{self.colors['end']} {tour['description'][:100]}...")
            print("=".center(50, '='))

    # Display detailed information about a single tour.
    def display_tour_details(self, tour):
        self.display_header(f"virtual tour: {tour['name']}")
        
        print(f"{self.colors['bold']}ID:{self.colors['end']} {tour['id']}")
        print(f"{self.colors['bold']}Name:{self.colors['end']} {tour['name']}")
        print(f"{self.colors['bold']}Duration:{self.colors['end']} {tour['duration']} minutes")
        print(f"\n{self.colors['underline']}Description:{self.colors['end']}\n{tour['description']}")
        
        if 'stops' in tour and tour['stops']:
            print(f"\n{self.colors['bold']}Tour Stops:{self.colors['end']}")
            for i, stop in enumerate(tour['stops'], 1):
                print(f"  {i}. {stop['name']} - {stop['description'][:50]}...")
        
        if 'video_url' in tour:
            print(f"\n{self.colors['cyan']}Tour video available at: {tour['video_url']}{self.colors['end']}")
        
        print(f"\n{self.colors['warning']}Added on: {tour['created_at']}{self.colors['end']}")

    # Get input for a new artifact from the user.
    def get_artifact_input(self):
        self.display_header("add new artifact")
        
        artifact = {
            'name': input(f"{self.colors['bold']}Artifact Name:{self.colors['end']} "),
            'era': input(f"{self.colors['bold']}Historical Era:{self.colors['end']} "),
            'culture': input(f"{self.colors['bold']}Culture/Origin:{self.colors['end']} "),
            'location': input(f"{self.colors['bold']}Current Location (Gallery/Room):{self.colors['end']} "),
            'description': input(f"{self.colors['bold']}Detailed Description:{self.colors['end']} "),
            'image_url': input(f"{self.colors['bold']}Image URL (optional):{self.colors['end']} ") or None
        }
        
        return artifact

    # Get input for a new exhibition from the user.
    def get_exhibition_input(self):
        self.display_header("add new exhibition")
        
        exhibition = {
            'title': input(f"{self.colors['bold']}Exhibition Title:{self.colors['end']} "),
            'theme': input(f"{self.colors['bold']}Theme:{self.colors['end']} "),
            'start_date': input(f"{self.colors['bold']}Start Date (YYYY-MM-DD):{self.colors['end']} "),
            'end_date': input(f"{self.colors['bold']}End Date (YYYY-MM-DD):{self.colors['end']} "),
            'description': input(f"{self.colors['bold']}Detailed Description:{self.colors['end']} "),
            'artifacts': list(map(int, input(f"{self.colors['bold']}Featured Artifact IDs (comma separated):{self.colors['end']} ").split(',')))
        }
        
        return exhibition

    # Get input for a new virtual tour from the user.
    def get_tour_input(self):
        self.display_header("add new virtual tour")
        
        tour = {
            'name': input(f"{self.colors['bold']}Tour Name:{self.colors['end']} "),
            'duration': int(input(f"{self.colors['bold']}Duration (minutes):{self.colors['end']} ")),
            'description': input(f"{self.colors['bold']}Detailed Description:{self.colors['end']} "),
            'video_url': input(f"{self.colors['bold']}Video URL (optional):{self.colors['end']} ") or None
        }
        
        # Get tour stops
        stops = []
        print(f"\n{self.colors['underline']}Add Tour Stops (leave name blank when done):{self.colors['end']}")
        while True:
            stop_name = input(f"{self.colors['bold']}Stop Name:{self.colors['end']} ")
            if not stop_name:
                break
            stop_desc = input(f"{self.colors['bold']}Stop Description:{self.colors['end']} ")
            stops.append({'name': stop_name, 'description': stop_desc})
        
        if stops:
            tour['stops'] = stops
        
        return tour

    # Get ID input from user for various operations.
    def get_id_input(self, item_type):
        return int(input(f"Enter {item_type} ID: "))

    # Display a message to the user with appropriate coloring.
    def display_message(self, message, is_error=False):
        if is_error:
            print(f"{self.colors['fail']}Error: {message}{self.colors['end']}")
        else:
            print(f"{self.colors['green']}{message}{self.colors['end']}")

    # Display admin login prompt.
    def admin_login(self):
        self.display_header("admin login")
        username = input(f"{self.colors['bold']}Username:{self.colors['end']} ")
        password = input(f"{self.colors['bold']}Password:{self.colors['end']} ")
        return username, password

    # Display admin sub-menu for a specific section.
    def display_admin_menu(self, section):
        self.display_header(f"admin: manage {section}")
        
        menu_options = [
            ("1", f"Add New {section.capitalize()}"),
            ("2", f"View {section.capitalize()} Details"),
            ("3", f"Update {section.capitalize()}"),
            ("4", f"Delete {section.capitalize()}"),
            ("5", f"List All {section.capitalize()}s"),
            ("0", "Back to Main Menu")
        ]
        
        print(f"{self.colors['blue']}Admin Menu:{self.colors['end']}")
        for num, option in menu_options:
            print(f"  {self.colors['cyan']}{num}.{self.colors['end']} {option}")
        
        print(f"\n{self.colors['warning']}Enter your choice (0-5):{self.colors['end']} ", end="")
        return input()