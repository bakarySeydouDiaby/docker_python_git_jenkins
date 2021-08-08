FROM python:3.6-slim
COPY . /python_docker_jenkins_git
WORKDIR /python_docker_jenkins_git
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null