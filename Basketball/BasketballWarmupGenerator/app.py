from warmupRoutines import WarmUpRoutineGenerator

# Main entry point for the Basketball Warm-Up Routine Generator
def main():
    # Create an instance of the warm-up routine generator
    generator = WarmUpRoutineGenerator()

    # Example usage for different player positions
    positions = ['Point Guard', 'Center', 'Small Forward']
    
    for position in positions:
        print(f"\nWarm-Up Routine for {position}")
        routine = generator.generate_routine(position)
        generator.display_routine(routine)

if __name__ == "__main__":
    main()
