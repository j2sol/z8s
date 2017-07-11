# z8s
Zuulernetes -- Launching Zuul with docker-compose, and eventually Kubernetes.

To start, put docker into a swarm mode (which can be a single host).

Copy zuul.conf to zuul.conf.secret and edit to set the github API key (or integration details)

Then: $ docker-compose build

To run: $ docker-compose up

To run with a local checkout of zuul: $ docker-compose -f docker-compose.yaml -f devel.yaml up

The checkout of zuul is volume mounted into the zuul containers. Use the ENV var $ZUUL_SRC to define
the local path where zuul is checked out.

If you are running on a system with SELinux enabled, you will need to allow docker to
access the ZUUL_SRC directory and the z8s directory (containing the zuul.conf.secrets
and cloud.yaml.secrets files) since these are mounted within the containers [1]. You
will have to run commands similar to the following:

$ sudo chcon -Rt svirt_sandbox_file_t $ZUUL_SRC

$ sudo chcon -Rt svirt_sandbox_file_t /path/to/z8s/checkout

References
----------
[1] http://www.projectatomic.io/blog/2015/06/using-volumes-with-docker-can-cause-problems-with-selinux/
