from app.vectorstore import search_chroma, add_to_vectorstore
from app.web_scraper import search_web
from app.fact_check_api import google_fact_check
from app.llm_router import query_llm
from langchain_core.documents import Document

def run_fact_check(user_query: str) -> str:

    local_facts = search_chroma(user_query)

    # Step 2: Search web and Google Fact Check API
    web_results = search_web(user_query)
    fact_checks = google_fact_check(user_query)

    # Combine all into documents
    combined_knowledge = local_facts + web_results + fact_checks

    # Step 3: Index new web/fact-check data into Chroma
    new_docs = [Document(page_content=txt) for txt in web_results + fact_checks]
    add_to_vectorstore(new_docs)

    # Step 4: Send everything to the LLM
    prompt = f"""You are a misinformation detection assistant. Based on the info below, fact-check the following claim:

Claim: {user_query}

Sources:\n\n{combined_knowledge}

Respond with a verdict and short explanation.
"""
    return query_llm(prompt)
