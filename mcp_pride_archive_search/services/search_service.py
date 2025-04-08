import aiohttp

"""
PRIDE archive search service implementation.
"""

async def fetch_projects(
        keyword: str,
        page_size: int,
        page: int,
        sort_direction: str,
        sort_fields: str,
):
    """
Fetches proteomics datasets from the PRIDE Archive database.
Use this function when:
- User is looking for proteomics research data
- Questions involve mass spectrometry datasets
- Queries about biological/biomedical datasets (especially cancer-related)
- User wants to find popular or specific proteomics projects

The function supports filtering by keyword, sorting by submissionDate,
and pagination for browsing results.

Args:
        keyword: The keyword for searching projects (e.g., 'Cancer').
        page_size: The number of results per page.
        page: The page number for pagination. Page starts with 0 and default value is 0
        sort_direction: The direction for sorting results ('ASC' or 'DESC').Default is DESC
        sort_fields: The fields to sort by (e.g., 'submissionDate','downloadCount').

Returns:
        A list of project accessions if successful, otherwise a dictionary with an error message.
"""
    url = "https://www.ebi.ac.uk/pride/ws/archive/v3/search/projects"
    params = {
        "keyword": keyword,
        "pageSize": page_size,
        "page": page,
        "sortDirection": sort_direction,
        "sortFields": sort_fields
    }

    # Using aiohttp instead of requests for async operations
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                accessions = [entry["accession"] for entry in data]
                print(accessions)
                return accessions
            else:
                return {"error": f"Request failed with status code {response.status}"}