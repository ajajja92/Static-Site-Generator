import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    text_node = TextNode("This is a simple text", text_type_text)
    bold_node = TextNode("This is bold", text_type_bold)
    italic_node = TextNode("This is italic", text_type_italic)
    code_node = TextNode("This is code", text_type_code)
    link_node = TextNode("Visit here", text_type_link, "https://www.example.com")
    image_node = TextNode("Image description", text_type_image, "https://www.example.com/image.png")
    
    def test_eq(self):
        node = TestTextNode.text_node
        node2 = TestTextNode.text_node
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TestTextNode.link_node
        node2 = TestTextNode.image_node
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TestTextNode.bold_node
        self.assertIsNone(node.url)

    def test_url_none(self):
        node = TestTextNode.link_node
        self.assertIsNotNone(node)

    def test_instance(self)
        node = TestTextNode.bold_node
        self.assertIsInstance


    
if __name__ == "__main__":
    unittest.main()