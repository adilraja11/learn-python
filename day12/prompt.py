GENERATE_TITLE_PROMPT = """
Generate a proper title from a topic: {topic}:

IMPORTANT :
- Title must be in clear english
- Title must be engaging 
"""

GENERATE_SECTION_PROMPT = """
Generate sections based on a topic: {topic}

IMPORTANT :
- At least 5 section
- Output must be bullet list
- Do not add any additional text or information or explanation
"""

GENERATE_CONTENT_PROMPT = """
Generate content based on section title : {section_title}
"""