from model.model import RoleModel, Role

class RoleController:
    def __init__(self):
        self.model = RoleModel()

    def add_role(self, title, description):
        role = Role(title, description)
        self.model.add_role(role)

    def remove_role(self, title):
        self.model.remove_role(title)

    def get_roles(self):
        return self.model.get_all_roles()

    def get_role_by_title(self, title):
        return self.model.get_role_by_title(title)

    def update_role(self, title, new_title, new_description):
        self.model.update_role(title, new_title, new_description)