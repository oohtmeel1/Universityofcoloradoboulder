#%%
from lxml import etree
from io import StringIO, BytesIO
import urllib.request

# %%

# Now we need to read this document 
def homepage(request):
    file = urllib2.urlopen('https://data.usgs.gov/datacatalog/metadata/USGS.283b1aa6-9268-4010-87da-45d496f63f90.xml')
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    return render_to_response('my_template.html', {'data': data})
# %%
