class Role:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class RoleModel:
    def __init__(self):
        self.roles = []

    def add_role(self, role):
        self.roles.append(role)

    def remove_role(self, title):
        self.roles = [role for role in self.roles if role.title != title]

    def get_all_roles(self):
        return self.roles

    def get_role_by_title(self, title):
        for role in self.roles:
            if role.title == title:
                return role
        return None

    def update_role(self, title, new_title, new_description):
        role = self.get_role_by_title(title)
        if role:
            role.title = new_title
            role.description = new_description