import json
import ast
import os
from src.helper import getPreParticipantLog
from src.helper import getPostParticipantLog
from src.helper import getFunctionDef
from src.helper import getConstant
from src.helper import getName
from src.helper import getAssign
from src.helper import getVariableNameWithKeys

class Synthesizer:
    def __init__(self, packagePath):
        self.packagePath = packagePath
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
        
        importNode = ast.parse("from LoggingHelper import semanticLogger").body[0]
        self.tree.body.insert(0, importNode)

        directory = os.getcwd()
        with open(os.path.join(directory, "output", 'synthesized.py'), 'w') as f:
            f.write(ast.unparse(self.tree))

        return None
    
    def processBehavior(self, node):
        body = []

        # Add log statements for pre participants
        for participant in node['pre_participants']:
            logStmt = getPreParticipantLog(participant)
            body.append(logStmt)

        # Process transformation here
        for transformation in node['transformations']:
            if (transformation["type"] == "set"):
                stmt = self.getSetStatement(transformation)
                if stmt is not None:
                    body.append(stmt)

        # Add log statements for post participants
        for participant in node['post_participants']:
            logStmt = getPostParticipantLog(participant)
            body.append(logStmt)

        # Create function
        return getFunctionDef(node['behavior'], node['pre_participants'], body)
    
    def getSetStatement(self, transformation):
        print(f"Processing set transformation: {transformation}")

        # Not supporting keys currently
        if (len(transformation["keys"])) > 0:
            name = getVariableNameWithKeys(transformation["targetParticipantName"], transformation["keys"])
        else:
            name = getName(transformation["targetParticipantName"], ast.Store())

        # Get name node and value or constant based on transformation
        if (transformation["valueType"]["type"] == "constant"):
            value = getConstant(transformation["valueType"]["value"])
        elif (transformation["valueType"]["type"] == "name"):
            value = getName(transformation["valueType"]["value"], ast.Load())
        return getAssign(name, value)
