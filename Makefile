devserver: 
	@echo "Starting dev server..."
	php -S localhost:8000 -t .

install:
	@echo "Installing dev requirements..."
	python3 -m pip install TapoP100-main.zip
	@touch iterate.env
	@echo 1 >iterate.env
	touch credentials.env
	@echo "johndoe@example.com" >credentials.env
	@echo "password123" >>credentials.env
	@echo "http://example.com" >>credentials.env
	@touch access.log

uninstall:
	@echo "Uninstalling dev requirements..."
	python3 -m pip uninstall TapoP100
	@rm -f iterate.env
	@rm -f credentials.env
	@rm -f access.log
	@echo "Uninstall complete."