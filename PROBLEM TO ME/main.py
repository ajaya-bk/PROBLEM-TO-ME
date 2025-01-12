from controllers.problem_controller import ProblemController

def main():
    problem_controller = ProblemController()

    while True:
        print("Community Problem Reporter")
        print("1. Report a Problem")
        print("2. View Reported Problems")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the problem title: ")
            description = input("Enter the problem description: ")
            location = input("Enter the location of the problem: ")
            reporter = input("Enter your name: ")
            problem_controller.report_problem(title, description, location, reporter)
        elif choice == "2":
            problem_controller.view_problems()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
