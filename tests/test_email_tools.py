import unittest
from unittest.mock import patch
from datacoco_email_tools import Email


class TestEmail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.email = Email()
        cls.expected_response = {"MessageId": "string"}
        cls.exp_response_html = {
            "Html": {"Charset": "UTF-8", "Data": "<p>Test</p>",}
        }
        cls.exp_response_text = {"Text": {"Charset": "UTF-8", "Data": "Test",}}

    @patch("datacoco_email_tools.email_tools.Email.send_email_with_attachment")
    def test_send_email_with_attachment(self, mock_send_email_with_attachment):
        print("--------------test_send_email_with_attachment")

        mock_send_email_with_attachment.return_value = self.expected_response

        response = self.email.send_email_with_attachment(  # nosec
            aws_access_key="aws_access_key",
            aws_secret_key="aws_secret_key",
            aws_sender="aws_sender",
            aws_region="aws_region",
            to_addr="email@email.com",
            subject="hello world",
            from_addr="email@gmail.com",
            filename="helloworld.txt",
            body_msg="email body text",
        )

        self.assertDictEqual(response, self.expected_response)

    @patch("datacoco_email_tools.email_tools.Email.send_mail")
    def test_send_mail(self, mock_send_mail):
        print("--------------test_send_mail")

        mock_send_mail.return_value = self.expected_response

        response = self.email.send_mail(  # nosec
            aws_access_key="aws_access_key",
            aws_secret_key="aws_secret_key",
            aws_sender="aws_sender",
            aws_region="aws_region",
            to_addr="email@email.com",
            subject="hello world",
            from_addr="email@gmail.com",
            text_msg="text message",
        )

        self.assertDictEqual(response, self.expected_response)

    def test_html(self):
        print("--------------test_html")
        self.email.html("<p>Test</p>")
        self.assertDictEqual(self.email._email_body, self.exp_response_html)

    def test_text(self):
        print("--------------test_text")
        self.email.text("Test")
        self.assertDictEqual(self.email._email_body, self.exp_response_text)

    @patch("datacoco_email_tools.email_tools.Email.send")
    def test_send(self, mock_send):
        print("--------------test_send")

        mock_send.return_value = self.expected_response

        self.email = Email(  # nosec
            recipients="email@email.com",
            subject="hello world",
            aws_access_key="aws_access_key",
            aws_secret_key="aws_secret_key",
            aws_sender="aws_sender",
            aws_region="aws_region",
        )
        self.email.text("Test")
        response = self.email.send("email@gmail.com")

        self.assertDictEqual(response, self.expected_response)

    @patch("datacoco_email_tools.email_tools.Email.send_attachment")
    def test_send_attachment(self, mock_send_attachment):
        print("--------------test_send_attachment")

        mock_send_attachment.return_value = self.expected_response

        body_msg = "email body text"
        from_addr = "email@gmail.com"
        filepath = "tests/test_data/helloworld.txt"

        self.email = Email(  # nosec
            recipients="email@email.com",
            subject="hello world",
            aws_access_key="aws_access_key",
            aws_secret_key="aws_secret_key",
            aws_sender="aws_sender",
            aws_region="aws_region",
        )
        self.email.create_attachment(body_msg, from_addr, filepath)
        response = self.email.send_attachment(from_addr)

        self.assertDictEqual(response, self.expected_response)
