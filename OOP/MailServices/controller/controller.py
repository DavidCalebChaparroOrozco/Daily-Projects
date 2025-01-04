import json
import csv
from model.model import PackageService
from view.view import View

class Controller:
    def __init__(self):
        self.service = PackageService()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.display_menu()
            if choice == '1':
                self.view.show_packages(self.service.get_all_packages())
            elif choice == '2':
                package_info = self.view.get_package_info()
                self.service.add_package(package_info)
            elif choice == '3':
                package_id = self.view.get_package_id("remove")
                self.service.remove_package(package_id)
            elif choice == '4':
                package_id = self.view.get_package_id("modify")
                new_info = self.view.get_package_info()
                self.service.modify_package(package_id, new_info)
            elif choice == '5':
                search_term = self.view.get_search_term()
                results = self.service.search_package(search_term)
                self.view.show_packages(results)
            elif choice == '6':
                weight_limit = self.view.get_weight_filter()
                filtered_packages = self.service.filter_packages_by_weight(weight_limit)
                self.view.show_packages(filtered_packages)
            elif choice == '7':
                sorted_packages = self.service.sort_packages_by_weight()
                self.view.show_packages(sorted_packages)
            elif choice == '8':
                self.view.show_statistics(self.service.get_statistics())
            elif choice == '9':
                filename = self.view.get_filename("save")
                filetype = self.view.get_filetype()
                if filetype == 'json':
                    self.save_to_json(filename)
                elif filetype == 'csv':
                    self.save_to_csv(filename)
            elif choice == '10':
                filename = self.view.get_filename("load")
                filetype = self.view.get_filetype()
                if filetype == 'json':
                    self.load_from_json(filename)
                elif filetype == 'csv':
                    self.load_from_csv(filename)
            elif choice == '11':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    # Save packages to a JSON file.
    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.service.get_all_packages(), json_file, indent=4)
        print(f"Packages saved to {filename} successfully.")

    # Load packages from a JSON file.
    def load_from_json(self, filename):
        with open(filename, 'r') as json_file:
            packages = json.load(json_file)
            for pkg in packages:
                self.service.add_package(pkg)
        print(f"Packages loaded from {filename} successfully.")

    # Save packages to a CSV file.
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['id', 'description', 'weight'])
            writer.writeheader()
            writer.writerows(self.service.get_all_packages())
        print(f"Packages saved to {filename} successfully.")

    # Load packages from a CSV file.
    def load_from_csv(self, filename):
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            row['weight'] = float(row['weight']) 
            for row in reader:
                self.service.add_package(row)
        print(f"Packages loaded from {filename} successfully.")
