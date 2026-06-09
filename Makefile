deploy:
	docker-compose up -d --build
audit:
	python3 src/threat_analyzer.py
