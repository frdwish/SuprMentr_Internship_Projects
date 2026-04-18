class ValidatorAgent:
    def validate(self, results):
        print("[Validator] Checking results...")
        
        if all(results):
            return "All tasks completed successfully!"
        else:
            return "Some tasks failed!"