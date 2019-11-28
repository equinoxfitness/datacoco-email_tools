datacoco-email_tools
=======================

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CODE_OF_CONDUCT.rst

datacoco-email_tools provides basic interaction with the Amazon Web
Service (AWS) Simple Email Service.

Installation
------------

datacoco-email_tools requires Python 3.6+

::

    python3 -m venv venv
    source venv/bin/activate
    pip install datacoco_email_tools

Quickstart
----------

Sending email using one line wrapper

::

    Email.send_mail(
        aws_access_key=AWS_ACCESS_KEY,
        aws_secret_key=AWS_SECRET_KEY,
        aws_sender=SENDER,
        aws_region=AWS_REGION,
        to_addr=RECIPIENTS,
        subject='hello world',
        from_addr='email@github.com',
        text_msg='text message',
        html_msg='html message')

Sending email with attachment using one line wrapper

::

    Email.send_email_with_attachment(
        aws_access_key=AWS_ACCESS_KEY,
        aws_secret_key=AWS_SECRET_KEY,
        aws_sender=SENDER,
        aws_region=AWS_REGION,
        to_addr=RECIPIENTS,
        subject='hello world',
        from_addr='email@github.com',
        filename='helloworld.txt',
        body_msg='email body text')

Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment for development:

::

    python3 -m venv <virtual env name>
    source venv/bin/activate
    pip install -r requirements.txt

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox``

Contributing
------------

Contributions to datacoco\_email\_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CONTRIBUTING.rst>`__.