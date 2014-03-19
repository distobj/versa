#versa
import gettext
import locale
import logging

def init_localization():
  '''prepare l10n'''
  locale.setlocale(locale.LC_ALL, '') # User's preferred locale, according to environment
  # Use first two characters of country code
  loc = locale.getlocale()
  filename = "res/messages_%s.mo" % locale.getlocale()[0][0:2]

  try:
    logging.debug( "Opening message file %s for locale %s", filename, loc[0] )
    trans = gettext.GNUTranslations(open( filename, "rb" ) )
  except IOError:
    logging.debug( "Locale not found. Using default messages" )
    trans = gettext.NullTranslations()

  trans.install()

