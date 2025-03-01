from flask import render_template, make_response

from application.laboratoire.website_stats import website_stats_bp

from application.laboratoire.data import laboratoire_list


############################################
#                Apps                      #
############################################

@website_stats_bp.route('/')
def website_stats():
    return make_response(render_template('website_stats.html', title="Website_stats"), 200)
