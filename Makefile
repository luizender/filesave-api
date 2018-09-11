SRC_DIR:=./src
DOC_DIR:=./docs
API_DIR:=${SRC_DIR}/api
TESTS_DIR:=${SRC_DIR}/tests

.PHONY: run docs lint tests clean

run:
	PYTHONPATH=${SRC_DIR} python3 ${API_DIR}/app.py

docs:
	sphinx-apidoc -f -o ${DOC_DIR}/source/_modules ./src/ > /dev/null
	sphinx-build -Q ${DOC_DIR}/source/ ${DOC_DIR}/build

lint:
	PYTHONPATH=${SRC_DIR} pylint ${SRC_DIR}

tests:
	PYTHONPATH=${SRC_DIR} STORAGE_ROOT_PATH=/test python3 -m unittest discover -s ${TESTS_DIR}

clean:
	rm -rf ${DOC_DIR}/build ${DOC_DIR}/source/_*
	find ${SRC_DIR} | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
