import re
from crewai import Crew

domainRegex = re.compile(r'(https?:\/\/[^\/]+)([^\n?]+)')


def split_list(file):
    # takes a file, returns an array of strings. each string should be 500 lines of the file
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.match(domainRegex, line):
                newLine = re.match(domainRegex, line).group(2)
                lines[lines.index(line)] = newLine
        lines = list(set(lines))

        return ['\n'.join(lines[i:i + 500]) for i in range(0, len(lines), 500)]


def first_part(tasks, endpointList, directory_structure_creator, directory_structure_checker):
    directory_structure = tasks.create_directory_structure_task(
        directory_structure_creator, endpointList)
    directory_checker = tasks.check_directory_structure_task(
        directory_structure_checker, [directory_structure], endpointList)
    creation_crew = Crew(
        agents=[directory_structure_creator,
                directory_structure_checker],
        tasks=[directory_structure, directory_checker],
        verbose=True
    )
    creation_crew.kickoff()
    directory_structure = directory_checker.output.raw_output
    return directory_structure


def next_parts(tasks, endpointList, directory_structure_creator, directory_structure_checker, directory_structure):
    directory_structure_add = tasks.add_to_directory_structure_task(
        directory_structure_creator, endpointList, directory_structure)
    directory_checker = tasks.check_directory_structure_task(
        directory_structure_checker, [directory_structure_add], endpointList)
    creation_crew = Crew(
        agents=[directory_structure_creator,
                directory_structure_checker],
        tasks=[directory_structure, directory_checker],
        verbose=True
    )
    creation_crew.kickoff()
    directory_structure = directory_checker.output.raw_output
    return directory_structure


def final_part(tasks, directory_structure, directory_structure_checker, directory_structure_analyzer):
    directory_analyzer = tasks.analyze_directory_structure_task(
        directory_structure, directory_structure_analyzer, 'tech stack')
    final_crew = Crew(
        agents=[directory_structure_checker],
        tasks=[directory_analyzer],
        verbose=True
    )
    final_crew.kickoff()
    new_endpoints = directory_analyzer.output.raw_output
    with open('endpoints.txt', 'w') as f:
        f.write(new_endpoints)
