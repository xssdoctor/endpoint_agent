# endpoint_agent
uses crewai to create a list of possible new endpoints from a list of existing endpoints

# installation
```bash
git clone https://github.com/xssdoctor/endpoint_agent.git
cd endpoint_agent
pip install -r requirements.txt
```

# Usage
```bash
python endpoint_agent.py <input_file>
``` 

# WARNING

this uses many many tokens and may be expensive. Use at your own risk. Output is best in gpt-4-turbo or claude-3-opus
