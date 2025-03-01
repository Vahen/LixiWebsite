from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def passions() -> List[Dict]:
    passion_list = [
        {
            'name': "GN",
            'miniature': url_for('static', filename='general/img/miniature/gn_miniature.png'),
            'url': url_for('passions_bp.passions_gn')
        },
        {
            'name': "Travail du cuir",
            'miniature': url_for('static', filename='general/img/miniature/tdc_miniature.png'),
            'url': url_for('travail_du_cuir_bp.travail_du_cuir_page')
        },
        # {
        #     'name': "Jeux de rôle",
        #     'miniature': url_for('static', filename='img/miniature/jdr_miniature_250_250.png'),
        #     'url': url_for('passions_bp.passions_jeux_de_role')
        # },
        # {
        #     'name': "Jeux de societe",
        #     'miniature': url_for('static', filename='img/miniature/jeux_societe_miniature.png'),
        #     'url': url_for('passions_bp.passions_jeux_de_societe')
        # }
    ]
    return passion_list


def passions_short() -> List[Dict]:
    passion_list = passions()[:2]

    return passion_list
