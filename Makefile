.PHONY: tests

# Run pytest with proper Python path
tests:
	@echo "Running tests..."
	poetry run pytest
