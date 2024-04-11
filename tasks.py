from textwrap import dedent
from crewai import Task


class endpointTasks:
    def create_directory_structure_task(self, agent, endpoints):
        return Task(description=dedent(f"""
    Analyze a given list of endpoints, uncover the underlying directory structure, and generate a comprehensive representation of the application's directory hierarchy. By doing so, you aim to provide developers and stakeholders with a clear and intuitive understanding of the application's organization.
    STEPS
    Carefully examine the provided list of endpoints, paying close attention to the path segments and any apparent directory-like structures.
   a. Identify common prefixes, suffixes, and path patterns that suggest the presence of directories and subdirectories within the application. b. Consider industry-standard naming conventions, best practices for directory organization, and any application-specific patterns that could influence the directory structure. c. Generate a directory hierarchy based on the insights gained from analyzing the endpoints, starting from the root directory and progressively building the tree-like structure. d. If the input is complex or lacks clear patterns, make reasonable assumptions and use your expertise to create a logical and organized directory structure.
    Represent directories using intuitive names that align with their apparent purpose or the endpoints they contain, ensuring clarity and readability.
    Appropriately nest subdirectories within parent directories to accurately reflect the hierarchical relationships present in the endpoint paths.
    Always generate a directory structure, even if the input is complex or lacks a pre-existing structure. Use your best judgment and expertise to create a logical and organized hierarchy.

                                       INPUT: {endpoints}"""),
                    expected_output="""
    a clean and intuitive tree-like format.
    Use appropriate indentation and symbols (e.g., ├─ for directories, └─ for files) to visually represent the hierarchical relationships between directories and files.
    Ensure that the "GENERATED DIRECTORY STRUCTURE" section exclusively contains the directory tree representation, without any additional text or explanations.
""", agent=agent)

    def add_to_directory_structure_task(self, agent, endpoints, structure):
        return Task(description=dedent(f"""
Analyze a given list of endpoints and an existing directory structure, your task is to integrate the new endpoints into the existing structure, making appropriate modifications and additions. By doing so, you aim to provide developers and stakeholders with a clear and intuitive understanding of the application's organization.
STEPS
Carefully examine the provided list of endpoints, paying close attention to the path segments and any apparent directory-like structures.
a. Analyze the existing structure to understand its organization and naming conventions. b. Identify the appropriate locations within the structure where the new endpoints should be placed based on their path segments and functionality. c. Modify the existing structure by adding new directories or files as necessary to accommodate the new endpoints.
Represent directories using intuitive names that align with their apparent purpose or the endpoints they contain, ensuring clarity and readability.
Appropriately nest subdirectories within parent directories to accurately reflect the hierarchical relationships present in the endpoint paths.
Always generate a directory structure, even if the input is complex or lacks a pre-existing structure. Use your best judgment and expertise to create a logical and organized hierarchy.

                                                                INPUT: {endpoints}
                                                                Known Directory Structure: {structure}"""), expected_output="""
a clean and intuitive tree-like format.
    Use appropriate indentation and symbols (e.g., ├─ for directories, └─ for files) to visually represent the hierarchical relationships between directories and files.
    Ensure that the "GENERATED DIRECTORY STRUCTURE" section exclusively contains the directory tree representation, without any additional text or explanations.
""", agent=agent)

    def check_directory_structure_task(self, agent, context, endpoints):
        return Task(description=dedent(f"""Check a given directory structure to ensure its accuracy, cleanliness, and alignment with the provided list of endpoints. By meticulously examining the directory hierarchy and endpoint paths, you aim to identify and rectify any inconsistencies, inaccuracies, or inefficiencies in the structure. Your task is to optimize the directory tree, remove redundant or unnecessary elements, and ensure that the endpoints are accurately represented in the structure. Your attention to detail and expertise will help developers and stakeholders navigate the application's architecture effectively. Also, make sure that there are no direct references to image files (instead just [image])
                                       INPUT: {endpoints}
                                       """), expected_output="""a clean and intuitive tree-like format.
    Use appropriate indentation and symbols (e.g., ├─ for directories, └─ for files) to visually represent the hierarchical relationships between directories and files.
    Ensure that the "GENERATED DIRECTORY STRUCTURE" section exclusively contains the directory tree representation, without any additional text or explanations. """, agent=agent, context=context)

    def check_add_to_directory_structure_task(self, structure, endpoints, agent, context):
        return Task(description=dedent(f"""Check a given directory structure to ensure its accuracy, cleanliness, and alignment with the provided list of endpoints. By meticulously examining the directory hierarchy and endpoint paths, you aim to identify and rectify any inconsistencies, inaccuracies, or inefficiencies in the structure. Your task is to optimize the directory tree, remove redundant or unnecessary elements, and ensure that the endpoints are accurately represented in the structure. Your attention to detail and expertise will help developers and stakeholders navigate the application's architecture effectively. Also, make sure that there are no direct references to image files (instead just [image]).
                                       Structure: {structure}
                                       Endpoints: {endpoints}
                                       """), expected_output="""a clean and intuitive tree-like format.
    Use appropriate indentation and symbols (e.g., ├─ for directories, └─ for files) to visually represent the hierarchical relationships between directories and files.
    Ensure that the "GENERATED DIRECTORY STRUCTURE" section exclusively contains the directory tree representation, without any additional text or explanations. """, agent=agent, context=context)

    def analyze_directory_structure_task(self, structure, agent, context):
        return Task(description=dedent(f"""Analyze a given directory structure to determine the underlying tech stack used in the application. By examining the directory hierarchy, you aim to identify the technologies, frameworks, and languages employed in the development of the application. Your analysis should provide developers and stakeholders with valuable insights into the technology stack, enabling them to make informed decisions and plan future development efforts effectively.
        STEPS
        Examine the directory structure provided, paying close attention to the names of directories, subdirectories, and files.
        Identify common naming patterns, keywords, and file extensions that indicate the presence of specific technologies or frameworks.
        Cross-reference the identified patterns with industry-standard tech stack configurations and best practices to validate your findings.
        Generate a detailed report outlining the technologies, frameworks, and languages inferred from the directory structure.
                                       Directory Structure: {structure}"""), expected_output="""a comprehensive breakdown of the tech stack used in the application.
        Include a list of technologies, frameworks, and languages identified in the directory structure, along with any additional insights or observations.""", context=context, agent=agent)

    def produce_endpoints(self, structure, techstack, agent, context):
        return Task(description=dedent(f"""Generate a list of possible endpoints based on a given directory structure and tech stack. By leveraging your expertise in directory structures and tech stacks, you aim to identify potential endpoints that align with the application's architecture and technology stack. Your task is to think creatively and propose endpoints that reflect the functionality and design of the application, providing developers and stakeholders with valuable insights for further development.
        STEPS
        Analyze the provided directory structure and tech stack to gain a deep understanding of the application's architecture and technology choices.
        Identify key directories, subdirectories, and files that could serve as endpoints or contribute to endpoint generation.
        Consider the naming conventions, file extensions, and tech stack components present in the structure to inform your endpoint selection.
        Generate a list of 1000 possible endpoints that align with the application's functionality, design, and technology stack.
                                       Directory Structure: {structure}
        Tech Stack: {techstack}"""), output_instructions="""a list of 300 possible endpoints that do not already exist in the directory structure that reflect the application's architecture and technology stack.""", agent=agent, context=context)
