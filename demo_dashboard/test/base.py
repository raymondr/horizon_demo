from django import http

from horizon import test


class TestCase(test.BaseAdminViewTests):
    def setUp(self):
        super(TestCase, self).setUp()

    def switch_context(self, user=None, roles=None, authorized_tenants=None):
        user = user or self.user
        authorized_tenants = authorized_tenants or [self.tenant]
        if not hasattr(user, "tenant_id"):
            user.tenant_id = self.tenant.id
        if not hasattr(user, "tenant_name"):
            user.tenant_name = self.tenant.name
        user.authorized_tenants = authorized_tenants
        roles = roles or [self.roles.admin._info]
        self.setActiveUser(id=user.id,
                           token=self.token,
                           username=user.name,
                           tenant_id=user.tenant_id,
                           service_catalog=self.service_catalog,
                           tenant_name=user.tenant_name,
                           roles=roles,
                           authorized_tenants=authorized_tenants)
        self.request = http.HttpRequest()
        self.request.session = self.client._session()
        self.request.session['token'] = self.token.id
