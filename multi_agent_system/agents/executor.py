class ExecutorAgent:
    def execute(self, subtask):
        print(f"[Executor] Working on: {subtask}")
        
        if subtask == "collect data":
            return "data collected"
        elif subtask == "analyze data":
            return "data analyzed"
        elif subtask == "generate report":
            return "report generated"
        else:
            return "task done"