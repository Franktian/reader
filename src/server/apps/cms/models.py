# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
)

class HomePage(Page):
    page_name = models.BooleanField(
        blank=True,
        default=False,
    )

    content_panels = Page.content_panels + [
        FieldPanel(
            'page_name',
        ),
    ]
