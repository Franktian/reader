# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from apps.cms.panel import PanelBlock

class HomePage(Page):
    content = StreamField([
        ('panel', PanelBlock()),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [StreamFieldPanel('content')],
            heading="Home Panels"
        )
    ]
