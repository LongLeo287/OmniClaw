import os
from atropos import Atropos

# Initialize Atropos with the specified configuration
atropos = Atropos(
    repository=os.environ['REPOSITORY'],
    agent_type=os.environ['AGENT_TYPE'],
    tool_calling=bool(os.environ['TOOL_CALLING']),
    multiturn_loop=bool(os.environ['MULTITURN_LOOP'])
)

# Define the training loop for the LLM agents
def train_agent():
    atropos.train()

if __name__ == '__main__':
    train_agent()