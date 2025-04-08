.PHONY: clean build install dev-install test lint publish

clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name ".eggs" -exec rm -rf {} +

build: clean
	@echo "Building package..."
	python -m build

install:
	@echo "Installing package..."
	pip install .

test:
	@echo "Running tests..."
	pytest

lint:
	@echo "Linting code..."
	isort mcp_pride_archive_search
	black mcp_pride_archive_search
	flake8 mcp_pride_archive_search

publish: clean build
	@echo "Publishing package to PyPI..."
	twine upload dist/*

run:
	@echo "Running MCP PRIDE Archive Search server..."
	python main.py --connection_type http 