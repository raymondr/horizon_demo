import json
import time

from django import http
from django.utils.dateparse import parse_datetime
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _


from horizon import api
from horizon import exceptions
from horizon import tables
from .tables import FlockingInstancesTable


class IndexView(tables.DataTableView):
    table_class = FlockingInstancesTable
    template_name = 'visualizations/flocking/index.html'

    def get_data(self):
        instances = []
        try:
            instances = api.nova.server_list(self.request, all_tenants=True)
        except:
            exceptions.handle(self.request,
                              _('Unable to retrieve instance list.'))

        # Get the useful data... thanks Nova :-P
        if instances:
            self.correlate_flavors(instances)
            self.correlate_tenants(instances)
            self.correlate_users(instances)
            self.calculate_ages(instances)

        return instances

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            data = json.dumps([i._apiresource._info for i in self.get_data()])
            return http.HttpResponse(data)
        else:
            return super(IndexView, self).get(request, *args, **kwargs)

    def correlate_tenants(self, instances):
        # Gather our tenants to correlate against IDs
        try:
            tenants = api.keystone.tenant_list(self.request, admin=True)
        except:
            tenants = []
            msg = _('Unable to retrieve instance tenant information.')
            exceptions.handle(self.request, msg)
        tenant_dict = SortedDict([(t.id, t) for t in tenants])
        for inst in instances:
            tenant = tenant_dict.get(inst.tenant_id, None)
            inst._apiresource._info['tenant'] = tenant._info
            inst.tenant = tenant

    def correlate_flavors(self, instances):
        # Gather our flavors to correlate against IDs
        try:
            flavors = api.nova.flavor_list(self.request)
        except:
            flavors = []
            msg = _('Unable to retrieve instance size information.')
            exceptions.handle(self.request, msg)

        flavors_dict = SortedDict([(f.id, f) for f in flavors])
        for inst in instances:
            flavor = flavors_dict.get(inst.flavor["id"], None)
            inst._apiresource._info['flavor'] = flavor._info
            inst.flavor = flavor

    def correlate_users(self, instances):
        # Gather our users to correlate against IDs
        try:
            users = api.keystone.user_list(self.request)
        except:
            users = []
            msg = _('Unable to retrieve instance user information.')
            exceptions.handle(self.request, msg)
        user_dict = SortedDict([(u.id, u) for u in users])
        for inst in instances:
            user = user_dict.get(inst.user_id, None)
            inst._apiresource._info['user'] = user._info
            inst.user = user

    def calculate_ages(self, instances):
        for instance in instances:
            dt = parse_datetime(instance._apiresource.created)
            timestamp = time.mktime(dt.timetuple())
            instance._apiresource._info['created'] = timestamp
            instance.age = dt
