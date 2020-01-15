datacoco-email_tools
=======================

.. image:: https://badge.fury.io/py/datacoco-email-tools.svg
    :target: https://badge.fury.io/py/datacoco-email-tools
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/datacoco-email-tools/badge/?version=latest
    :target: https://datacoco-email-tools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://api.codacy.com/project/badge/Grade/8367602b061d48af9e396cda3231cf59
    :target: https://www.codacy.com/manual/meikalei/datacoco-email_tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-email_tools&amp;utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://api.codacy.com/project/badge/Coverage/8367602b061d48af9e396cda3231cf59
    :target: https://www.codacy.com/manual/meikalei/datacoco-email_tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-email_tools&amp;utm_campaign=Badge_Coverage
    :alt: Coverage

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

datacoco-email_tools provides basic interaction with the Amazon Web
Service (AWS) Simple Email Service.

Installation
------------

datacoco-email_tools requires Python 3.6+

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install datacoco-email-tools

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
    source <virtual env name>/bin/activate
    pip install -r requirements.txt

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``

Contributing
------------

Contributions to datacoco\_email\_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CONTRIBUTING.rst>`__.