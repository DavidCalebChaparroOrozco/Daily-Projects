# Importing necessary libraries
import flet as ft

# Class to represent an Exercise
class Exercise:
    def __init__(self, name):
        self.name = name
        self.records = []  

    # Add a new record of weight and repetitions.
    def add_record(self, weight, repetitions):
        self.records.append({'weight': weight, 'repetitions': repetitions})

# Main app class
class FitnessTrackerApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.exercises = []  

        # Initialize input fields as instance variables
        self.exercise_name = ft.TextField(label="Exercise Name")
        self.weight_input = ft.TextField(label="Weight")
        self.reps_input = ft.TextField(label="Repetitions")
        self.exercises_column = ft.Column()  
        self.stats_container = ft.Container()

    # Build the UI components of the app.
    def build(self):
        return ft.Column(
            controls=[
                self.exercise_name,
                ft.Row(
                    controls=[
                        self.weight_input,
                        self.reps_input,
                        ft.ElevatedButton("Add Exercise", on_click=self.add_exercise),
                    ]
                ),
                self.exercises_column,
                ft.ElevatedButton("Show Statistics", on_click=self.show_statistics),
                self.stats_container
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10
        )

    # Handle adding a new exercise.
    def add_exercise(self, e):
        exercise_name = self.exercise_name.value
        weight = self.weight_input.value
        repetitions = self.reps_input.value

        if exercise_name and weight.isdigit() and repetitions.isdigit():
            exercise = Exercise(exercise_name)
            exercise.add_record(int(weight), int(repetitions))
            self.exercises.append(exercise)

            # Clear input fields
            self.exercise_name.value = ""
            self.weight_input.value = ""
            self.reps_input.value = ""

            # Update the exercises list display
            self.update_exercises_list()
    
    # Update the displayed list of exercises.
    def update_exercises_list(self):
        self.exercises_column.controls.clear()
        for exercise in self.exercises:
            exercise_info = f"{exercise.name}: {exercise.records[-1]['weight']}kg for {exercise.records[-1]['repetitions']} reps"
            self.exercises_column.controls.append(ft.Text(exercise_info))
        self.update()

    # Display statistics for the exercises.
    def show_statistics(self, e):
        stats_text = ""
        for exercise in self.exercises:
            total_weight = sum(record['weight'] for record in exercise.records)
            total_reps = sum(record['repetitions'] for record in exercise.records)
            stats_text += f"{exercise.name} - Total Weight: {total_weight}kg, Total Reps: {total_reps}\n"
        
        # Show statistics in a container
        self.stats_container.content = ft.Text(stats_text)
        self.update()

# Create and run the app
def main(page: ft.Page):
    page.title = "Fitness Tracker"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(FitnessTrackerApp())

ft.app(target=main)
