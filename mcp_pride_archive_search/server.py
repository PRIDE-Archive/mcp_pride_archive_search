"""
Model Context Protocol (MCP) PRIDE API Server implementation.

This module sets up an MCP-compliant server and registers PRIDE Archive search tools
that follow Anthropic's Model Context Protocol specification. These tools can be
accessed by Claude and other MCP-compatible AI models.
"""
from mcp.server.fastmcp import FastMCP
import argparse
from mcp_pride_archive_search.utils.logging import logger
from mcp_pride_archive_search.services.search_service import fetch_projects
from mcp_pride_archive_search.config import DEFAULT_PORT, DEFAULT_CONNECTION_TYPE

def create_mcp_server(port=DEFAULT_PORT):
    """
    Create and configure the Model Context Protocol server.
    
    Args:
        port: Port number to run the server on
        
    Returns:
        Configured MCP server instance
    """
    mcp = FastMCP("PrideArchiveSearchService", port=port)
    
    # Register MCP-compliant tools
    register_tools(mcp)
    
    return mcp

def register_tools(mcp):
    """
    Register all tools with the MCP server following the Model Context Protocol specification.
    
    Each tool is decorated with @mcp.tool() to make it available via the MCP interface.
    
    Args:
        mcp: The MCP server instance
    """
    @mcp.tool()
    async def search_archive_tool(
        keyword: str,
        page_size: int,
        page: int,
        sort_direction: str,
        sort_fields: str):
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
        return await fetch_projects( keyword,page_size,page,sort_direction,sort_fields)

    @mcp.tool()
    def server_status():
        """
        Check if the Model Context Protocol server is running.
        
        This MCP tool provides a simple way to verify the server is operational.
        
        Returns:
            A status message indicating the server is online
        """
        return {"status": "online", "message": "MCP PRIDE API server is running"}
    
    logger.debug("Model Context Protocol tools registered")

def main():
    """
    Main entry point for the Model Context Protocol PRIDE API Server.
    """
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Model Context Protocol PRIDE API Service")
    parser.add_argument("--connection_type", type=str, default=DEFAULT_CONNECTION_TYPE, 
                        choices=["http", "stdio"], help="Connection type (http or stdio)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, 
                        help=f"Port to run the server on (default: {DEFAULT_PORT})")
    args = parser.parse_args()
    
    # Initialize MCP server
    mcp = create_mcp_server(port=args.port)
    
    if args.connection_type == "http":
        server_type = "sse"
    else:
        server_type = "stdio"
    
    # Start the server
    logger.info(f"🚀 Starting MCP PRIDE API Service on port {args.port} with {args.connection_type} connection")
    mcp.run(server_type)

if __name__ == "__main__":
    main() 