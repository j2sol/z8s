# z8s
Zuulernetes -- Launching Zuul with docker-compose, and eventually Kubernetes.

To start, put docker into a swarm mode (which can be a single host).

Copy zuul.conf to zuul.conf.secret and edit to set the github API key (or integration details)

Then: $ docker-compose build

To run: $ docker-compose up

To run with a local checkout of zuul: $ docker-compose -f docker-compose.yaml -f devel.yaml up

The checkout of zuul is volume mounted into the zuul containers. Use the ENV var $ZUUL_SRC to define
the local path where zuul is checked out.
