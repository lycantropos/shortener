=========
Shortener
=========

Simple application which provides next facilities:

- shortening URLs for authorized users,
- showing stored URLs with number of redirects by shorten links.

Requirements
------------

- ``Docker`` (`installation guide <https://docs.docker.com/engine/installation/>`__),
- ``Docker Compose`` (`installation guide <https://docs.docker.com/compose/install/>`__).

Running with Docker Compose
---------------------------

Run ``Docker`` container

.. code-block:: bash

    docker-compose up

After successful start application should be available at http://localhost:8000/.

Development with Docker Compose
-------------------------------

Run ``Docker`` container with remote debugger

.. code-block:: bash

    ./set-dockerhost.sh docker-compose -f docker-compose.debug.yml up
