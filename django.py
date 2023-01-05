from django.conf import settings

from settings.config import Config

#
# Charting configuration
#
settings.PROJECT_PATH_MAP['image_path'] = 'images'

#
# Color configurations
#
PYPLOT_FILL_OPACITY = Config.decimal('ZIMAGI_PYPLOT_FILL_OPACITY', 0.5)

PYPLOT_VALUE_FILL_COLOR = Config.string('ZIMAGI_PYPLOT_VALUE_FILL_COLOR', '#ffcccb')
PYPLOT_MEASURE_FILL_UP_COLOR = Config.string('ZIMAGI_PYPLOT_MEASURE_FILL_UP_COLOR', '#00ffff')
PYPLOT_MEASURE_FILL_DOWN_COLOR = Config.string('ZIMAGI_PYPLOT_MEASURE_FILL_DOWN_COLOR', '#ffd700')

NA_DARK_COLOR = Config.string('ZIMAGI_NA_DARK_COLOR', '#333333')

UP_DARK_COLOR = Config.string('ZIMAGI_UP_DARK_COLOR', '#008080')
DOWN_DARK_COLOR = Config.string('ZIMAGI_DOWN_DARK_COLOR', '#808000')
ZERO_DARK_COLOR = Config.string('ZIMAGI_ZERO_DARK_COLOR', '#333333')
