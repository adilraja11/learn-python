import os
from openai import OpenAI
from dotenv import load_dotenv
from pm import PromptManager

load_dotenv()

CONTEXT = """
Q1: What is Devscale Indonesia?
A1: Devscale Indonesia is a dedicated learning institution focused on equipping individuals with the practical skills and theoretical knowledge required to become proficient software engineers.

Q2: What is the mission of Devscale Indonesia?
A2: Our mission is to bridge the tech talent gap in Indonesia by providing high-quality, accessible, and industry-relevant software engineering education. Also, we aim to help students to boost their potential fire in programming fields

Q3: What types of courses does Devscale Indonesia offer?
A3: Devscale Indonesia offers a variety of courses, including Full-Stack JavaScript Bootcamp, Full-Stack MERN Bootcamp, and AI-Enabled Python Web Development.
"""

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

pm = PromptManager()

while True:
    input_query = input("Query: ")
    pm.add_message("system", f"Answer the question based on this text only: {CONTEXT}")
    pm.add_message("user", input_query)

    result = pm.generate()
    pm.add_message("assistant", result)
    print(result)