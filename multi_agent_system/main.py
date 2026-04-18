from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.validator import ValidatorAgent

def run_system(task):
    planner = PlannerAgent()
    executor = ExecutorAgent()
    validator = ValidatorAgent()

    # Step 1: Plan
    subtasks = planner.plan(task)

    # Step 2: Execute
    results = []
    for subtask in subtasks:
        result = executor.execute(subtask)
        results.append(result)

    # Step 3: Validate
    final_result = validator.validate(results)

    print("\nFinal Output:", final_result)


if __name__ == "__main__":
    run_system("create report")