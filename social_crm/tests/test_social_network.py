from odoo.tests.common import TransactionCase

class TestSocialNetwork(TransactionCase):
    def setUp(self):
        super(TestSocialNetwork, self).setUp()
        self.SocialNetwork = self.env['social.network']
        self.social_network = self.SocialNetwork.create({
            'name': 'Facebook Test',
            'media_type': 'facebook',
        })

    def test_create_social_network(self):
        """Test creación de red social"""
        self.assertEqual(self.social_network.name, 'Facebook Test')
        self.assertEqual(self.social_network.media_type, 'facebook')

    def test_unlink_social_media(self):
        """Test eliminación de red social"""
        media_count = self.SocialNetwork.search_count([])
        self.social_media.unlink()
        self.assertEqual(self.SocialNetwork.search_count([]), media_count - 1)
