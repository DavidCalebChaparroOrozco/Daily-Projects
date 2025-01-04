class PackageService:
    # Initialize an empty list to store packages.
    def __init__(self):
        self.packages = []

    # Add a new package to the list.
    def add_package(self, package_info):
        self.packages.append(package_info)

    # Remove a package by its ID.
    def remove_package(self, package_id):
        self.packages = [pkg for pkg in self.packages if pkg['id'] != package_id]

    # Modify an existing package's information.
    def modify_package(self, package_id, new_info):
        for pkg in self.packages:
            if pkg['id'] == package_id:
                pkg.update(new_info)
                break

    # Search for packages by description or ID.
    def search_package(self, search_term):
        return [pkg for pkg in self.packages if search_term in pkg['description'] or search_term == pkg['id']]

    # Filter packages that are above a certain weight limit.
    def filter_packages_by_weight(self, weight_limit):
        return [pkg for pkg in self.packages if pkg['weight'] <= weight_limit]

    # Sort packages by their weight.
    def sort_packages_by_weight(self):
        return sorted(self.packages, key=lambda x: x['weight'])

    # Return all packages.
    def get_all_packages(self):
        return self.packages

    # Provide statistics about the packages.
    def get_statistics(self):
        total_packages = len(self.packages)
        return {
            "total_packages": total_packages,
            "packages": self.packages,
        }
