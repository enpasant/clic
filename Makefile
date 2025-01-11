# Variables
PYTHON = python3
VENV = venv
SRC = src
BIN_DIR = $(PREFIX)/bin

# Default rule: Run the main Python script
run:
	$(PYTHON) $(SRC)/clic.py
	@echo "clic Done!"

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created in $(VENV)/"

# Install dependencies in the virtual environment
install: venv
	$(VENV)/bin/pip install -r $(SRC)/make/requirements.txt
	@echo "Dependencies installed."

# Clean up temporary files
clean:
	rm -rf $(VENV)
	find . -name "__pycache__" -exec rm -rf {} +

# Package the application
package: install
	@echo "Packaging clic..."
	@mkdir -p package/DEBIAN
	@chmod 0755 package/DEBIAN
	@echo "Package: clic" > package/DEBIAN/control
	@echo "Version: 1.2" >> package/DEBIAN/control
	@echo "Architecture: all" >> package/DEBIAN/control
	@echo "Maintainer: Your Name <your.email@example.com>" >> package/DEBIAN/control
	@echo "Description: clic package" >> package/DEBIAN/control
	@mkdir -p package$(BIN_DIR)
	@cp $(SRC)/clic.py package$(BIN_DIR)/clic
	@chmod +x package$(BIN_DIR)/clic  # Ensure it's executable
	@dpkg-deb --build package
	@mv package.deb clic_1.2.deb
	@rm -rf package
	@echo "clic packaged as clic_1.2.deb"

.PHONY: run venv install clean package
