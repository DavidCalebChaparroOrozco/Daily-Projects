from model.model import MuseumModel
from view.view import MuseumView
from controller.controller import MuseumController

def main():
    # Create model, view, and controller instances
    model = MuseumModel()
    view = MuseumView()
    controller = MuseumController(model, view)
    
    # Add some initial data if the database is empty
    if not model.artifacts:
        initial_data = [
            {
                'name': 'Rosetta Stone',
                'era': 'Ptolemaic Period',
                'culture': 'Ancient Egyptian',
                'location': 'Room 4',
                'description': 'The Rosetta Stone is a granodiorite stele inscribed with a decree issued at Memphis in 196 BC on behalf of King Ptolemy V. The decree appears in three scripts: the upper text is Ancient Egyptian hieroglyphs, the middle portion Demotic script, and the lowest Ancient Greek. Because it presents essentially the same text in all three scripts, it provided the key to the modern understanding of Egyptian hieroglyphs.',
                'image_url': 'https://es.wikipedia.org/wiki/Archivo:Rosetta_Stone.JPG'
            },
            {
                'name': 'Parthenon Marbles',
                'era': 'Classical Greece',
                'culture': 'Ancient Greek',
                'location': 'Room 18',
                'description': 'The Parthenon Marbles are a collection of Classical Greek marble sculptures made under the supervision of the architect and sculptor Phidias and his assistants. They were originally part of the temple of the Parthenon and other buildings on the Acropolis of Athens.',
                'image_url': 'https://en.wikipedia.org/wiki/File:Elgin-marbles-jan-2024.jpg'
            }
        ]
        for artifact in initial_data:
            model.add_artifact(artifact)
    
    if not model.exhibitions:
        model.add_exhibition({
            'title': 'Ancient Civilizations',
            'theme': 'Early Human Societies',
            'start_date': '2023-01-15',
            'end_date': '2023-12-31',
            'description': 'This exhibition explores the great ancient civilizations that shaped human history, from Mesopotamia to Rome.',
            'artifacts': [1, 2]
        })
    
    if not model.tours:
        model.add_tour({
            'name': 'Highlights of the Museum',
            'duration': 60,
            'description': 'This tour takes you through the most famous artifacts in our collection, providing historical context and interesting anecdotes.',
            'video_url': 'https://www.elmamm.org/',
            'stops': [
                {'name': 'Egyptian Gallery', 'description': 'Explore our collection of ancient Egyptian artifacts.'},
                {'name': 'Greek and Roman Wing', 'description': 'Discover the art and culture of classical antiquity.'},
                {'name': 'Medieval Europe', 'description': 'Journey through the Middle Ages with our collection.'}
            ]
        })
    
    # Add admin user if not exists
    if not model.users:
        model.add_user({
            'username': 'admin',
            'password': 'museum123',
            'role': 'admin'
        })
    
    # Start the application
    controller.run()

if __name__ == "__main__":
    main()