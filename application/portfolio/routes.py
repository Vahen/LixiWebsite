from flask import render_template, make_response

from application.portfolio import data, portfolio_bp
from application.portfolio.data_folder import data_site_perso, data_pacman3d, data_webcrawler, data_plateforme_game, data_runner, \
    data_acronymos, data_anagramos, data_string_to_leet, data_raytracer, data_2048


############################################
#             Portfolio                    #
############################################

# Les routes ont pour prefix : url_prefix="/portfolio"

@portfolio_bp.route('/')
def portfolio():
    project_m = data.projects()
    return make_response(render_template('portfolio.html', title="Portfolio", projectList=project_m), 200)


@portfolio_bp.route('/vahen_website')
def portfolio_vahen_website():
    skills_back = data_site_perso.skills_back()
    skills_front = data_site_perso.skills_front()
    return make_response(render_template('projects/vahen_website.html', title="Site personnel", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/pacman3d')
def portfolio_pacman3d():
    skills_back = data_pacman3d.skills_back()
    screenshots_gallery = data_pacman3d.screenshots()
    return make_response(render_template('projects/pacman3d.html', title="Pacmand 3D", skills_back=skills_back, screenshots_gallery=screenshots_gallery), 200)


@portfolio_bp.route('/webcrawler')
def portfolio_webcrawler():
    skills_back = data_webcrawler.skills_back()
    skills_front = data_webcrawler.skills_front()
    return make_response(render_template('projects/webcrawler.html', title="WebCrawler", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/raytracer')
def portfolio_raytracer():
    skills_back = data_raytracer.skills_back()
    screenshots_gallery = data_raytracer.screenshots()
    return make_response(render_template('projects/raytracer.html', title="Raytracer", skills_back=skills_back, screenshots_gallery=screenshots_gallery), 200)


@portfolio_bp.route('/plateforme_game')
def portfolio_plateforme_game():
    skills_back = data_plateforme_game.skills_back()
    skills_front = data_plateforme_game.skills_front()
    return make_response(render_template('projects/plateforme_game.html', title="Plateforme Game", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/runner')
def portfolio_runner():
    skills_back = data_runner.skills_back()
    skills_front = data_runner.skills_front()
    return make_response(render_template('projects/runner.html', title="Runner", skills_back=skills_back, skills_front=skills_front), 200)


# @portfolio_bp.route('/acronymos')
# def portfolio_acronymos():
#     skills_back = data_acronymos.skills_back()
#     skills_front = data_acronymos.skills_front()
#     return make_response(render_template('projects/acronymos.html', title="Acronymos", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/anagramos')
def portfolio_anagramos():
    skills_back = data_anagramos.skills_back()
    skills_front = data_anagramos.skills_front()
    return make_response(render_template('projects/anagramos.html', title="Anagramos", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/string_to_leet')
def portfolio_string_to_leet():
    skills_back = data_string_to_leet.skills_back()
    skills_front = data_string_to_leet.skills_front()
    return make_response(render_template('projects/string_to_leet.html', title="String to leet", skills_back=skills_back, skills_front=skills_front), 200)


@portfolio_bp.route('/2048')
def portfolio_2048():
    skills_back = data_2048.skills_back()
    screenshots_gallery = data_2048.screenshots()
    return make_response(render_template('projects/2048.html', title="2048", skills_back=skills_back, screenshots_gallery=screenshots_gallery), 200)
