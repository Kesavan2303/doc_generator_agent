from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)   

@tool
def analyze_requirements(requirements: str) -> str:
    """
    Analyze the provided requirements and return a structured summary.
    """
    return f"Analyzed requirements: {requirements}"

tools = [analyze_requirements]
agent = create_react_agent(model=llm, tools=tools)

def generate_document(doc_type: str, requirements: str) -> str:
    
    doc_structures = {
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
        """
    }

    structure = doc_structures.get(doc_type, doc_structures["Custom"])
    prompt = f"""
    You are an expert Business Analyst and Technical Writer.
    
    Generate a detailed {doc_type} document with this structure:
    {structure}
    
    Requirements provided by user:
    {requirements}
    
    Rules:
    - Be detailed and professional
    - Use proper headings for each section
    - Add relevant content under each section
    - Make it ready for enterprise use
    - Format clearly with proper structure
    """
    response = agent.invoke({
        "messages": [{"role": "user", "content": prompt}]
    })

    return response['messages'][-1].content
