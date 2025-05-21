import unittest
from ix_ghostprotocol.network import NetworkNode, Peer
from ix_ghostprotocol.crypto import generate_keypair

class TestNetworkFunctions(unittest.TestCase):

    def setUp(self):
        self.node = NetworkNode()
        self.pub_key, self.priv_key = generate_keypair()
        self.peer = Peer(public_key=self.pub_key, address="127.0.0.1")

    def test_connect_peer(self):
        result = self.node.connect_peer(self.peer)
        self.assertTrue(result)
        self.assertIn(self.peer.public_key, self.node.peers)

    def test_disconnect_peer(self):
        self.node.connect_peer(self.peer)
        result = self.node.disconnect_peer(self.peer.public_key)
        self.assertTrue(result)
        self.assertNotIn(self.peer.public_key, self.node.peers)

    def test_peer_discovery(self):
        discovered = self.node.discover_peers()
        self.assertIsInstance(discovered, list)

    def test_send_receive_message(self):
        self.node.connect_peer(self.peer)
        message = b"Hello peer"
        msg_id = self.node.send_message(self.peer.public_key, message)
        self.assertIsNotNone(msg_id)

if __name__ == "__main__":
    unittest.main()
