from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):
    def setUp(self):
        super(TestResPartner, self).setUp()
        self.Partner = self.env['res.partner']
        self.SocialNetwork = self.env['social.network']

        self.partner = self.Partner.create({
            'name': 'Test Partner',
        })

        self.facebook = self.SocialNetwork.create({
            'name': 'Facebook',
            'media_type': 'facebook',
        })

        self.twitter = self.SocialNetwork.create({
            'name': 'Instagram',
            'media_type': 'instagram',
        })

    def test_add_social_media(self):
        """Test añadir redes sociales a partner"""
        self.partner.write({
            'social_network_ids': [
                (0, 0, {
                    'social_network_id': self.facebook.id,
                    'url': 'https://facebook.com/test'
                }),
                (0, 0, {
                    'social_network_id': self.instagram.id,
                    'url': 'https://instagram.com/test'
                })
            ]
        })

        self.assertEqual(len(self.partner.social_media_ids), 2)
        self.assertEqual(
            set(self.partner.social_media_ids.mapped('media_type')),
            {'facebook', 'instagram'}
        )

    def test_display_image_computation(self):
        """Test cálculo de imagen para kanban"""
        # Sin imagen ni redes sociales
        self.assertIsNotNone(self.partner.display_image)

        # Con imagen
        self.partner.image = b'TEST_IMAGE'
        self.partner._compute_display_image()
        self.assertEqual(self.partner.display_image, b'TEST_IMAGE')

        # Con redes sociales pero sin imagen
        self.partner.image = False
        self.partner.write({
            'social_network_ids': [(0, 0, {
                'social_network_id': self.facebook.id,
                'url': 'https://facebook.com/test',
            })]
        })
        self.facebook.image = b'FB_IMAGE'
        self.partner._compute_display_image()
        self.assertEqual(self.partner.display_image, b'FB_IMAGE')