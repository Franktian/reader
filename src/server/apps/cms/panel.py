from wagtail.wagtailcore import blocks

class PanelBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        required=False,
        help_text="Not diplayed in the app",
    )
    img_url = blocks.URLBlock(
        required=True,
        help_text="https://unsplash.it/1200/1000?image=0"
    )
