import earthworm_model
import logging
import os
import unittest
from StringIO import StringIO
import csv

# class earthwormQaqcPage(webapp.RequestHandler):
#     def get(self):
#         templatepath = os.path.dirname(__file__) + '/../templates/'
#         ChkCookie = self.request.cookies.get("ubercookie")
#         html = uber_lib.SkinChk(ChkCookie, "Earthworm QA/QC")
#         html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'earthworm','page':'qaqc'})
#         html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
#         html = html + template.render(templatepath + '04uberoutput_start.html', {
#                 'model':'earthworm',
#                 'model_attributes':'Earthworm QAQC'})
# #        html = html =
#         html = html + template.render(templatepath + '04uberinput_end.html', {'sub_title': ''})
#         html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
#         self.response.out.write(html)

# app = webapp.WSGIApplication([('/.*', earthwormQaqcPage)], debug=True)

# def main():
#     run_wsgi_app(app)

# if __name__ == '__main__':
#     main()
