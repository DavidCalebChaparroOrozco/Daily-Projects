# Import necessary libraries
import pkg_resources
from collections import defaultdict
import sys

# A recursive dependency manager that checks conflicts against currently installed packages.
# This class checks dependency requirements against packages installed in the current Python environment.
class InstalledDependencyManager:
    # Initialize with the currently installed packages from the environment.
    def __init__(self):
        # Dictionary to store package requirements we want to check
        self.requirements_to_check = {}
        
        # Set to track visited packages during resolution
        self.visited = set()
        
        # Get all installed packages in the current environment
        self.installed_packages = {pkg.key: pkg for pkg in pkg_resources.working_set}
    
    # Add a package requirement to be checked against installed packages.
    def add_requirement(self, package_name, version_spec):
        """        
        Args:
            package_name: Name of the package
            version_spec: Version specification (e.g., ">=2.0.0")
        """
        self.requirements_to_check[package_name.lower()] = version_spec
    
    # Check all added requirements against installed packages.
    def check_conflicts(self):
        """        
        Returns:
            dict: Conflict report {package: error_message} if conflicts found
            None: If no conflicts found
        """
        conflicts = {}
        
        for pkg_name, version_spec in self.requirements_to_check.items():
            try:
                self._resolve_dependencies(pkg_name, version_spec)
            except ValueError as e:
                conflicts[pkg_name] = str(e)
        
        return conflicts if conflicts else None
    
    # Recursively resolve dependencies for a package requirement.
    def _resolve_dependencies(self, package_name, version_spec):
        """        
        Args:
            package_name: Name of the package
            version_spec: Version specification
            
        Raises:
            ValueError: If conflict is found
        """
        if (package_name, version_spec) in self.visited:
            return
            
        self.visited.add((package_name, version_spec))
        
        # Check if package is installed
        installed_pkg = self.installed_packages.get(package_name.lower())
        
        if installed_pkg:
            if not self._check_version(installed_pkg.version, version_spec):
                raise ValueError(
                    f"Version conflict: {package_name} {installed_pkg.version} installed "
                    f"but {version_spec} required"
                )
            
            # Recursively check dependencies of the installed package
            for req in installed_pkg.requires():
                self._resolve_dependencies(req.key, str(req.specifier))
    
    # Check if installed version satisfies the requirement.
    def _check_version(self, installed_version, required_spec):
        """        
        Args:
            installed_version: Currently installed version
            required_spec: Required version specification
            
        Returns:
            bool: True if version satisfies requirement
        """
        # Create a requirement object for easy comparison
        req = pkg_resources.Requirement.parse(f"dummy{required_spec}")
        
        # Create a dummy package with the installed version
        installed_pkg = pkg_resources.Distribution(
            project_name="dummy",
            version=installed_version
        )
        
        return installed_pkg in req
    
    # Print a report of installed packages and potential conflicts.
    def print_environment_report(self):
        print("\nCurrently installed packages:")
        for pkg in sorted(self.installed_packages.values(), key=lambda x: x.key):
            print(f"- {pkg.key} {pkg.version}")
            
        conflicts = self.check_conflicts()
        if conflicts:
            print("\nCONFLICTS FOUND:")
            for pkg, error in conflicts.items():
                print(f"{pkg}: {error}")
        else:
            print("\nNo conflicts found with added requirements.")

# Demonstrate the dependency checker with the current environment.
def main():
    dm = InstalledDependencyManager()
    
    # Add some requirements to check against installed packages
    dm.add_requirement("requests", ">=2.25.0")
    dm.add_requirement("numpy", ">=1.20.0")
    dm.add_requirement("pandas", ">=1.3.0")
    
    # Print environment report
    dm.print_environment_report()
    
    # Example of adding a conflicting requirement
    print("\nAdding conflicting requirement...")
    # This will likely conflict
    dm.add_requirement("requests", "<=2.20.0")  
    dm.print_environment_report()

if __name__ == "__main__":
    main()