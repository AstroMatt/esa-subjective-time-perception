from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class IndexDashboard(Dashboard):

    def init_with_context(self, context):

        self.children.append(modules.ModelList(
            title=_('Subjective Time Perception'),
            column=1,
            collapsible=False,
            models=[
                'backend.api_v2.models.*']))

        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('HTTP Request Logger'),
                column=3,
                collapsible=False,
                models=[
                    'backend.logger.models.*']))

            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=False,
                models=['django.contrib.*'],
                css_classes=['grp-closed']))
