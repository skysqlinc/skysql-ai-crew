from skysql_ai_crew.crew import crew

def main():
    print("🔍 SkySQL Semantic Agent (CrewAI)\nType 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        result = crew.kickoff(inputs={"user_input": user_input})
        print(f"\nAgent:\n{result}")
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
