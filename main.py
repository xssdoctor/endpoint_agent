from agents import endpointAgents
from tasks import endpointTasks
from dotenv import load_dotenv
from utils import split_list
import argparse
import sys

load_dotenv('.env')

tasks = endpointTasks()
agents = endpointAgents()

print('## Welcome to the endpoint creator!')
print('-------------------------------')

# Create Agents
directory_structure_creator = agents.directory_structure_creator()
directory_structure_checker = agents.directory_structure_checker()
directory_structure_analyzer = agents.directory_structure_analyzer()
endpoint_creator = agents.endpoint_creator()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a directory structure from a list of endpoints")
    parser.add_argument(
        "file", help="The file containing the list of endpoints")
    args = parser.parse_args()
    listOfEndpointLists = split_list(args.file)
    directory_structure = None
    for endpointList in listOfEndpointLists:
        # create tasks
        if endpointList == listOfEndpointLists[0]:
            from utils import first_part
            directory_structure = first_part(tasks, endpointList, directory_structure_creator,
                                             directory_structure_checker)
        else:
            from utils import next_parts
            directory_structure = next_parts(tasks, endpointList, directory_structure_creator,
                                             directory_structure_checker, directory_structure)
    from utils import final_part
    final_part(tasks, directory_structure, directory_structure,
               directory_structure_checker, directory_structure_analyzer)
