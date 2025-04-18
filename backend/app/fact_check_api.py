import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_FACT_CHECK_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")

def google_fact_check(query: str):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": query,
        "key": GOOGLE_FACT_CHECK_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        claims = data.get("claims", [])
        results = []
        for claim in claims:
            text = claim.get("text", "")
            claimant = claim.get("claimant", "")
            claim_review = claim.get("claimReview", [])
            if claim_review:
                review = claim_review[0]
                publisher = review.get("publisher", {}).get("name", "")
                title = review.get("title", "")
                url = review.get("url", "")
                result = f"Claim: {text}\nReviewed by: {publisher}\nVerdict: {title}\nLink: {url}"
                results.append(result)
        return results
    else:
        return [f"Google Fact Check API error: {response.status_code}"]

__all__ = ["google_fact_check"]
