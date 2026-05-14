import json
import ast
from helper import getPreParticipantLog
from helper import getPostParticipantLog
from helper import getFunctionDef

class Synthesizer:
    def __init__(self, packagePath):
        try:
            with open(packagePath, 'r') as f:
                self.model = json.loads(f.read())
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            self.model = None

        self.tree = module = ast.Module(
            body=[],
            type_ignores=[]
        )

    def run(self):
        if self.model is None:
            print("No model loaded. Cannot synthesize.")
            return None
            
        for entry in self.model:
            output = self.processBehavior(entry)
            self.tree.body.append(output)
            ast.fix_missing_locations(self.tree)
            print(ast.unparse(self.tree))
        return None
    
    def processBehavior(self, node):
        print(f"Processing behavior: {node['behavior']}")
        body = []

        # Add log statements for pre participants
        for participant in node['pre_participants']:
            print(f"Participant: {participant}")
            logStmt = getPreParticipantLog(participant)
            body.append(logStmt)

        # Add log statements for post participants
        for participant in node['post_participants']:
            print(f"Participant: {participant}")
            logStmt = getPostParticipantLog(participant)
            body.append(logStmt)

        # Process transformation here

        # Create function
        return getFunctionDef(node['behavior'], [], body)