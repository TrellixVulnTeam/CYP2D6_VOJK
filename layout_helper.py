
import base64
import os

import dash
import dash_core_components as dcc
import dash_html_components as html

def header_colors():
    return {
        'bg_color': '#0C4142',
        'font_color': 'white',
    }

def run_standalone_app(
        layout,
        callbacks,
        header_colors
):
    """Run demo app (tests/dashbio_demos/*/app.py) as standalone app."""
    app = dash.Dash(__name__)
    app.scripts.config.serve_locally = True
    # Handle callback to component with id "fullband-switch"
    app.config['suppress_callback_exceptions'] = True


    app_name = "CYP2D6"

    app_title = "{}".format(app_name.replace('-', ' ').title())

    # Assign layout
    app.layout = app_page_layout(
        page_layout=layout(),
        app_title=app_title,
        app_name=app_name,
        standalone=True,
        **header_colors()
    )

    # Register all callbacks
    callbacks(app)

    # return app object
    return app


def app_page_layout(page_layout,
                    app_title="Dash App",
                    app_name="",
                    light_logo=True,
                    standalone=False,
                    bg_color="#506784",
                    font_color="#F3F6FA"):
    return html.Div(
        id='main_page',
        children=[
            dcc.Location(id='url', refresh=False),
            html.Div(
                id='app-page-header',
                children=[
                    html.A(
                        id='dashbio-logo', children=[
                            html.Img(
                                src='data:image/png;base64,{}'.format(
                                    base64.b64encode(
                                        open(
                                            './assets/plotly-dash-bio-logo.png', 'rb'
                                        ).read()
                                    ).decode()
                                )
                            )],
                        href="/Portal" if standalone else "/dash-bio"
                    ),
                    html.H2(
                        app_title
                    ),

                    html.A(
                        id='gh-link',
                        children=[
                            'View on GitHub'
                        ],
                        href="https://github.com/anny2908/CYP2D6"
                        "blob/master/tests/dashbio_demos/dash-{}/app.py".format(
                            app_name
                        ),
                        style={'color': 'white' if light_logo else 'black',
                               'border': 'solid 1px white' if light_logo else 'solid 1px black'}
                    ),

                    html.Img(
                        src='data:image/png;base64,{}'.format(
                            base64.b64encode(
                                open(
                                    './assets/github.png'.format(
                                        'Light-' if light_logo else ''
                                    ),
                                    'rb'
                                ).read()
                            ).decode()
                        )
                    )
                ],
                style={
                    'background': bg_color,
                    'color': font_color,
                }
            ),
            html.Div(
                id='app-page-content',
                children=page_layout
            )

        ],
        
    )
