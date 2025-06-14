# Represents a user in the social network with friends
class User:
    
    # Initialize a user with ID, name, and empty friends list
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        # List to store friend User objects
        self.friends = []  
    
    # Add another user as a friend (bidirectional connection)
    def add_friend(self, friend_user):
        if friend_user not in self.friends:
            self.friends.append(friend_user)
            # Ensure mutual friendship
            friend_user.friends.append(self)  
    
    # String representation of the user for debugging
    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}')"

# Represents the entire social network graph
class SocialNetwork:
    
    # Initialize an empty social network
    def __init__(self):
        # Dictionary to store users by ID
        self.users = {}  
    
    # Add a user to the network
    def add_user(self, user):
        if user.user_id not in self.users:
            self.users[user.user_id] = user
    
    # Find all friends within n degrees of separation from a starting user.
    def get_friendship_circles(self, start_user_id, max_depth):
        """    
            Args:
                start_user_id: ID of the user to start from
                max_depth: maximum degrees of separation to explore
            Returns:
                Dictionary where keys are degree levels and values are sets of users
        """
        if start_user_id not in self.users:
            raise ValueError("User not found in the network")
        
        # Track visited users to avoid cycles
        visited = set()  
        # Store results by degree level
        circles = {}  
        
        # Initialize recursion
        start_user = self.users[start_user_id]
        self._recursive_find_friends(
            user=start_user,
            current_depth=0,
            max_depth=max_depth,
            visited=visited,
            circles=circles
        )
        
        return circles
    
    # Recursive helper function to traverse the social network.
    def _recursive_find_friends(self, user, current_depth, max_depth, visited, circles):
        """    
            Args:
                user: current User object being processed
                current_depth: current degree of separation from start
                max_depth: maximum allowed depth to explore
                visited: set of already visited user IDs
                circles: dictionary to store results by degree level
        """
        # Base case: stop if we've reached max depth
        if current_depth > max_depth:
            return
        
        # Mark current user as visited
        visited.add(user.user_id)
        
        # Initialize the current depth level in circles if not present
        if current_depth not in circles:
            circles[current_depth] = set()
        
        # Add current user to the appropriate circle
        circles[current_depth].add(user)
        
        # Recursively visit all friends that haven't been visited yet
        for friend in user.friends:
            if friend.user_id not in visited:
                self._recursive_find_friends(
                    user=friend,
                    current_depth=current_depth + 1,
                    max_depth=max_depth,
                    visited=visited,
                    circles=circles
                )

# Demonstrate the social network traversal
def main():
    # Create a social network
    network = SocialNetwork()
    
    # Create some users
    caleb = User(1, "Caleb")
    boromir = User(2, "Boromir")
    Kobe = User(3, "Kobe")
    dave = User(4, "Dave")
    eve = User(5, "Eve")
    frank = User(6, "Frank")
    
    # Add users to the network
    network.add_user(caleb)
    network.add_user(boromir)
    network.add_user(Kobe)
    network.add_user(dave)
    network.add_user(eve)
    network.add_user(frank)
    
    # Establish friendships
    caleb.add_friend(boromir)
    caleb.add_friend(Kobe)
    boromir.add_friend(dave)
    Kobe.add_friend(eve)
    dave.add_friend(frank)
    
    # Find friendship circles for Caleb with max depth 3
    circles = network.get_friendship_circles(start_user_id=1, max_depth=3)
    
    # Print results
    for degree, users in sorted(circles.items()):
        print(f"\nDegree {degree} connections:")
        for user in users:
            print(f"  - {user.name}")
    
if __name__ == "__main__":
    main()

# Expected output:
    # Degree 0 connections:
        # - Caleb
    # Degree 1 connections:
        #   - Boromir")
        #   - Kobe
    # Degree 2 connections:
        #   - Dave
        #   - Eve
    # Degree 3 connections:
        #   - Frank