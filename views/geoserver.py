import json
import logging

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from ..REST import rest_funcs

def test_page(request):

    # orv_huc12_json = requests.get(
    #     "http://134.67.114.4/geoserver/rest/workspaces/cite/datastores/huc12s05/featuretypes/huc12s05.json",
    #     auth=('admin', 'geoserver')
    # ).json()
    # logging.info(orv_huc12_json)

    html = render_to_string('geoserver.html', {})

    response = HttpResponse()
    response.write(html)

    return response

@require_POST
def sam_huc_query(request, jid):
    # "20150402133114784000"

    geoserver_post_dict = json.loads(request.body)

    try:
        huc12_id = geoserver_post_dict['features'][0]['properties']['huc12']

    except IndexError:

        html = "Try again..."

        response = HttpResponse()
        response.write(html)

        return response

    try:
        #                                       jid   huc12
        sam_out = rest_funcs.get_sam_huc_output(jid, huc12_id)
        spatial = geoserver_post_dict['features'][0]['properties']
        html = render_to_string('geoserver_details.html', {
            "sam_out": sam_out[0]['model_object_dict']['output'],
            "spatial": spatial
        })

        # If Geoserver returns actual values, below can be used without have to query Mongo for SAM output data
        # html = render_to_string('geoserver_details.html', { "sam_out": geoserver_post_dict['features'][0]['properties'] } )
    except:
        html = "Try again..."

    response = HttpResponse()
    response.write(html)

    return response

@require_POST
def sam_done_query(request, jid):

    request = rest_funcs.get_model_object(jid, "sam")

    response = {}

    if request is None:
        response['done'] = False
    else:
        try:
            if request['output'] == '':
                response['done'] = False
            else:
                logging.info('SAM dumped output to Mongo')
                response['done'] = True
                response['input'] = request['input']
                response['jid'] = jid
        except Exception as e: 
            # html = "except: {}".format(e)
            logging.exception(e)

    # response = HttpResponse()
    # response.write(html)

    return HttpResponse(json.dumps(response), content_type="application/json")
