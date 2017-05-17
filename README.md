# z8s
Zuulernetes -- Launching Zuul with docker-compose, and eventually Kubernetes.

To start, put docker into a swarm mode (which can be a single host).

Copy zuul.conf to zuul.conf.secret and edit to set the github API key (or integration details)

Then: $ docker-compose build

To run: $ docker-compose up
