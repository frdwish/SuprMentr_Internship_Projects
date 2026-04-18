class PlannerAgent:
    def plan(self, task):
        print("[Planner] Breaking task...")
        
        if "report" in task:
            return ["collect data", "analyze data", "generate report"]
        else:
            return ["execute task"]