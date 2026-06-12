from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

_prompt = PromptTemplate.from_template(
    "You are an expert Business Analyst and Technical Writer.\n\n"
    "Generate a detailed {doc_type} document with this structure:\n{structure}\n\n"
    "Requirements provided by user:\n{requirements}\n\n"
    "Rules:\n"
    "- Be detailed and professional\n"
    "- Use proper headings for each section\n"
    "- Add relevant content under each section\n"
    "- Make it ready for enterprise use\n"
    "- Format clearly with proper structure"
)

chain = _prompt | llm | StrOutputParser()

_doc_structures = {
    "BRD": """
        1. Project Overview
        2. Business Objectives
        3. Scope (In-Scope & Out-Scope)
        4. Functional Requirements
        5. Non-Functional Requirements
        6. Assumptions and Constraints
        7. Risks
    """,
    "BPD": """
        1. Process Overview
        2. Process Objectives
        3. Process Flow
        4. Process Steps (L1, L2, L3)
        5. Roles and Responsibilities
        6. Inputs and Outputs
        7. Exception Handling
    """,
    "FD": """
        1. Feature Overview
        2. Feature Description
        3. User Stories
        4. Acceptance Criteria
        5. Technical Specifications
        6. Dependencies
        7. Test Scenarios
    """,
    "TD": """
        1. Technical Overview
        2. Architecture Design
        3. Technology Stack
        4. Component Details
        5. API Specifications
        6. Database Design
        7. Deployment Strategy
    """,
    "Custom": """
        Generate a professional document with appropriate sections
        based on the requirements provided.
    """,
}


def generate_document(doc_type: str, requirements: str):
    structure = _doc_structures.get(doc_type, _doc_structures["Custom"])
    return chain.stream({"doc_type": doc_type, "structure": structure, "requirements": requirements})
